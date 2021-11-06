#!/bin/sh
echo "Currently booting and i am on"
pwd
ls -lah

cd /home/ec2-user/sample-app
echo "And now shifted"
ls -lah
pwd

source /home/ec2-user/simple-flask-app-with-cicd/venv/bin/activate

nohup gunicorn -b :5000 --access-logfile - --error-logfile - main:app </dev/null &>/dev/null &