import os

if os.name == "nt":
    pass
else:
    os.system("apt-get install curl -y")
    os.system("curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -")
    os.system("apt install nodejs")
    os.system("npm install randomstring")
    os.system("npm install cloudscraper")
    os.system("npm install superagent-proxy --save-dev")
    os.system("npm install crypto-random-string@3.3.1")
    os.system("npm install request --save")