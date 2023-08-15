# Import necessary libraries
from pygame import mixer
from tkinter import *
from tkinter import filedialog

# Initialize the mixer module
mixer.init()

# Load and play a specific music file
mixer.music.load('hear-me-134134.mp3') 

mixer.music.play()
mixer.music.pause() 

mixer.music.unpause()
mixer.music.stop()


# Create a class for the MusicPlayer application
class MusicPlayer:
    def __init__(self, window ):

        #Setup the window
        window.geometry('320x100'); 
        window.title('Music Player')
        window.resizable(0,0)

        # Create buttons for control
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)

        # Place buttons on the window
        Load.place(x=0,y=20)
        Play.place(x=110,y=20)
        Pause.place(x=220,y=20)
        Stop.place(x=110,y=60)
        
        # Initialize attributes
        self.music_file = False
        self.playing_state = False

    def load(self):
        # Open file dialog to select a music file
        self.music_file = filedialog.askopenfilename()


    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()

# Create the Tkinter window
root = Tk()
app= MusicPlayer(root)
root.mainloop()