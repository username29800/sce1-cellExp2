import utils, os
flag = utils.auto_flag('status.txt')
if flag == 'inactive':
    # mkdir within cwd
    cell_num = os.getcwd().split('_')[1]
    cell_num = utils.get_cell_idx('.')
    files_root = os.listdir('..')
    while 'cell_' + str(cell_num) in files_root:
        cell_num += 1
    os.mkdir('../cell_' + str(cell_num))