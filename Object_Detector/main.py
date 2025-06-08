from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import platform

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/start-detection', methods=['GET'])
def start_detection():
    try:
        if platform.system() == "Windows":
            subprocess.Popen(['start', 'cmd', '/k', 'python', 'detector.py'], shell=True)  # Open a new terminal window
        else:
            subprocess.Popen(['python3', 'detector.py'])  # For Linux/macOS
        
        return jsonify({"message": "YOLO detection started in a new window."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
