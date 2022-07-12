import os
from flask import Flask, render_template, request, url_for, send_file
import custom_error as error
import library

app = Flask(__name__)


@app.route('/download/<string:filename>')
def download(filename):
    path = os.path.join('storage', 'temp', filename)
    try:
        return send_file(library.get_temp(filename), as_attachment=True)
    except:
        return 'File Code is Invalid'


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        file = request.files['file-upload']
        filename = file.filename

        if filename:
            file.save(os.path.join('storage', 'temp', filename))
    return render_template('index.html')


@app.route('/download')
def video_downloader():
    return "Download Page"


@app.errorhandler(404)
def invalid_route(e):
    url = {[url_for(request.endpoint, **request.view_args)]}
    error.save(404, str(e), request.remote_addr, url)
    return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)
