from instascrape import Reel

link = 'https://www.instagram.com/reel/Cf14kgNo-C5/?utm_source=ig_web_button_share_sheet'
reel = Reel(link)
reel.download('video.mp4')