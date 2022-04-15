import os

from pi_server import app

if __name__ == "__main__":
    app.run(host=os.getenv("HOST", "0.0.0.0"), port=os.getenv("PORT", 8080))
