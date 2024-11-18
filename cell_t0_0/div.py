import utils, os, shutil, sys
CELLNAMEPREFIX = utils.auto_find('status.txt', 'defaultname')

args = ''
if len(sys.argv):
    args = sys.argv[1]

flag = utils.auto_flag('status.txt')
if (flag == 'inactive') or (args == '-f'): # add force option
    # mkdir within rootdir
    cell_num = utils.get_cell_idx()
    cell_name = CELLNAMEPREFIX + str(cell_num)
    while utils.is_cell_in_root(cell_name):
        cell_num += 1
        cell_name = CELLNAMEPREFIX + str(cell_num)
    os.mkdir('../' + cell_name)
    # copy contents
    for source in os.listdir():
        if source != '__pycache__':
            shutil.copy2(source, f'../{CELLNAMEPREFIX}{cell_num}/{source}')
