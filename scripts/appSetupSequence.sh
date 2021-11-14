#!/bin/bash

cd /home/ec2-user

sudo yum update -y
sudo yum install git -y
touch git_install.txt

git clone https://github.com/jamby1100/simple-flask-app-with-cicd.git
cd simple-flask-app-with-cicd
touch i_was_here.txt

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
chmod +x boot.sh

./boot.sh

INSTANCE_ID="`wget -q -O - http://instance-data/latest/meta-data/instance-id`"
echo $INSTANCE_ID

cd /home/ec2-user
touch cycle-complete.txt