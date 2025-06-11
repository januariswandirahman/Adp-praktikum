
import os
import time
from termcolor import colored, cprint
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def logo_adidas(color='white', warna_latar='on_black'):
    logo = [

        "                                  ██                                       ",
        "                                ██████                                     ",
        "                              ██████████                                   ",
        "                            ██████████████                                 ",
        "                              ██████████████                               ",
        "                        ██      ██████████████                             ",
        "                       ██████      ██████████████                          ",
        "                    ██████████      ██████████████                         ",
        "                  ██████████████      ██████████████                       ",
        "                    ██████████████      ██████████████                     ",
        "              ██      ██████████████      ██████████████                   ",
        "            ██████      ██████████████      ██████████████                 ",
        "          ██████████      ██████████████      ██████████████               ",
        "        ██████████████      ██████████████      ██████████████             ",
        "                       █               █                █████              ",
        "                       █               █                █                  ",
        "          ███       ████      █     ████      ███       █████              ",  
        "         █   █     █   █      █    █   █     █   █          █              ",
        "          █████     ████      █     ████      █████     █████              "    
    ]
    for line in logo:
        for char in line:
            if char == '█':
                cprint(' ', 'white', 'on_white', end='')
            else:
                cprint(' ', color, warna_latar, end='')
        print()
def main():
    clear_screen()
    print("\n\n")
    print("Membuat logo Adidas...")
    time.sleep(1)
    warna_latar = ['on_red', 'on_blue', 'on_green', 'on_magenta', 'on_cyan'] 
    for i, bg in enumerate(warna_latar):
        clear_screen()
        print(f"\n\nVersi {i+1} - Background {bg[3:]}")
        logo_adidas('white', bg)
        time.sleep(1)
    clear_screen()
    print("\n\nLogo Final Adidas")
    logo_adidas('white', 'on_blue')  
    print("\n")
    cprint(" " * 20 + "TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI" + " " * 20, 'white', 'on_blue')
    print("\n")
if __name__ == "__main__":
    main()
#############################################################################################################
import os
from termcolor import colored, cprint

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo_pertamina():
    
    logo = [
        "                            " + colored("  █████████████", 'red'),
        "                              " + colored("  █████████████", 'red'),
        "                                " + colored("  █████████████", 'red'),
        "                                   " + colored(" █████████████", 'red'),
        "                                   " + colored("   █████████████ ", 'red'),
        "                                                                                  ",
        "                                                                                       ",
        "                  "+ colored("█████████████",'blue')+colored("███████", 'black')   +colored("█████████████", 'green'),
        "                "+ colored("█████████████",'blue')+colored("███████", 'black')   +colored("█████████████", 'green'),
        "             "+ colored(" █████████████",'blue')+colored("███████", 'black')   +colored("█████████████ ", 'green'),
        "           "+ colored(" █████████████",'blue')+colored("███████", 'black')   +colored("█████████████ ", 'green'),
        "        "+ colored("  █████████████",'blue')+colored("███████", 'black')   +colored("█████████████   ", 'green'),
        "       "+ colored(" █████████████ ", 'blue'),
        "     "+ colored(" █████████████ ", 'blue'),
        "    "+ colored("█████████████ ", 'blue'),
        "  "+ colored("█████████████ ", 'blue'),
        " "+colored("█████████████ ", 'blue'),
        "                                                                                  ",
        " █████    █████  ████    ███████      ██     ██    ██   █    ██    █       ██     ",
        " █    █   █      █   █      █        █  █    █ █  █ █   █    █ █   █      █  █    ",
        " █████    ████   ████       █       ██████   █  ██  █   █    █  █  █     ██████   ",
        " █        █      █   █      █       █    █   █      █   █    █   █ █     █    █   ",
        " █        ████   █    █     █       █    █   █      █   █    █    ██     █    █   ",
    ]
    
    for line in logo:
        print(line)
def main():
    clear_screen()
    print("\n\n")
    cprint(" " * 30 + "LOGO RESMI PERTAMINA" + " " * 30, 'white', 'on_blue')
    print("\n")
    logo_pertamina()
if __name__ == "__main__":
    main()