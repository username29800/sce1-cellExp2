import utils, shutil, os
import util2


#최초 실행시 flag 활성화
flag = utils.auto_flag('status.txt')
if flag == 'inactive':
    utils.set_flag('status.txt', 'active')


#allowlist 스캔 및 복구
al_filename = utils.auto_find('status.txt', 'al')
check_missing = utils.xll_find_missing(al_filename, '..')
if check_missing != []:
    utils.set_flag('status.txt', 'repair')
    org_filename = utils.auto_find('status.txt', 'org')
    org_prep = utils.unpack_org(org_filename)
    for move_file in check_missing:
        shutil.move(f'{org_filename[:-4]}/{move_file}', move_file)
    shutil.rmtree(org_filename[:-4])
    utils.set_flag('status.txt', 'active')


#allowlist 외부 파일 스캔 및 삭제
check_unknown = utils.xll_find_unknown(al_filename, '..')
del_failed = []
if check_unknown != []:
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
