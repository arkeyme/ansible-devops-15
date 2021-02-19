from flask import Flask
from redis import Redis
app = Flask(__name__)
db = Redis (host="redis")

@app.route('/')
def hello():
    visitsCounter = db.incr('visitsCounter')
    html = """
    <h1>Hello {visits}-person! Hello {visits}-person! Hello {visits}-person! Hello {visits}-person!</h1>
    <h1>Hello {visits}-person! Hello {visits}-person! Hello {visits}-person! Hello {visits}-person!</h1>
    <h1>Hello {visits}-person! Hello {visits}-person! Hello {visits}-person! Hello {visits}-person!</h1>
    <h1>Hello {visits}-person! Hello {visits}-person! Hello {visits}-person! Hello {visits}-person!</h1>
    <h1>Hello {visits}-person! Hello {visits}-person! Hello {visits}-person! Hello {visits}-person!</h1>
    <h1>Hello {visits}-person! Hello {visits}-person! Hello {visits}-person! Hello {visits}-person!</h1>
    <h1>Hello {visits}-person! Hello {visits}-person! Hello {visits}-person! Hello {visits}-person!</h1>
    <h1>Hello {visits}-person! Hello {visits}-person! Hello {visits}-person! Hello {visits}-person!</h1>
    """
    return html.format(visits=visitsCounter)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80")