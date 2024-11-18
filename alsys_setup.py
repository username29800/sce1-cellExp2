import os
alsys = open('alsys.txt', 'w')
files_now = os.listdir()
for i in range(len(files_now)):
    files_now[i] += '\n'
alsys.writelines(files_now)
alsys.close()