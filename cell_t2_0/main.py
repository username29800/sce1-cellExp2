# this script will serve as a server, transmitting str when requested by http
# 1. pre-boot POST routine
# core modules loader
import utils, sys, os, subprocess, time, shutil
config = 'status.txt' # set config file
CELLNAMEPREFIX = utils.auto_find(config, 'defaultname')

# self integrity check
subprocess.call(['python', 'keepalive.py'])

# check availability
def avail():
    avail = utils.auto_flag(config)
    if avail != "active":
        # put error logging code here
        exit()
    # backup origin
    subprocess.call(['python', 'packager.py', 'org', '0'])

# write output
# output contains current date/time, source, destination, and outcontent
def wrtout():
    out_name = utils.auto_find(config, 'out')
    cell_num = utils.get_cell_idx()
    cell_name = CELLNAMEPREFIX + str(cell_num)
    out_file = open(out_name + cell_name + '.txt', 'w')
    wrtstr = utils.auto_find(config, 'outcontent')
    wrtstr += '\n'
    out_file.write(wrtstr)
    out_file.close()
    al_file = utils.auto_find(config, 'al')
    utils.write_add_to_xll(al_file, out_name + cell_name + '.txt')

# return output
def outpost():
    out_name = utils.auto_find(config, 'out')
    cell_num = utils.get_cell_idx()
    cell_name = CELLNAMEPREFIX + str(cell_num)
    subprocess.call(['python', 'packager.py','td', out_name + cell_name + '.txt'])

# check system root for unknown files
def check_system():
    files_root = os.listdir('../')
    als = utils.auto_find(config, 'alsys')
    unknown = utils.xll_find_unknown(als, '..')
    return unknown

def del_unknown(unknown):
    qdir = 'quarantine_sys'
    cdir = os.listdir('..')
    failed = []
    if not(qdir in cdir):
        os.mkdir('../' + qdir)
        als_name = utils.auto_find(config, 'alsys')
        utils.write_add_to_xll(als_name, qdir)
    for i in unknown:
        try:
            shutil.move('../' + i, f'../{qdir}/{i}')
        except Exception as e:
            print(e)
            failed.append(i)

def als_time():
    ct = time.gmtime() # current time
    pt:str = f'{ct.tm_year:04}{ct.tm_mon:02}{ct.tm_mday:02}{ct.tm_hour:02}{ct.tm_min:02}{ct.tm_sec:02}' # printable time
    return pt

# update allowlist
def refresh_als():
    # check for ../post/alsys_(time) for every loop
    als_root = os.listdir('../post')
    time_list = []
    for i in als_root:
        if i[:5] == 'alsys':
            time_als = i.split('_')[1]
            time_als = int(time_als)
            time_list.append(time_als)
    latest = 0
    for i in time_list:
        if i > latest:
            latest = i
    new_fn = 'alsys_' + str(latest)
    als_name = utils.auto_find(config, 'alsys')
    shutil.copy2('../post' + new_fn, als_name)

# post updated alsys (system-wide allowlist) - also required in normal cells' div.py and setup.py; format: alsys_(time given by als_time())
def post_als(file_list):
    als_name = utils.auto_find(config, 'alsys')
    utils.write_add_all_to_xll(als_name, file_list)

# check if a cell's flag is 'dead'
def check_int_flag(cell):
    flag = utils.auto_flag(cell + '/status.txt')
    if flag == 'dead' or flag == 'infected':
        return gen_bll(cell)

def gen_bll(path):
    utils.unpack_org(path + '/appdata.zip') # unpack(restore) appdata remains
    xll = utils.get_xll(path + '/appdata/allow.txt') # allowlist, preserved
    for i in range(len(xll)):
        if xll[i][-3:] == '.py':
            xll[i] = xll[i][:-3]
    fl = os.listdir(path)
    bll = [] # blocklist init
    for i in fl:
        if not(i in xll) and not(i in ['appdata', 'appdata.zip']):
            bll.append(i)
    return bll

def write_bll(path):
    bll = check_int_flag(path)
    bll_name = utils.auto_find(config, 'bl')
    bll0 = utils.get_xll(bll_name)
    if bll:
        bll2 = []
        for i in bll:
            if not(i in bll0):
                bll2.append(i)
        utils.write_add_all_to_xll(bll_name, bll2)

def bll_check_match(path, lconfig = 'status.txt'):
    bll_name = utils.auto_find(config, 'bl')
    match = utils.xll_find_match(bll_name, path)
    if len(match):
        utils.set_flag(path + '/' + lconfig, 'infected')


def main():
    # self sanity check
    avail()
    # main code
    bll_name = utils.auto_find(config, 'bl')
    all_name = utils.auto_find(config, 'al')
    if not(bll_name in os.listdir()):
        bll = open(bll_name, 'w')
        bll.write('')
        utils.write_add_to_xll(all_name, bll_name)
        bll.close()
    cell_num = utils.get_cell_idx()
    cell_name = CELLNAMEPREFIX + str(cell_num)
    while True:
    # always active - immune cells(type 1 - innate immune cells / strict immune cells)
    # has global allowlist / blocklist
        bll1 = utils.get_xll(bll_name)
        tree = os.listdir('..')
        t2 = []
        for i in tree:
            if i[:6] == 'cell_t':
                t2.append('../' + i)
        for i in t2:
            write_bll(i)
        for i in t2:
            bll_check_match(i)

main()
