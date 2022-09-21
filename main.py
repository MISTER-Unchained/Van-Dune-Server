import flask

app = flask.Flask(__name__)


database = {}


@app.route("/", methods=['GET'])
def hello_world():
    with open("./web/index.html", "r") as f:
        return f.read()


@app.route("/api/post", methods=['POST'])
def api_post():
    dat = flask.request.get_json()
    typ = dat["type"]
    typ_interval = dat["interval"]
    posted_data = dat["data"]
    database[typ] = {"data": posted_data, "interval": typ_interval}
    return {"succes": True}


@app.route("/api/get/database", methods=['GET'])
def api_get():
    return database


@app.route("/api/get/<item>", methods=['GET'])
def api_get_item(item):
    return database[item]


# @app.route("/api/get", methods=['GET'])
# def api_get():
#     return database


app.run(host='0.0.0.0', port=80)
