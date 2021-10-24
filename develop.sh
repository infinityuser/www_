project='www'
entry='source'
user='debian'

sudo systemctl start nginx.service
source /home/$user/$project/env/bin/activate
cd /home/$user/$project/$entry/
export FLASK_DEBUG=1
export FLASK_APP="wsgi.py"
flask run -p 4000
sudo systemctl stop nginx.service
