import zipfile, shutil, os, sys


# section 1: basics


def equal_str(list_a):
  for i in range(len(list_a)):
    list_a[i] = list_a[i].rstrip('\n')
  return list_a

def substr(str_origin, str_sub):
  for i in range(len(str_sub)):
    if str_sub[i] != str_origin[i]:
      str_origin = str_origin[i:]
      break
    if i == len(str_sub) - 1:
      str_origin = str_origin[i + 1:]
  return str_origin


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


def set_find(flag_file, find_str, set_str):
  flaglines = list_flag(flag_file)
  for i in range(len(flaglines)):
    if flaglines[i].split('=')[0].rstrip(' ') == find_str:
      preflag = flaglines[:i]
      afflag = flaglines[i + 1:]
  flaglines = preflag + [f'{find_str} = {set_str}\n'] + afflag
  flags = open(flag_file, 'w')
  flags.writelines(flaglines)
  return 0


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
def get_xll(al_file):  # get AllowList
  ok_file = open(al_file, 'r')
  ok_list = ok_file.readlines()
  ok_list = equal_str(ok_list)
  ok_file.close()
  return ok_list


def write_add_to_xll(al_file, str_write):  # for file i/o
  ok_file = open(al_file, 'a')
  ok_file.write(f'{str_write}\n')
  ok_file.close()
  return 0


def write_add_all_to_xll(al_file, str_write_list):
  for i in str_write_list:
    write_add_to_xll(al_file, i)
  return 0


def list_add_to_xll(al_file, str_write):  # for internal use. 코드 내에서 list initializer로 사용
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
      ok_update = ok_list[:i] + ok_list[i + 1:]
  return ok_update


def list_del_all_from_xll(al_file, str_del_list):
  ok_list = get_xll(al_file)
  ok_update = []
  for str_del in str_del_list:
    for i in range(len(ok_list)):
      if ok_list[i] == str_del:
        ok_update = ok_list[:i] + ok_list[i + 1:]
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
    if not (target in files_current):
      list_missing.append(target)
  return list_missing


def xll_find_unknown(al_file, scan_dir):
  xll = get_xll(al_file)
  xll_list = equal_str(xll)
  files_current = os.listdir(scan_dir)
  list_missing = []
  for target in files_current:
    if not (target in xll_list):
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


def unpack_org(org_file, ext = '.zip'):
  org_arc = zipfile.ZipFile(org_file, 'r')
  org_arc.extractall(org_file[:-len(ext)])
  org_arc.close()
  return 0


def pack_org(org_dir):
  shutil.make_archive('origin', 'zip', os.getcwd(), org_dir)
  return 0


def pre_pack_org(org_dir, file_list):
  for i in file_list:
    shutil.copy2(i, f'{org_dir}/{i}')
  return 0


def one_pack_org(org_dir, file_list):
  files_current = os.listdir()
  if f'origin.zip' in files_current:
    shutil.move(f'origin.zip', f'origin_backup.zip')
  os.mkdir(org_dir)
  pre_pack_org(org_dir, file_list)
  pack_org(org_dir)
  shutil.rmtree(org_dir)
  return 0


def one_pack_new(org_dir, dst_arc, file_list, backup = True, remove_dir = True):
  files_current = os.listdir()
  backup_number = 0
  file_check = [f'{org_dir}_backup_{backup_number}', f'{dst_arc}_backup_{backup_number}.zip']
  file_type = ['', '.zip']
  for i in file_check:
    for j in file_type:
      while f'{org_dir}_backup_{backup_number}{j}' in files_current:
        backup_number += 1
  if (org_dir in files_current) and backup:
    shutil.move(org_dir, f'{org_dir}_backup_{backup_number}')
  if (f'{dst_arc}.zip' in files_current) and backup:
    shutil.move(f'{dst_arc}.zip', f'{dst_arc}_backup_{backup_number}.zip')
  os.mkdir(org_dir)
  pre_pack_org(org_dir, file_list)
  shutil.make_archive(dst_arc, 'zip', org_dir, os.getcwd())
  if remove_dir:
    shutil.rmtree(org_dir)
  return 0


def one_pack_64(dst_arc, file_list, backup = True):
  backup_number = 0
  files_current = os.listdir()
  while f'{dst_arc}_backup_{backup_number}.zip' in files_current:
    backup_number += 1
  if (f'{dst_arc}.zip' in files_current) and backup:
    shutil.move(f'{dst_arc}.zip', f'{dst_arc}_backup_{backup_number}.zip')
  arch = zipfile.ZipFile(f'{dst_arc}.zip', 'w')
  for wfile in file_list:
    arch.write(wfile)
  arch.close()


def load_from_org(config_file):
  origin_filename = auto_find(config_file, 'org')
  unpack_org(origin_filename)
  for i in os.listdir(origin_filename[:-4]):
    shutil.move(f'{origin_filename[:-4]}/{i}', i)
  shutil.rmtree(origin_filename[:-4])
  return 0

def load_list_from_org(config_file, file_list):
  origin_filename = auto_find(config_file, 'org')
  unpack_org(origin_filename)
  for i in file_list:
    shutil.move(f'{origin_filename[:-4]}/{i}', i)
  shutil.rmtree(origin_filename[:-4])
  return 0

def load_from_find(find):
  unpack_org(find)
  for i in os.listdir(find[:-4]):
    shutil.move(f'{find[:-4]}/{i}', i)
  shutil.rmtree(find[:-4])
  return 0


# section 4: cell
# 4. cell

CELLNAMEPREFIX = auto_find('status.txt', 'defaultname')


def get_cell_idx(path=None):
  entry_dir = os.getcwd()
  if path:
    os.chdir(path)
  cell = os.getcwd()
  cell = cell.split('/')[-1]
  cell = cell.split('\\')[-1]
  cell_num = substr(cell, CELLNAMEPREFIX)
  cell_num = int(cell_num)
  os.chdir(entry_dir)
  return cell_num


def is_cell_in_root(cell):
  if cell in os.listdir('..'):
    return True
  else:
    return False


def check_post(cell_name=CELLNAMEPREFIX + str(get_cell_idx())):
  post_dir = os.listdir('../post')
  if f'req_{cell_name}' in post_dir:
    return True
  else:
    return False
