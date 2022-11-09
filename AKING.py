import os,time
os.system('clear')
os.system('xdg-open https://facebook.com/groups/351076900316263/')
from platform import uname
arch=uname().machine.lower()
if 'aarch' in arch:
    print(' \n\033[1;37mCongratulations! Your Device Support This Tools');time.sleep(2)
    import dump
    dump.Main()
else:
    print(' \033[1;31mSorry system not support this tools');exit()
