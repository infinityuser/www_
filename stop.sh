echo "__Server Is Shutted Down"
sudo systemctl stop gunicorn.service
sudo systemctl stop nginx.service
