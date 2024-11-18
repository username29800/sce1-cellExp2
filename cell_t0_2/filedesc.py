import os
files = os.listdir()
files_current = []
for i in files:
  if i.split('.')[-1] in ['py','txt']:
    files_current.append(i)
wrt_file = open('filedesc.out','w')
for i in files_current:
  rd_file = open(i,'r')
  rd_ctnt = rd_file.readlines()
  wrt_file.writelines(['filename: ' + i + '\n'] + rd_ctnt + ['\n'])
wrt_file.close()
