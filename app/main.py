from flask import Flask, render_template, request, jsonify
from app.model import train_resnet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    # Call the ResNet training function
    result = train_resnet()
    return jsonify({'status': 'Training started', 'details': result})

if __name__ == "__main__":
    app.run(host='0.0.0.0')