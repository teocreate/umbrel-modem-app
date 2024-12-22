
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def send_sms():
    number = request.json['number']
    message = request.json['message']
    try:
        result = subprocess.run(
            ['gammu-smsd-inject', 'TEXT', number, '-text', message],
            check=True,
            stdout=subprocess.PIPE
        )
        return jsonify({"status": "success", "output": result.stdout.decode()})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "output": e.output.decode()}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
