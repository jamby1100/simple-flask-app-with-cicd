echo "Installing and I am on"
ls -lah

cd /home/ec2-user/simple-flask-app-with-cicd

python3 -m venv venv
source venv/bin/activate

pip install -r /home/ec2-user/simple-flask-app-with-cicd/requirements.txt

chmod +x /home/ec2-user/simple-flask-app-with-cicd/boot.sh