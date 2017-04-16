# Searches eBooks for free download

## Install Python 3.6
```
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt update
sudo apt install python3.6 python3.6-venv python3.6-doc python3.6-dev
```

## Getting the project and creating virtual environment
```
git clone https://github.com/carlosaospinac/books.git
cd books
python3.6 -m venv venv
source venv/bin/activate
pip install -r requirements.pip
```

## Running project
```
source venv/bin/activate # If the environment is not enabled
python python app.py
```

## It will get something like ...
```
                 ▄▄▄▄▄
        ▀▀▀██████▄▄▄       _______________
      ▄▄▄▄▄  █████████▄  /                 \
     ▀▀▀▀█████▌ ▀▐▄ ▀▐█ |   Gotta go fast!  |
   ▀▀█████▄▄ ▀██████▄██ | _________________/
   ▀▄▄▄▄▄  ▀▀█▄▀█════█▀ |/
        ▀▀▀▄  ▀▀███ ▀       ▄▄
     ▄███▀▀██▄████████▄ ▄▀▀▀▀▀▀█▌
   ██▀▄▄▄██▀▄███▀ ▀▀████      ▄██
▄▀▀▀▄██▄▀▀▌████▒▒▒▒▒▒███     ▌▄▄▀
▌    ▐▀████▐███▒▒▒▒▒▐██▌
▀▄▄▄▄▀   ▀▀████▒▒▒▒▄██▀
          ▀▀█████████▀
        ▄▄██▀██████▀█
      ▄██▀     ▀▀▀  █
     ▄█             ▐▌
 ▄▄▄▄█▌              ▀█▄▄▄▄▀▀▄
▌     ▐                ▀▀▄▄▄▀
 ▀▀▄▄▀

2017-03-24 11:11:05,146: INFO: Goin' Fast @ http://0.0.0.0:8000
```



