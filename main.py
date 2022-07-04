import os
from flask import Flask, render_template, jsonify, request, url_for
import library.custom_error as error

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        file = request.files['file-upload']
        filename = file.filename

        if filename:
            file.save(os.path.join('storage', 'temp', filename))
    return render_template('index.html')


@app.errorhandler(404)
def invalid_route(e):
    error.save(404, str(e), request.remote_addr)
    return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)
