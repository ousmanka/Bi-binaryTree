# import cherrypy
#
# class HelloWorld(object):
#     @cherrypy.expose
#     def index(self):
#         return "Hello World!"
#
# cherrypy.quickstart(HelloWorld())


@app.route('/gettingUsername.js', methods=['GET', 'POST'])
def send_js(path):
    return send_from_directory('gettingUsername.js', path)
@app.route("/username")
def get_redUsernames():
    return json.dumps(playerList.get_redUsernames())

@app.route("/username")
def get_blueUsernames():
    return json.dumps(playerList.get_blueUsernames())

@app.route("/send")
def do_redUsernames():
    content = Flask.request.body.read().decode()
    content = json.loads(content)
    playerList.add_redUsername(content["username"])
    return json.dumps(playerList.get_redUsernames())

@app.route("/send")
def do_blueUsernames():
    content = Flask.request.body.read().decode()
    content = json.loads(content)
    playerList.add_blueUsername(content["username"])
    return json.dumps(playerList.get_blueUsernames())

@app.route("/")
def opening_page():
    send_from_directory("index.html")


@app.route('/index.js')
def add_player():
    send_from_directory("index.js")