import utils, sys, shutil, os
from main import CELLNAMEPREFIX

#origin packager
def pack(backup = True):
    file_list = ['utils.py', 'main.py', 'packager.py', 'keepalive.py', 'status.txt']
    try:
        utils.one_pack_64('origin', file_list, backup)
        #utils.one_pack_new('origin', 'origin', file_list)
        return 0
    except Exception as e:
        print(e)
        raise e

# pathogen sample packager (apoptosis, self-deletion-and-archiving)
def pack_pathogen(backup = True):
    pass

# appdata packager - allowlist matches packager
def pack_allowlist(backup = True):
    allow_file = utils.auto_find('status.txt', 'al')
    allow_list = utils.get_xll(allow_file)
    for i in ['appdata', '__pycache__']:
        while i in allow_list:
            del_idx = allow_list.index(i)
            allow_list = allow_list[:del_idx] + allow_list[del_idx + 1:]
    utils.one_pack_64('appdata', allow_list, backup)
    return 0

def pack_comm(file_list):
    backup_number = 0
    files_current = os.listdir()
    cell_name = CELLNAMEPREFIX + str(utils.get_cell_idx())
    while f't_{cell_name}_{backup_number}.zip' in files_current:
        backup_number += 1
    arc_name = f't_{cell_name}_{backup_number}'
    utils.one_pack_64(arc_name, file_list, False)
    shutil.copy(arc_name + '.zip', f'../post/{arc_name}.zip')

def main(backup = True):
    args = sys.argv[1]
    if args == 'org' or args == '': # normal
        pack(backup)
    elif args == 'ad': # appdata
        pack_allowlist(backup)
    elif args == 'ps': # pathogen sample
        pack_pathogen(backup)
    elif args == 'tr': # file transmission
        pack_comm(sys.argv[2:])

if len(sys.argv) > 2:
    if sys.argv[2] in ['1', 'True']:
        main()
    elif sys.argv[2] in ['0', 'False']:
        main(False)
    else:
        main()
elif len(sys.argv) > 1:
    main()