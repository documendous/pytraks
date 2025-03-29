#!/usr/bin/env python
import sys
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to PyTracks!"


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
    app.run(debug=True, port=port, host=host)
