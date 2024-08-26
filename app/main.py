from flask import Flask, render_template, request, jsonify, Response
from app.model import train_resnet
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    # Call the ResNet training function
    def generate():
        for log in train_resnet():
            yield log + '<br>'
            # Optional: simulate some delay
            time.sleep(1)
    
    return Response(generate(), content_type='text/html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')