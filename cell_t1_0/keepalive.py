import utils, shutil, os, subprocess, sys
def act_flag():
    #최초 실행시 flag 활성화
    config_file = 'status.txt'
    flag = utils.auto_flag(config_file)
    if flag == 'inactive':
        utils.set_flag(config_file, 'active')

def repair_missing():
    config_file = 'status.txt'
    #allowlist 스캔 및 복구
    al_filename = utils.auto_find(config_file, 'al')
    check_missing = utils.xll_find_missing(al_filename, '.')
    if len(check_missing):
        utils.set_flag(config_file, 'repair')
        try:
            utils.load_list_from_org(config_file, check_missing)
        except:
            apoptosis_init()
        utils.set_flag(config_file, 'active')

def repair_unknown():
    config_file = 'status.txt'
    al_filename = utils.auto_find(config_file, 'al')
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
                    if not(del_file in del_failed):
                        del_failed.append(del_file)
                    print(e)
        utils.set_flag(config_file, 'active')
    if len(del_failed) > 1:
        apoptosis_init()

#apoptosis
def apoptosis_init():
    config_file = 'status.txt'
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
if len(sys.argv) == 2:
    args = sys.argv[1]
if args == "kill":
    apoptosis_init()

def main():
    act_flag()
    repair_missing()
    repair_unknown()

main()