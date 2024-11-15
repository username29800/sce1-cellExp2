import utils, sys
#origin packager
def pack():
    file_list = ['utils.py', 'main.py', 'packager.py', 'keepalive.py', 'status.txt']
    try:
        utils.one_pack_64('origin', file_list)
        #utils.one_pack_new('origin', 'origin', file_list)
        return 0
    except Exception as e:
        print(e)
        raise e

def pack_pathogen():
    pass

def pack_allowlist():
    allow_file = utils.auto_find('status.txt', 'al')
    allow_list = utils.get_xll(allow_file)
    for i in ['appdata', '__pycache__']:
        while i in allow_list:
            del_idx = allow_list.index(i)
            allow_list = allow_list[:del_idx] + allow_list[del_idx + 1:]
    utils.one_pack_64('appdata', allow_list)
    return 0

def main():
    args = sys.argv[1]
    if args == 'org' or args == '': # normal
        pack()
    elif args == 'ad': # appdata
        pack_allowlist()
    elif args == 'ps': # pathogen sample
        pack_pathogen()

main()