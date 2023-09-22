from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Jeremy Imbisi",
        "email": "jeremyimbisi44@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/")
def home():
    return "Welcome to your homepage Jeremy"

if __name__ == "__main__":
    app.run(debug=True)
