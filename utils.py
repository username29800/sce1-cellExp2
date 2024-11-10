# 0. global variables
#flag_file = ''
#flag_line = 0
#flag=''

# section 1: basics
# 1. flags

def get_flag(flag_file, flag_line):
    flag = list_flag(flag_file)[flag_line - 1]
    return flag

def set_flag(flag_file, flag):
    flaglines = list_flag(flag_file)
    #split file by flag line
    for i in range(len(flaglines)):
        if flaglines[i][:7] == 'flag = ':
            preflag = flaglines[:i]
            afflag = flaglines[i:]
            flaglines = preflag + [f'flag = {flag}\n'] + afflag
            flags = open(flag_file, 'w')
            flags.writelines(flaglines)
    return 0

def list_flag(flag_file):
    flags = open(flag_file, 'r')
    flags_list = flags.readlines()
    flags.close()
    return flags_list

# section 2: lists
# 2. allowlist
def get_all(al_file): # get AllowList
    ok_file = open(al_file, 'r')
    ok_list = ok_file.readlines()
    ok_file.close()
    return ok_list

def write_add_to_all(al_file, str_write): # for file i/o
    ok_file = open(al_file, 'a')
    ok_file.write(f'{str_write}\n')
    ok_file.close()
    return 0

def list_add_to_all(al_file, str_write): # for internal use. 코드 내에서 list initializer로 사용
    ok_list = get_all(al_file)
    ok_list.append(f'{str_write}\n')
    return ok_list

def del_from_all(al_file, str_del):
    ok_list = get_all(al_file)
    ok_update = []
    for i in range(len(al_file)):
        if ok_list[i] == str_del:
            ok_update = ok_list[:i] + ok_list[i:]
    return ok_update

def write_del_from_all(al_file, str_del):
    ok_update = del_from_all(al_file, str_del)
    ok_write = open(al_file, 'w')
    ok_write.writelines(ok_update)
    return 0
