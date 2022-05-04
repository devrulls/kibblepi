from pi_server import app
from pi_server.views import routes
import os

if __name__ == "__main__":
    app.run(host=os.getenv("HOST", "0.0.0.0"), port=os.getenv("PORT", 8080))
