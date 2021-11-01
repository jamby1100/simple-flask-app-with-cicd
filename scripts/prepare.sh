echo "Installing and I am on"
ls -lah

cd /home/ec2-user/sample-app

python3 -m venv venv
source venv/bin/activate

pip install -r /home/ec2-user/sample-app/requirements.txt

chmod +x /home/ec2-user/sample-app/boot.sh