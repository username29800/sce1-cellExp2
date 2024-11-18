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

def main():
    # self sanity check
    avail()
    # main code
    cell_num = utils.get_cell_idx()
    cell_name = CELLNAMEPREFIX + str(cell_num)
    while True:
    # always active - immune cells(type 1 - innate immune cells / strict immune cells)
    # has global allowlist / blocklist
        # refresh_als()
        unknown = check_system()
        del_unknown(unknown)

main()
