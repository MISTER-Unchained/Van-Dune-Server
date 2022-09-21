import requests

# URL van de server
URL = "http://127.0.0.1"

# Data om naar de server te pushen, waarbij het "data"-veld alles als inhoud kan hebben. "type", "interval", "data", moeten in elk geval aanwezig zijn anders geeft de server een error.
dat = {
    "type" : "eenTest",
    "interval" : 10_000,
    "data" : [
        "data1",
        "data2",
        "etc."
    ]
}

# Post de data naar de server (endpoint: /api/post) dmv. POST-http request.
new_task = requests.post(f"{URL}/api/post", json=dat)

# Als succesvol en anders error (zie http codes)
if new_task.status_code == 200:
    print("Succesvol data afgeleverd, met als server response: ", new_task.text)
else:
    print("Oeps! Er is iets mis gegaan... De status code was: ", new_task.status_code)
    print("Overige informatie: ", new_task.raw)