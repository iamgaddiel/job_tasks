import os, sys


abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(abs_path)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
