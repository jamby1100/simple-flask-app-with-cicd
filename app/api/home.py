from flask import jsonify, request, render_template, redirect, url_for, Response
from . import api
import os
import json
import random
import string

from ..gateways.dynamodb_gateway import DynamodbGateway


user_db = {
    "raphael.jambalos@gmail.com": {"password": "authoriscool", "token": "jambytoken"},
    "test.driver@gmail.com": {"password": "driveiscool", "token": "testdriver"},
    "ultra.player@gmail.com": {"password": "ultraplayeriscool", "token": "ultraplayer"},
    "super.user@gmail.com": {"password": "superuseriscool", "token": "superuser"},
    "code.maestro@gmail.com": {"password": "codemaestroiscool", "token": "codemaestro"},
}


def build_post_body():
    if request.json:
        return request.json
    elif request.form.to_dict():
        return request.form.to_dict()

    return {}

def authenticated():
    auth_token = request.headers.get('Auth')

    for email in user_db:
        user = user_db[email]
        if user["token"] == auth_token:
            return True

    return False


@api.route('/')
def home():
    return json.dumps({"status": "welcome to the homepage"})

cards = []

@api.route('/users/signin', methods=['POST'])
def users_signin():
    post_body = build_post_body()

    if "email" not in post_body or "password" not in post_body:
        return Response("{'access denied':'your request does not have email or password'}", status=403, mimetype='application/json')

    if post_body["email"] in user_db:
        user = user_db[post_body["email"]]

        if user["password"] == post_body["password"]:
            token = user['token']
            return Response("{'token':" + token + "}", status=200, mimetype='application/json')
        else:
            return Response("{'access denied':'you have the wrong password'}", status=403, mimetype='application/json')
    else:
        return Response("{'access denied':'username is not in database'}", status=403, mimetype='application/json')

@api.route('/loyalty_cards', methods=['POST'])
def loyalty_cards_create():
    post_body = build_post_body()

    print("LOYALTY CARDS")

    if not authenticated():
        return Response("{'forbidden':'you are logged out'}", status=403, mimetype='application/json')

    if "first_name" not in post_body or "last_name" not in post_body:
        return Response("{'wrong input':'you did not supply a last name or first name'}", status=400, mimetype='application/json')

    if len(post_body["first_name"]) <= 2 or len(post_body["last_name"]) <= 2:
        return Response("{'wrong input':'last name or first name must be more than 2 letters'}", status=400, mimetype='application/json')
    
    random_part = ''.join(random.choice(string.digits) for _ in range(12))
    card_number = f"4444{str(random_part)}"
    table_name = os.getenv("DYNAMODB_TABLE_NAME")

    card_data = {
        "card_number": card_number,
        "first_name": post_body["first_name"],
        "last_name": post_body["last_name"]
    }

    data = [card_data]

    DynamodbGateway.upsert(table_name, data)

    return json.dumps({"status": "we created loyalty cards", "post_body": card_data})

@api.route('/loyalty_cards/<loyalty_card_id>', methods=['GET'])
def loyalty_cards_show(loyalty_card_id):
    if not authenticated():
        return Response("{'forbidden':'you are logged out'}", status=403, mimetype='application/json')

    print(f"RETRIEVE INFORMATION FOR loyalty_card_id: {loyalty_card_id}")

    table_name = os.getenv("DYNAMODB_TABLE_NAME")
    result = DynamodbGateway.query_by_partition_key(table_name, "card_number", loyalty_card_id)

    if result == []:
        return Response("{'error':'card with that id number is not found'}", status=404, mimetype='application/json')

    item = result[0]

    return json.dumps({"item": item})