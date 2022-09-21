import flask
app = flask.Flask(__name__)

# Database
database = {}

# Homepage: serve de inhoud van /web/index.html
@app.route("/", methods=['GET'])
def hello_world():
    with open("./web/index.html", "r") as f:
        return f.read()

# POST endpoint voor de data
@app.route("/api/post", methods=['POST'])
def api_post():
    # converteer input text (in json) naar dict. Negeer de "tpye: ignore". Dat is een 'interpreter/compiler'-hint voor dynamic typing.
    dat: dict = flask.request.get_json()  # type: ignore

    # Haal de velden uit de dict
    typ = dat["type"]
    typ_interval = dat["interval"]
    posted_data = dat["data"]

    # Zet het op de juist manier in de dict
    database[typ] = {"data": posted_data, "interval": typ_interval}

    # Als succesvol
    return {"succes": True}

# Return de database
@app.route("/api/get/database", methods=['GET'])
def api_get():
    return database

# Return een specifiek item uit de database. <item> is een url-param voor het item.
@app.route("/api/get/<item>", methods=['GET'])
def api_get_item(item):
    return database[item]


# Serve de app
app.run(host='0.0.0.0', port=80)
