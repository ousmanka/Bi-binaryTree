from flask import Flask, send_from_directory, render_template
# import json
# import playerList
from webapp import templates
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

# @app.route("/index.js")
# def main():
#     return render_template("index.js")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)


# @app.route('/gettingUsername.js', methods=['GET', 'POST'])
# def send_js(path):
#     return send_from_directory('gettingUsername.js', path)
# @app.route("/username")
# def get_redUsernames():
#     return json.dumps(playerList.get_redUsernames())
#
# @app.route("/username")
# def get_blueUsernames():
#     return json.dumps(playerList.get_blueUsernames())
#
# @app.route("/send")
# def do_redUsernames():
#     content = Flask.request.body.read().decode()
#     content = json.loads(content)
#     playerList.add_redUsername(content["username"])
#     return json.dumps(playerList.get_redUsernames())
#
# @app.route("/send")
# def do_blueUsernames():
#     content = Flask.request.body.read().decode()
#     content = json.loads(content)
#     playerList.add_blueUsername(content["username"])
#     return json.dumps(playerList.get_blueUsernames())
#
# @app.route("/")
# def opening_page():
#     send_from_directory("index.html")
#
#
# @app.route('/index.js')
# def add_player():
#     send_from_directory("index.js")