from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,platform,math,shutil,random,uuid,string,hashlib,json,sys

logo=("""\033[1;32m
             ##   ##     ##   ########  
             ##    ##   ##    ##     ## 
             ##     ## ##     ##     ## 
             ##      ###      ########  
       ##    ##     ## ##     ##     ## 
       ##    ##    ##   ##    ##     ## 
        ######    ##     ##   ########
------------------------------------------------
\033[1;37m [+] Author       :       Awais tahir
\033[1;37m [+] Github       :       https://github.com/JUTTBRAND
\033[1;37m [+] Version      :       7.4 [mix new]
\033[1;37m [+] Status       :       Premium
\033[1;32m------------------------------------------------""")
def clear():
        os.system(f'clear')
        print(logo)
        
def menu():
        
                        clear()
                        print(' [1] File cloning new \n [2] file cloning mix ')
                        xd=input(' Choose : ')
                        if xd in ['1','01']:
                                import AWS   
                        elif xd in ['2','02']:
                                import aws1 
menu()                                                            
