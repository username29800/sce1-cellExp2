import zipfile, shutil, os, sys

# section 1: basics

def equal_str(list_a):
  for i in range(len(list_a)):
    list_a[i] = list_a[i].rstrip('\n')
  return list_a

# 1. flags

def get_flag(flag_file, flag_line):
  flag = list_flag(flag_file)[flag_line - 1]
  return flag

def format_flag(flag_file, flag_line):
  flag = get_flag(flag_file, flag_line)
  flag_f = ''
  if flag[:7] == "flag = ":
    flag_f = flag[7:]
    flag_f = flag_f.rstrip('\n')
    return flag_f
  else:
    return ''

def auto_flag(flag_file):
  flaglines = list_flag(flag_file)
  flag_line = 0
  for i in range(len(flaglines)):
    if flaglines[i][:7] == 'flag = ':
      flag_line = i + 1
      break
  flag = format_flag(flag_file, flag_line)
  return flag

def format_auto(flag_file, flag_line, find_str):
  flag = get_flag(flag_file, flag_line)
  flag_f = ''
  if flag.split('=')[0].rstrip(' ') == find_str:
    flag_f = flag.split('=')[1].lstrip(' ')
    flag_f = flag_f.rstrip('\n')
    return flag_f
  else:
    return ''
def auto_find(flag_file, find_str):
  flaglines = list_flag(flag_file)
  flag_line = 0
  for i in range(len(flaglines)):
    if flaglines[i].split('=')[0].rstrip(' ') == find_str:
      flag_line = i + 1
      break
  flag = format_auto(flag_file, flag_line, find_str)
  return flag

def set_flag(flag_file, flag):
  flaglines = list_flag(flag_file)
  #split file by flag line
  for i in range(len(flaglines)):
    if flaglines[i][:7] == 'flag = ':
      preflag = flaglines[:i]
      afflag = flaglines[i + 1:]
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
def get_xll(al_file): # get AllowList
  ok_file = open(al_file, 'r')
  ok_list = ok_file.readlines()
  ok_file.close()
  return ok_list

def write_add_to_xll(al_file, str_write): # for file i/o
  ok_file = open(al_file, 'a')
  ok_file.write(f'{str_write}\n')
  ok_file.close()
  return 0

def write_add_all_to_xll(al_file, str_write_list):
  for i in str_write_list:
    write_add_to_xll(al_file, i)
  return 0

def list_add_to_xll(al_file, str_write): # for internal use. 코드 내에서 list initializer로 사용
  ok_list = get_xll(al_file)
  ok_list.append(f'{str_write}\n')
  return ok_list

def list_add_all_to_xll(al_file, str_write_list):
  ok_list = get_xll(al_file)
  for str_write in str_write_list:
    ok_list.append(f'{str_write}\n')
  return ok_list

def list_del_from_xll(al_file, str_del):
  ok_list = get_xll(al_file)
  ok_update = []
  for i in range(len(ok_list)):
    if ok_list[i] == str_del:
      ok_update = ok_list[:i] + ok_list[i+1:]
  return ok_update

def list_del_all_from_xll(al_file, str_del_list):
  ok_list = get_xll(al_file)
  ok_update = []
  for str_del in str_del_list:
    for i in range(len(ok_list)):
      if ok_list[i] == str_del:
        ok_update = ok_list[:i] + ok_list[i+1:]
  return ok_update

def write_del_from_xll(al_file, str_del):
  ok_update = list_del_from_xll(al_file, str_del)
  ok_write = open(al_file, 'w')
  ok_write.writelines(ok_update)
  return 0

def write_del_all_from_xll(al_file, str_del_list):
  list_del = list_del_all_from_xll(al_file, str_del_list)
  ok_write = open(al_file, 'w')
  ok_write.writelines(list_del)
  return 0

def xll_find_match(al_file, scan_dir):
  xll = get_xll(al_file)
  xll_list = equal_str(xll)
  files_current = os.listdir(scan_dir)
  list_match = []
  for target in xll_list:
    if target in files_current:
      list_match.append(target)
  return list_match

def xll_find_missing(al_file, scan_dir):
  xll = get_xll(al_file)
  xll_list = equal_str(xll)
  files_current = os.listdir(scan_dir)
  list_missing = []
  for target in xll_list:
    if not(target in files_current):
      list_missing.append(target)
  return list_missing

def xll_find_unknown(al_file, scan_dir):
  xll = get_xll(al_file)
  xll_list = equal_str(xll)
  files_current = os.listdir(scan_dir)
  list_missing = []
  for target in files_current:
    if not(target in xll_list):
      list_missing.append(target)
  return list_missing

def xll_find_all(al_file, scan_dir):
  xll = get_xll(al_file)
  xll_list = equal_str(xll)
  files_current = os.listdir(scan_dir)
  list_match = []
  list_missing = []
  for target in xll_list:
    if target in files_current:
      list_match.append(target)
    else:
      list_missing.append(target)
  return [list_match, list_missing]

# section 3: origin
# 3. origin

def unpack_org(org_file):
  shutil.unpack_archive(org_file, os.getcwd(), 'zip')
  return 0

def pack_org(org_dir):
  shutil.make_archive('origin', 'zip', os.getcwd(), org_dir)
  return 0

def pre_pack_org(org_dir, file_list):
  for i in file_list:
    shutil.move(i, f'{org_dir}/{i}')
  return 0

def one_pack_org(org_dir, file_list):
  files_current = os.listdir()
  if f'{org_dir}.zip' in files_current:
    shutil.move(f'{org_dir}.zip', f'{org_dir}_backup')
  os.mkdir(org_dir)
  pre_pack_org(org_dir, file_list)
  pack_org(org_dir)
  shutil.rmtree(org_dir)
  return 0

def load_from_org(config_file):
  origin_filename = auto_find(config_file, 'org')
  unpack_org(origin_filename)
  for i in os.listdir(origin_filename[:-4]):
    shutil.move(f'{origin_filename[:-4]}/{i}', i)
  shutil.rmtree(origin_filename[:-4])
  return 0
