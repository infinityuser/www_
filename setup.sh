# general variables
project='www'
entry='source'
user='debian'
configs='configs'

# general preparation
sudo apt-get update
sudo apt-get install ufw nmap wget tmux vim nginx htop build-essential zlib1g-dev libncurses5-dev libgdbm-dev libsqlite3-dev libnss3-dev libssl-dev libreadline-dev libffi-dev curl libbz2-dev
# --------------------------

# making up python environment
mkdir /home/$user/temp
cd /home/$user/temp

wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tar.xz
tar -xvf Python-3.8.3.tar.xz
cd Python-3.8.3
./configure --enable-optimizations --prefix=/home/$user/.python
make -j1
make altinstall

pip install --upgrade pip
/home/$user/.python/bin/pip3.8 install virtualenv
cd /home/$user/$project
/home/$user/.python/bin/python3.8 -m venv env

source /home/$user/$project/env/bin/activate
pip install -r /home/$user/$project/$configs/reqs.txt
deactivate
# --------------------------

# network configuration
sudo cp /home/$user/$project/$configs/g*     /lib/systemd/system/
sudo cp /home/$user/$project/$configs/ngi*   /etc/nginx/

sudo ufw allow 22
sudo ufw allow 80
sudo systemctl enable ufw.service
sudo systemctl start ufw.service
sudo ufw enable
sudo ufw status
/home/$user/.python/bin/pip3.8 freeze

sudo systemctl enable nginx.service
sudo systemctl start nginx.service
sudo systemctl enable gunicorn.service
sudo systemctl start gunicorn.service
# --------------------------

echo **** tumturum! All done! ****
