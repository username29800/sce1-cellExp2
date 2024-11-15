import utils, sys
#origin packager
def pack():
    file_list = ['utils.py', 'main.py', 'packager.py', 'keepalive.py', 'status.txt']
    try:
        utils.one_pack_org('pre_origin', file_list)
        return 0
    except:
        return 1

def pack_pathogen():
    pass

def pack_allowlist():
    allow_file = utils.auto_find('status.txt', 'al')
    allow_list = utils.get_xll(allow_file)
    utils.one_pack_new('appdata', 'appdata', allow_list)
    return 0

def main():
    args = sys.argv[1]
    if args == 'org' or args == '': # normal
        pack()
    elif args == 'ad': # appdata
        pack_allowlist()
    elif args == 'ps': # pathogen sample
        pack_pathogen()