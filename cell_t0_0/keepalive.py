import utils, shutil, os, subprocess, sys

#최초 실행시 flag 활성화
config_file = 'status.txt'
flag = utils.auto_flag(config_file)
if flag == 'inactive':
    utils.set_flag(config_file, 'active')

#allowlist 스캔 및 복구
al_filename = utils.auto_find(config_file, 'al')
check_missing = utils.xll_find_missing(al_filename, '.')
if len(check_missing):
    utils.set_flag(config_file, 'repair')
    utils.load_list_from_org(config_file, check_missing)
    utils.set_flag(config_file, 'active')

#allowlist 외부 파일 스캔 및 삭제
check_unknown = utils.xll_find_unknown(al_filename, '.')
del_failed = []
if len(check_unknown):
    utils.set_flag(config_file, 'repair')
    for del_file in check_unknown:
        try:
            os.remove(del_file)
        except:
            try:
                shutil.rmtree(del_file)
            except Exception as e:
                del_failed.append(del_file)
                raise e
    utils.set_flag(config_file, 'active')

#apoptosis
def apoptosis_init():
    #step 1. archive appdata and pathogen
    subprocess.call('python packager.py ad 0')
    subprocess.call('python packager.py ps 0')

    #step 2. make executables inactive
    utils.set_flag(config_file, 'dead')
    files_list = os.listdir()
    delpy_list = []
    for i in files_list:
        if i[-3:] == '.py':
            delpy_list.append(i)
    for i in delpy_list:
        os.rename(i, i[:-3])
        rm_file = open(i[:-3], 'w')
        rm_file.write('file content removed')
        rm_file.close()

args = ""
if len(sys.argv) - 1:
    args = sys.argv[1]
if args == "kill":
    apoptosis_init()
