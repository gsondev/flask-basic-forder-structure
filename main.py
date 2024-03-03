import os
from app import init_app, db
from app.models import user
from flask_migrate import Migrate

app = init_app()
migrate = Migrate(app, db)

host = os.getenv('HOST', 'localhost')
port = os.getenv('PORT', 5000)

if __name__ == "__main__":
  app.run(host=host, port=port)