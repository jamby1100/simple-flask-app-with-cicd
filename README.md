# Simple Loyalty Flask Application

This is the sample application for the demo part of my talk

## Development

### Paths

- `GET /` - homepage
- `POST /loyalty_card` - create a loyalty card

### Installation

```sh
python3 -m venv venv
source venv/bin/activate

pip install flask
pip install gunicorn
pip install numpy
pip install boto3
pip freeze > requirements.txt

chmod +x boot.sh
```

### Run it locally

```sh
export FLASK_CONFIG=development
export FLASK_APP=main.py
export FLASK_DEBUG=1
export SPECIALMESSAGE="This is a special message from the ship"
export DYNAMODB_TABLE_NAME="loyalty_cards"
export DYNAMODB_REGION_NAME="ap-southeast-1"

flask run
```

## Deployment

### Deployment Prerequisites

1. Install AWS CLI on your local
    - (Create an AWS IAM user that we will use locally)[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console]
    - (Install AWS CLI using)[https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html]
    - (Add the AKID and Secret that you got from creating the AWS IAM user)[https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html]
2. Create ECR Repo - (follow this tutorial)[https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html]

### Build the docker image locally and push to your ECR repo

```sh
export ECR_URL=""
export VERSION_NUMBER="v0.0.1"

aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin $ECR_URL

docker build -t flask-helloworld .

docker tag flask-helloworld:latest $ECR_URL:$VERSION_NUMBER

docker push $ECR_URL:$VERSION_NUMBER
```

### Deploy the ECS Service

1. Create the DynamoDB table
1. Create the ECS Task Definition
    - follow (this link)[] for the steps
    - Make sure the task role has DynamoDB full access
        - task execution role and task role is different
    - Make sure to set the enviornment variables
        
2. Create an Application Load Balancer
3. Create the ECS Cluster
4. Create the ECS Service
    - with the ECS Task definition
    - inside the ECS Cluste we just created
    - 

