from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/health',methods=['GET'])

def health_check():
    return jsonify({"status": "healthy"}) ,200

@app.route('/tasks',methods=['GET'])

def get_tasks():
    return jsonify({"tasks": tasks}) , 200

@app.route('/tasks',methods=['POST'])

def create_tasks():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({"error": "Title Required"}) , 400

    task = {
        "id": len(tasks)+1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(task)
    return jsonify(task), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)