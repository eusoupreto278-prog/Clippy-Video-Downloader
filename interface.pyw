
"""
    Add a function to save data about downloaded videos into an SQLite database
"""

from downloader import Download

import customtkinter as ctk

class Interface:
    def __init__(self):
        self.dld = Download()

        self.MP3 = False
        self.MKV = False

        # Window

        self.app = ctk.CTk()
        self.app.title('Clippy')
        self.app.resizable(False, False)
        self.app.geometry('250x200')
       
        ctk.set_appearance_mode('dark')

        # Entry box

        self.entry = ctk.CTkEntry(self.app, 
                                    placeholder_text='URL'
                                    )
        self.entry.pack(pady=15)
     
        # MP3 check var
     
        self.check_var1 = ctk.StringVar(value='off')
        self.checkbox1 = ctk.CTkCheckBox(self.app, 
                                        command=self.check_mp3, 
                                        variable=self.check_var1, 
                                        hover_color='#EA0000',
                                        fg_color='#EA0000',
                                        offvalue='off',
                                        onvalue='on', 
                                        text='MP3'
                                        )
        self.checkbox1.pack(pady=5)
     
        # MKV check var
     
        self.check_var2 = ctk.StringVar(value='off')
        self.checkbox2 = ctk.CTkCheckBox(self.app, 
                                        variable=self.check_var2, 
                                        command=self.check_mkv, 
                                        hover_color='#EA0000',
                                        fg_color='#EA0000',
                                        offvalue='off',
                                        onvalue='on', 
                                        text='MKV'
                                        )
        self.checkbox2.pack()
     
        # Button
     
        self.button = ctk.CTkButton(self.app, text='Download', 
                                        command=lambda: self.dld.start_download(
                                        self.entry.get(), 
                                        self.MP3, self.MKV),
                                        hover_color='#B30000',
                                        fg_color='#EA0000'
                                        )
        self.button.pack(pady=20)

        self.app.mainloop()
  
    # MP3 check box

    def check_mp3(self):
        if not self.MP3:
            self.MP3 = True

        else:
            self.MP3 = False

        print('[MP3]', self.MP3)

        # MKV check box
    
    # MKV chech box

    def check_mkv(self):
        if not self.MKV:
            self.MKV = True

        else:
            self.MKV = False

        print('[MKV]', self.MKV)

Interface()