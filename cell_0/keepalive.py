import utils, shutil, os, subprocess

#최초 실행시 flag 활성화
flag = utils.auto_flag('status.txt')
if flag == 'inactive':
    utils.set_flag('status.txt', 'active')

#allowlist 스캔 및 복구
al_filename = utils.auto_find('status.txt', 'al')
check_missing = utils.xll_find_missing(al_filename, '.')
if len(check_missing):
    utils.set_flag('status.txt', 'repair')
    utils.load_from_org('status.txt')
    utils.set_flag('status.txt', 'active')

#allowlist 외부 파일 스캔 및 삭제
check_unknown = utils.xll_find_unknown(al_filename, '..')
del_failed = []
if len(check_unknown):
    utils.set_flag('status.txt', 'repair')
    for del_file in check_unknown:
        try:
            os.remove(del_file)
        except:
            try:
                shutil.rmtree(del_file)
            except:
                del_failed.append(del_file)
    utils.set_flag('status.txt', 'active')

#apoptosis
def apoptosis_init():
    #step 1. archive appdata and pathogen
    subprocess.call('python packager.py ad 0')
    subprocess.call('python packager.py ps 0')

    #step 2. make executables inactive
    files_list = os.listdir()
    delpy_list = []
    for i in files_list:
        if i[-3:] == '.py':
            delpy_list.append(i)
    for i in delpy_list:
        os.rename(i, i[:-3])
