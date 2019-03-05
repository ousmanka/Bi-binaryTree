import bottle
import json
import guess
from bottle import route, run, template, get

@route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root="c:/python32/bottle/build/static")

@bottle.route('/hello/:name')
def gameHTML(name='mock-up'):
    return bottle.static_file('mock-up', name=name)


@bottle.route('/username.js')
def static():
    return bottle.static_file("username.js", root="")


@bottle.route('/guess')
def get_Guesses():
    return json.dumps(guess.get_Guesses())


@bottle.post('/send')
def do_Guesses():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    guess.add_Guesses(content['guess'])
    return json.dumps(guess.get_Guesses())


bottle.run(host="0.0.0.0", port=8080, debug=True)