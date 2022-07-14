import os
from flask import Flask, render_template, request, url_for, send_file, redirect
import custom_error as error
import library
import link_downloader

app = Flask(__name__)

vid_q_list = []
aud_q_list = []


@app.route('/download/<string:key>')
def download(key):
    path = library.get_temp(key)
    if path:
        return send_file(path, as_attachment=True)
    else:
        return 'File Code is Invalid'


@app.route('/youtube_video_downloader/download/')
def video_downloader():
    if request.method == "GET":
        youtube_link = request.args.get('link')
        return redirect(url_for('download', key=link_downloader.download(youtube_link)))


@app.route('/youtube_video_downloader/res')
def choose_res():
    return render_template('view_res_option.html', list=list)


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
    return render_template('download_link_files.html')


# @app.errorhandler(404)
# def invalid_route(e):
#     url = {[url_for(request.endpoint, **request.view_args)]}
#     error.save(404, str(e), request.remote_addr, url)
#     return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
