import utils, os, sys
config_file = 'status.txt'
# 1. unpack origin into cwd
if len(sys.argv) > 1 and sys.argv[1] == 'init':
    utils.load_from_org(config_file)
# 2. generate allowlist
allow_list = open('allow.txt', 'w')
files_current = os.listdir()
for i in range(len(files_current)):
    files_current[i] += '\n'
allow_list.writelines(files_current)
allow_list.close()
# 3. fetch blocklist - needed