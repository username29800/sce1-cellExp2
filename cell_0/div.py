import utils, os, shutil

flag = utils.auto_flag('status.txt')
if flag == 'inactive':
    # mkdir within rootdir
    cell_num = utils.get_cell_idx()
    cell_name = 'cell_' + str(cell_num)
    while utils.is_cell_in_root(cell_name):
        cell_num += 1
        cell_name = cell_name[:-1] + str(cell_num)
    os.mkdir('../cell_' + str(cell_num))
    # copy contents
    for source in os.listdir():
        if source != '__pycache__':
            shutil.copy2(source, f'../cell_{cell_num}/{source}')