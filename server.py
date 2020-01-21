from flask import Flask, jsonify, abort, make_response, url_for, request
from collections import namedtuple
import smtplib
import time
import subprocess
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# config = configparser.ConfigParser()
# config.read("settings.ini")
# server_log = config.get("Settings", "Login")
# server_pass = config.get("Settings", "pass")



app = Flask(__name__)

Login = ''
role = ''

def bat_():
    filepath=r"C:\Users\sergey\Desktop\bat.bat"
    print('start')
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
    #p = subprocess.Popen(['powershell', 'calc'])
    print('finish')
    stdout, stderr = p.communicate()
    print(p.returncode) # is 0 if success

@app.route('/start/all', methods=['POST'])
def login_():
    '''curl -i -H "Content-Type: application/json" -X POST -d "{\"State\": \"test\", \"post\":{\"test\":\"bugaga\"}}" http://127.0.0.1:5000/start/all'''
    if not request.json or not 'State' in request.json:
        abort(400)
    State = request.json.get('State')
    result ='true'
    if root_id == 404:
        return jsonify({'messg': 'oopss'}), 201
    else:
        return jsonify({'State': State, 'result': result}), 201


@app.route('/startALL', methods=['GET'])
def get_all_room():
    roomst = namedtuple('roomst',['name','adress','chairs'])
    room=roomst(1,2,3)
    print(room.name)
    rooms = []
    bat_()
    rooms.append({
        'name': room.name,
        'adress': room.adress,
        'chairs': room.chairs,
    })
    return jsonify({'room': rooms})



if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
