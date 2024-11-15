import utils, os, shutil

flag = utils.auto_flag('status.txt')
if flag == 'inactive':
    # mkdir within rootdir
    cell_num = utils.get_cell_idx()
    while utils.is_cell_in_root(os.getcwd()):
        cell_num += 1
    os.mkdir('../cell_' + str(cell_num))
    # copy contents
    for source in os.listdir('.'):
        shutil.copy2(source, f'../cell_{cell_num}/{source}')
