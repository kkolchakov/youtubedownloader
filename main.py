from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRect, TextfieldLabel, MDTextField
from kivy.properties import StringProperty,ObjectProperty
from kivymd.uix.dialog import MDDialog
import os
from download import Download

url_kv = """
MDTextField:
    hint_text: 'Enter Video URL'
    pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    size_hint_x:0.8
    
    multiline: True



"""


class YouTubeDownloderApp(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.folder = os.getcwd()
        self.status_text = 'Status'
        self.stream_title = ''

    def build(self):
        
        
        self.theme_cls.theme_style = 'Dark'  # use for dark theme

        screen = Screen()
        screen.padding = '15dp'

        

        self.url_textfield = Builder.load_string(url_kv)

        download_video_button = MDRectangleFlatButton(text='Download Video', pos_hint={
                                                      'center_x': 0.5, 'center_y': 0.4})
        
        download_audio_button = MDRectangleFlatButton(text='Download Audio', pos_hint={
                                                      'center_x': 0.5, 'center_y': 0.3}) 

        folder_label = MDTextField(hint_text=f'Current download folder:\n{self.folder}',
                                pos_hint={'center_x':0.5, 'center_y':0.6},
                                font_size='15dp',
                                size_hint_x = 0.8)

        
        


        screen.add_widget(self.url_textfield)   
        screen.add_widget(download_video_button)        
        screen.add_widget(download_audio_button)
        screen.add_widget(folder_label)        
        
        download_audio_button.bind(on_press=self.audio_download)
        download_audio_button.bind(on_release=self.show_data)
        download_video_button.bind(on_press=self.video_download)
        download_video_button.bind(on_release=self.show_data)
        
        
        
        
    
        
        return screen

    
    def video_download(self, ins):
        stream = Download(self.url_textfield.text, self.folder)
        stream.download_video
        self.status_text = stream.download_status
        self.stream_title = stream.title
        

    def audio_download(self,ins):
        stream = Download(self.url_textfield.text, self.folder)
        stream.download_audio
        self.status_text = stream.download_status
        self.stream_title = stream.title
        
    def show_data(self, ins):
        
        dialog_text = f'Downloading:\n {self.stream_title}!\n\n {self.status_text}'''
        self.dialog = MDDialog(text= dialog_text,size_hint=(0.7,0.1),
                          buttons=[MDFlatButton(text='Close',on_release=self.close_dialog)])
        self.dialog.open()
    
    def close_dialog(self,obj):
        self.dialog.dismiss()  
    
    

if __name__ == '__main__':

    YouTubeDownloderApp().run()
