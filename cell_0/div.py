import utils, os, shutil, sys
CELLNAMEPREFIX = utils.auto_find('status.txt', 'defaultname')

args = ''
if len(sys.argv):
    args = sys.argv[1]

# post updated alsys (system-wide allowlist) - also required in normal cells' div.py and setup.py; format: alsys_(time given by als_time())
def post_als(file_list):
    als_name = utils.auto_find('status.txt', 'alsys')
    utils.write_add_all_to_xll(als_name, file_list)

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
    post_als([cell_name])
