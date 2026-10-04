from flask import Flask, request, jsonify
from db import init_db, create_user, get_user


def create_app(testing=False):
    app = Flask(__name__)
    app.config["TESTING"] = testing
    app.config["DATABASE"] = "test.db" if testing else "app.db"

    init_db(app)

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.route("/users", methods=["POST"])
    def add_user():
        data = request.get_json()
        create_user(app, data["name"], data["email"])
        return jsonify({"msg": "user created"}), 201

    @app.route("/users/<email>")
    def fetch_user(email):
        user = get_user(app, email)
        if not user:
            return jsonify({"error": "not found"}), 404
        return jsonify({"name": user[1], "email": user[2]})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
