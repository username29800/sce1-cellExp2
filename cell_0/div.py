from venv import create

import utils, os
def main():
    flag = utils.auto_flag('status.txt')
    create_cell(flag)

def create_cell(flag):
    if flag == 'inactive':
        # mkdir within cwd
        cell_num = utils.get_cell_idx()
        while utils.is_cell_in_root(os.getcwd()):
            cell_num += 1
        os.mkdir('../cell_' + str(cell_num))

def copy_content(dst):
    pass