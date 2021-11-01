aws ecr get-login-password --region ap-northeast-1 --profile personal | docker login --username AWS --password-stdin 272898481162.dkr.ecr.ap-northeast-1.amazonaws.com

docker build . -t loyalty-flask-demo-app:latest 

docker tag loyalty-flask-demo-app:latest 272898481162.dkr.ecr.ap-northeast-1.amazonaws.com/loyalty-flask-demo-app:v0.0.2

docker push 272898481162.dkr.ecr.ap-northeast-1.amazonaws.com/loyalty-flask-demo-app:v0.0.2

