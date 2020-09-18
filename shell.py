import os

print("git pull origin ec2-server")
os.system("sudo git pull origin ec2-server")

print("daemon-reload")
os.system("sudo systemctl daemon-reload")

print("restart gunicorn")
os.system("sudo systemctl restart gunicorn")

