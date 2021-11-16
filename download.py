from pytube import YouTube
import os


class Download():
    '''
    Wrapper class for youtube downloads
    Takes URL and folder to download to
    Video title and download_status
    '''

    def __init__(self, url, folder):
        self.yt = YouTube(url)
        self.url = url
        self.folder = folder
        self.title = self.yt.title
        self.download_status = ''  # status of download

    @property
    def download_video(self):
        '''
        Download video and audio stream.
        '''
        self.download_status = 0 
        #print(f'Downloading {self.yt.title}')
        self.yt.streams.get_highest_resolution().download(self.folder)
        self.download_status = 'VIDEO DOWNLOAD COMPLETE!!!' # "COMPLETE!"
        

    @property
    def download_audio(self):
        '''
        Download audio stream only.
        '''
        self.download_status = 0 # Downloading
        self.yt.streams.get_audio_only().download(self.folder)
        self.download_status = 'AUDIO DOWNLOAD COMPLETE!!!' # Complete
    
    @property    
    def get_status(self):
        return self.download_status
        
'''
test = Download('https://www.youtube.com/watch?v=FrMlRbpSK-A')

test.download_audio(os.getcwd())
print(test.download_status)

'''