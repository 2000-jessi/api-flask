from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Servidor en puerto"})


if __name__ == '__main__':
    app.run(threaded=True,port=5000)