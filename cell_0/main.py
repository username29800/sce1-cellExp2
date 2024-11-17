# this script will serve as a server, transmitting str when requested by http
# 1. pre-boot POST routine
# core modules loader
import utils, sys, os, subprocess
config = 'status.txt' # set config file
CELLNAMEPREFIX = utils.auto_find(config, 'defaultname')

# self integrity check
os.system('python keepalive.py')

# check availability
def avail():
    avail = utils.auto_flag(config)
    if avail != "active":
        # put error logging code here
        exit()
    # backup origin
    subprocess.call('packager.py org 0')

# write output
def wrtout():
    out_name = utils.auto_find(config, 'out')
    cell_num = utils.get_cell_idx()
    cell_name = CELLNAMEPREFIX + cell_num
    out_file = open('','')

# return output
def outpost():
    out_name = utils.auto_find(config, 'out')
    cell_num = utils.get_cell_idx()
    cell_name = CELLNAMEPREFIX + cell_num
    subprocess.call('packager.py tr' + out_name + cell_name)