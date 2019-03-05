import bottle
import json
import username
from bottle import route, run, template, get

@route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root='/absolute/path/to/static')

@bottle.route("/")
def usernameHTML():
    return bottle.static_file('index.html', root="")


@bottle.route('/username.js')
def static():
    return bottle.static_file("username.js", root="")


@bottle.route('/username')
def get_usernames():
    return json.dumps(username.get_usernames())


@bottle.post('/send')
def do_chat():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    username.add_username(content['username'])
    return json.dumps(username.get_usernames())


bottle.run(host="0.0.0.0", port=8080, debug=True)
