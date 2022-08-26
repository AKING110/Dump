import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

print('<------------------------------------>')
bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{green}[•] Join Over Facebook Group For Any Help{white}')
    os.system('xdg-open https://facebook.com/groups/351076900316263/')
    import Dump
else:
    print(f'{red}[×] Sorry Device Not Support{white}')
