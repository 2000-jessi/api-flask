from flask import Flask, jsonify, render_template, send_file

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    file = open("./spam-ham.txt","r")
    spam= file.read(3)
    ham= file.read(3)
    return jsonify({"Spam": str(spam),"Ham":str(ham)})

@app.route('/image',methods=['GET'])
def image():
    return send_file('./Correos.jpg',attachment_filename='Correos.jpg')

@app.route('/prediction',methods=['GET'])
def prediction():
    file= open('./prediction.txt',"r")
    prediction = file.read()
    return jsonify({"Prediction": str(prediction)})

@app.route('/accuracy',methods=['GET'])
def accuracy():
    file= open('./accuracy.txt',"r")
    accuracy = file.read()
    return jsonify({"Accuracy": str(accuracy)})

if __name__ == '__main__':
    app.run(port=5000)