from mutagen.easyid3 import EasyID3
import pygame
from tkinter.filedialog import *
from tkinter import *


pygame.init()


class FrameApp(Frame):
    def __init__(self,master):
        super(FrameApp, self).__init__(master)

        self.grid()
        self.paused = False
        self.playlist = list()
        self.actual_song = 0

        self.b1 = Button(self, text="play", command=self.play_music, width=20)
        self.b1.grid(row=1, column=0)

        self.b2 = Button(self, text="previous", command=self.previous_song,
                         width=20)
        self.b2.grid(row=2, column=0)

        self.b3 = Button(self, text="toggle", command=self.toggle, width=20)
        self.b3.grid(row=3, column=0)

        self.b4 = Button(self, text="next", command=self.next_song, width=20)
        self.b4.grid(row=4, column=0)

        self.b5 = Button(self, text="add to list", command=self.add_to_list,
                         width=20)
        self.b5.grid(row=5, column=0)

        self.label1 = Label(self)
        self.label1.grid(row=6, column=0)

        self.output = Text(self, wrap=WORD, width=50)
        self.output.grid(row=7, column=0)

        '''self.p = ttk.Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
        self.p.grid(row=4, column=0)'''

    '''def pasek_update(self,dlugosc):
        pozycja=0
        while pozycja<dlugosc:
            pozycja=(pygame.mixer.music.get_pos() / 1000)
            proc=(pozycja/dlugosc)*100
            print(proc," %")
            time.sleep(1)
            #self.pasek_update(dlugosc)'''


    #dodaje do listy odtwarzania kolejne utwory
    def add_to_list(self):
        directory = askopenfilenames()
        for song_name in directory:
            self.playlist.append(song_name)
        self.output.delete(0.0, END)

        for item in range(len(self.playlist)):
            song = EasyID3(self.playlist[item])
            song_data = str(item+1)+str(song['title'])+" - "+str(song['artist'])
            self.output.insert(END, str(song_data)+'\n')

    #wyswietla w etykicie nr piosenki,nazwe i wykonawce
    def song_data(self):
        piosenka = EasyID3(self.playlist[self.actual_song])
        danepiosenki = "Teraz gra: Nr:"+str(self.actual_song+1)+" "+str(piosenka['title']) + " - " + str(piosenka['artist'])
        return danepiosenki

    def play_music(self):
        direc=self.playlist[self.actual_song]
        pygame.mixer.music.load((str(direc)))
        pygame.mixer.music.play(1, 0.0)
        self.paused=False
        self.label1['text'] = str(self.song_data())

    def toggle(self):
        print(pygame.mixer.music.get_pos() / 1000)
        if self.paused==True:
            pygame.mixer.music.unpause()
            self.paused=False
        elif self.paused==False:
            pygame.mixer.music.pause()
            self.paused = True

    def next_song(self):
        if self.actual_song+2<=len(self.playlist):
            self.actual_song=self.actual_song+1
        else:
            self.actual_song=0
        self.play_music()

    def previous_song(self):
        if self.actual_song-1>=0:
            self.actual_song=self.actual_song-1
        else:
            self.actual_song=len(self.playlist)-1
        self.play_music()


root = Tk()
root.geometry("350x500")
app = FrameApp(root)
app.mainloop()
