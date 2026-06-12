from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

sensor_data = {
    "heart_rate": 0,
    "spo2": 0,
    "hemoglobin": 0.0
}

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def receive_data():
    global sensor_data
    data = request.get_json()
    if data:
        sensor_data['heart_rate'] = data.get('heart_rate', sensor_data['heart_rate'])
        sensor_data['spo2'] = data.get('spo2', sensor_data['spo2'])
        sensor_data['hemoglobin'] = data.get('hemoglobin', sensor_data['hemoglobin'])
    return jsonify({"status": "success"}), 200

@app.route('/api/data', methods=['GET'])
def send_data():
    return jsonify(sensor_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
