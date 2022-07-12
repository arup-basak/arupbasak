import os
from flask import Flask, render_template, request, url_for, send_file, redirect
import custom_error as error
import library
import link_downloader

app = Flask(__name__)


@app.route('/download/<string:key>')
def download(key):
    path = library.get_temp(key)
    print(path)
    if path:
        return send_file(path, as_attachment=True)
    else:
        return 'File Code is Invalid'


@app.route('/download', methods=['GET'])
def video_downloader():
    if request.method == "GET":
        youtube_link = request.args.get('link')
        redirect(url_for('download/' + link_downloader.download(youtube_link)))

        return "Download Page"


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        file = request.files['file-upload']
        filename = file.filename

        if filename:
            file.save(os.path.join('storage', 'temp', filename))
    return render_template('index.html')


@app.route('/youtube_video_downloader/', methods=['GET', 'POST'])
def downloader():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            print("Hello World")
    return render_template('download_link_files.html')


# @app.errorhandler(404)
# def invalid_route(e):
#     url = {[url_for(request.endpoint, **request.view_args)]}
#     error.save(404, str(e), request.remote_addr, url)
#     return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)
