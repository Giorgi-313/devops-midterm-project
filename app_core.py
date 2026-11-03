from flask import Flask, jsonify

app = Flask(__name__)

# სატესტო მონაცემთა ბაზა
tasks_db = {
    1: {"id": 1, "title": "Setup CI/CD", "status": "done"},
    2: {"id": 2, "title": "Write Unit Tests", "status": "in_progress"}
}

@app.route("/")
def home():
    return jsonify({"message": "DevOps Midterm API is running!"})

@app.route("/api/health")
def health_status():
    return jsonify({"status": "healthy", "version": "1.0.0"})

@app.route("/api/tasks")
def get_tasks():
    return jsonify(list(tasks_db.values()))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)