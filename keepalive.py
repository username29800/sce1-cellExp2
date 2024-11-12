import utils


#최초 실행시 flag 활성화
flag = utils.auto_flag('status.txt')
if flag == 'inactive':
  utils.set_flag('status.txt', 'active')
  
  
#whitelist 관리
wl_filename = utils.auto_find('status.txt', 'al')
wl = utils.get_xll(wl_filename)