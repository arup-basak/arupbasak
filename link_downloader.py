from pytube import YouTube
import os
import shutil
import library

download_path = os.path.join('storage', 'temp')


def download(link):
    yt = Youtube(link)
    path = yt.download('360p', 'vid')
    return path


def find_link(link: object) -> str:
    temp = link
    if link[:8] == 'https://':
        temp = temp[8:]
    if temp[:4] == 'www.':
        temp = temp[4:]

    if temp[:10].__contains__('youtube') or temp[:10].__contains__('youtu.be'):
        return 'youtube'
    elif temp[:10].__contains__('instagram'):
        return 'instagram'


def insta_find_link(link):
    temp = link
    if link[:8] == 'https://':
        temp = temp[8:]
    if temp[:4] == 'www.':
        temp = temp[4:]
    link_data = temp[13:]

    if link_data[0:3] == '/p/':
        return 'post'
    elif link_data[0:6] == '/reel/':
        return 'reel'
    elif link_data[0:4] == '/tv/':
        return 'igtv'
    else:
        return 'profile'


# class LinkDownloader:
#     def __init__(self, link):
#         website = find_link(link)
#         if website == 'youtube':
#             self.clss = Youtube(link)
#         elif website == 'instagram':
#             self.clss = Instagram(link)
#
#     def download(self, q, vid_aud):
#         return self.clss.download(q, vid_aud)
#
#     def get_list(self):
#         return self.clss.get_vid_list(), self.clss.get_aud_list()

# class Instagram:
#     def __init__(self, link):
#         self.link = link
#         reel = Reel(link)
#         reel.download('/')
#
#     def download(self, q, vid_aud):
#         pass


class Youtube:
    def __init__(self, file_link):
        self.link = file_link
        yt = YouTube(self.link)
        streams = yt.streams
        self.vid_res = []
        self.aud_res = []
        self.video_only = streams.filter(file_extension='mp4', progressive=False).order_by('resolution')
        self.audio_only = streams.filter(only_audio=True).order_by('abr')

        vid_size = len(self.video_only.fmt_streams)
        for i in range(vid_size):
            temp = self.video_only.fmt_streams[i].resolution
            if temp:
                self.vid_res.append(temp)

        aud_size = len(self.audio_only.fmt_streams)
        for i in range(aud_size):
            temp = self.video_only.fmt_streams[i].abr
            if temp:
                self.aud_res.append(temp)

    def get_vid_list(self):
        return self.vid_res

    def get_aud_list(self):
        return self.aud_res

    def download(self, q, vid_aud):
        stream = self.video_only
        if vid_aud == 'vid':
            stream = stream.filter(res=q).first()
        elif vid_aud == 'aud':
            stream = stream.filter(abr=q).first()
        else:
            return None
        stream.download()
        filename = stream.default_filename
        new_filename = filename.replace(' ', '_')
        os.rename(filename, new_filename)
        shutil.move(new_filename, os.path.join(download_path, new_filename))
        path = library.push_temp(new_filename)
        return path
