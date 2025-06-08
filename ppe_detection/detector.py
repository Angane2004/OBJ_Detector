from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import platform

app = Flask(__name__)
CORS(app)  # Allow requests from other origins

@app.route('/detection', methods=['GET'])
def start_detection():
    try:
        if platform.system() == "Windows":
            # Open a new terminal window and run YOLO script
            subprocess.Popen(['start', 'cmd', '/k', 'python', 'yolo_detector.py'], shell=True)
        else:
            # For macOS or Linux
            subprocess.Popen(['python3', 'yolo_detector.py'])
            
        return jsonify({"message": "YOLO detection started in a new window."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Run Flask on port 8000
