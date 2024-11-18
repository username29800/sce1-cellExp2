# this script will serve as a server, transmitting str when requested by http
# 1. pre-boot POST routine
# core modules loader
import utils, sys, os, subprocess
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

# return output
def outpost():
    out_name = utils.auto_find(config, 'out')
    cell_num = utils.get_cell_idx()
    cell_name = CELLNAMEPREFIX + str(cell_num)
    subprocess.call(['python', 'packager.py','td', out_name + cell_name + '.txt'])

def main():
    # self sanity check
    avail()
    # main code
    cell_num = utils.get_cell_idx()
    cell_name = CELLNAMEPREFIX + str(cell_num)
    while True:
    # check if request is present
    # requests exist in ../post
        if utils.check_post(cell_name):
            wrtout()
            outpost()

main()
