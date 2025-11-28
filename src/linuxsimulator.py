import getpass
import platform
import time
import random

users = {
    'senya': {
        'password': 'senya777',
        'is_admin': False
    },
    'nastya': {
        'password': 'animegirl',
        'is_admin': False
    },
    'mutniymrak': {
        'password': 'vor666',
        'is_admin': False
    },
    'krutoipacan': {
        'password': 'krutoi1234',
        'is_admin': False
    },
    'yarik': {
        'password': 'pelmen',
        'is_admin': False
    },
    'hitori': {
        'password': 'guitarhero',
        'is_admin': False
    },
    'masha': {
        'password': 'hljkfdsfdshjk',
        'is_admin': False
    },
    'Andrey': {
        'password': '5673845',
        'is_admin': False
    },
    'root':{
        'password': '1234',
        'is_admin': True
    },
    'linus': {
        'password': 'creatorofgdz',
        'is_admin': True
    }    
}

hardware_name = 'archlinux'

def systemd_boot():
    stages = [
        'Welcome to Arch Linux!\n'
        '[ OK ] Started Journal Service.\n'
        '[ OK ] Creating slice system-getty.slice.\n'
        '[ OK ] Reached target swap.\n'
        '[ OK ] Reached target Local File Systems.\n'
        '[ OK ] Mounted /dev/sda2.\n'
        '[ OK ] Mounted /dev/sda3.\n'
        'Starting Login Service.\n'
        'Starting Getty on TTI.\n'
        'Starting Command scheulder.\n'
        '[ OK ] Started command scheulder.\n'
        '[ OK ] Started Network Manager.\n'
        '[ OK ] Started command scheulder.\n'
        '[ OK ] Swaga prisutstvuet.\n'
    ]
    
    for stage in stages:
        print(stage)
        time.sleep(random.uniform(0.3, 0.8))


def terminal():    
    while True:
        if users[userlogin]['is_admin'] == True:
            cmd = input(f"{userlogin}@{hardware_name}:~# ")
        else:
            cmd = input(f"{userlogin}@{hardware_name}:~$ ")  

        if cmd == 'pwd':
            print(f"home/{userlogin}")
        elif cmd == 'shutdown':
            exit()
        elif cmd == 'fastfetch':
            print('OS: Arch Linux\n'
                    'Kernel: 6.6.6\n'
                    f'CPU:{platform.processor()} \n'
                    'Memory: 4589 MB / 15985\n'
                    'GPU: Nvidia RTX 3060\n'
                    'Solution: 1920x1080\n'
                    'bash 5.2.6\n')
        elif cmd == 'ls':
            print('Documents\n'
                    'Downloads\n'
                    'Images\n'
                    'Music\n'
                    'Desktop\n'
                    'Video\n')
        elif cmd == 'whoami':
            print(f'{userlogin}')
        elif cmd == 'uname -a':
            print('linux 6.6.6')
        elif cmd == 'lol':
            print('НОВЫЙ ПРОЕКТ RED HAT SYSTEMD — ЭТО ВИРУСНЫЙ ЭКСПЛОИТ GCC!!!\n'
                '🚨🔥 КИБЕРОРУЖИЕ RED HAT УГРОЗА НАНОРОБОТ ВСТРОЕН В GCC МОДУЛЬ ДЛЯ RED HAT LINUX!!!\n'
                'КВАНТОВО-ФИЗИКО-МАТЕМАТИЧЕСКИЙ УРОВЕНЬ SYSTEMD!!! 🌌🔮\n'
                'СССР НЛО RED HAT MICROSOFT ИНОПЛАНЕТЯНЕ ЗОНА 51 GCC БЕНДЕР LINUX АНТИМАТЕРИЯ ЦРУ СПЕЦСЛУЖБЫ!!!\n'
                'СЛЕЖКА ЗА ЛЮДЬМИ ЧЕРЕЗ OPEN SOURCE!!! 🕵️‍♂️💀\n'
                'ЭТО ПРОЕКТ ЭЛЕМЕНТАРНЫХ МАСШТАБОВ США РАЗВОДКА SYSTEMD!!!\n'
                'RED HAT ЗАХВАТ ЗЕМЛИ GCC СУПЕРСЕКРЕТНАЯ РАЗРАБОТКА!!!\n'
                'SYSTEMD ЕВРЕЙСКАЯ ЦИВИЛИЗАЦИЯ COMMODORE 64!!!\n')
        else:
            print(f"bash: command not found: {cmd}")

systemd_boot()

while True:
    userlogin = input("Login: ")
    userpassword = getpass.getpass("Password: ")
    if userlogin in users:
        if users[userlogin]['password'] == userpassword:
            terminal()
        else:
            print("Inncorect password")
    else:
        print("Inncorect Login")
