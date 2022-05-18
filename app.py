"""Test harness for loading the dashboard into another page."""
from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def test_page():
    return send_from_directory('./', 'test_page.html')

if __name__ == '__main__':
    app.run(port=5000)