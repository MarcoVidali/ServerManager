# ServerManager
ServerManager is a program that allows you to control your server remotely and easily using mostly SSH.

## Installation
You need to have installed Python 3. Then, install the requirements running:
```bash
# Windows
pip install -r requirements.txt

# Unix
sudo pip3 install -r requirements.txt
```

You also need to install these packages to get the program working:
```bash
# Debian based distros
sudo apt install ssh

# RedHat based distros
sudo dnf install ssh

# Arch based distros
sudo pacman -S ssh
```

## Running
To run, execute:
```bash
# Windows
python app.py

# Unix
python3 app.py
```