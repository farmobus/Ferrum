# main 1a63b5c2a944d7c5d775205e14a7cdd2980171ae73363a2167e8dd6d37695b5de4960463be11b5a77c269
# 200615913
# confirm 995899ba

from flask import Flask, request, json
import vk
import random

token = '1a63b5c2a944d7c5d775205e14a7cdd2980171ae73363a2167e8dd6d37695b5de4960463be11b5a77c269'
confirm_token = '995899ba'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Server online'

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' in data.keys():
        type = data['type']
        if type == 'confirmation':
            return '995899ba'
        elif type == 'message_new':
            session = vk.Session()
            api = vk.API(session, v='5.131')
            user_id = data['object']['message']['from_id']
            api.messagen.send(acces_token=token, user_id=str(user_id), message='test of this bot step 1', random_id=random.getrandbits(64))
            return 'ok'
