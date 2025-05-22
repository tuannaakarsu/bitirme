from flask import Flask, request, jsonify
from PIL import Image
import io
import base64
import torch  # eğer PyTorch modeliniz varsa

app = Flask(__name__)

@app.route('/vton', methods=['POST'])
def vton():
        data = {'message': 'Merhaba, bu bir API!'}
        return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
