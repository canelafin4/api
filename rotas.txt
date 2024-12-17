from flask import Flask, jsonify, request


app = Flask(__name__)

users = [
    {
        'id': 1,
        'name': 'João',
        'email': 'email@gmail.com',
        'telefone': 112345678
    },

    {
       'id': 2,
        'name': 'Paulo',
        'email': 'email@hotmail.com',
        'telefone': 110123456  
    }
]

#test
@app.route('/home')
def home():
    return 'hi'

#get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

#get all user information by name
@app.route('/users/<string:name>', methods=['GET'])
def get_user(name):
    for user in users:
        if user.get('name') == name:
            return jsonify(user)

#add new user to list
@app.route('/users', methods=['POST'])     
def create_new_user():
    new_user = request.get_json()
    users.append(new_user)

    return jsonify(users)

app.run(port=3000, host='localhost', debug=True)