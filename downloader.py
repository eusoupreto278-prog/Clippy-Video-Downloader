from yt_dlp import YoutubeDL

import threading

class Download:
    def download_video(self, url, mp3, mkv):
        if 'www.youtube.com' in url:
            if mp3:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    }]
                }

            elif mkv:
                ydl_opts = {
                    'format': 'bv*+ba/b',
                    'merge_output_format': 'mkv',
                }

            else:
                ydl_opts = {
                    'format': 'bv*+ba/b',
                    'merge_output_format': 'mp4',
                }

            try:        
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)

            except:
                pass

            print('[url]', url)

    def start_download(self, url, mp3, mkv):
        t = threading.Thread(target=self.download_video, 
                            args=(url, mp3, mkv))
        t.start()