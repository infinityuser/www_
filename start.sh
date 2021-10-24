sudo systemctl start gunicorn.service
sudo systemctl start nginx.service

echo "__Current Status"
sudo systemctl status gunicorn.service
sudo systemctl status nginx.service
