from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "uuptstespdated Hello from Azure Web App deployed via Azure DevOps!"})

# 2️⃣ Basic info endpoint
@app.route("/info")
def info():
    return jsonify({
        "app": "Azure Flask Demo",
        "version": "1.0",
        "author": "Your Name"
    })

# 3️⃣ POST API to echo data
@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({
        "received_data": data,
        "message": "POST request received successfully"
    })




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
