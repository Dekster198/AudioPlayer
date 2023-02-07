import dearpygui.dearpygui as dpg
from tkinter.filedialog import askopenfilenames
import sounddevice as sd
import soundfile as sf

class Player:
    global filename

    def selectFile(self):
        self.filename = askopenfilenames()
    def play(self):
        for song in self.filename:
            data, fs = sf.read(song, dtype='float32')
            sd.play(data, fs)
    def stop(self):
        sd.stop()
    def nextSong(self):
        pass
    def prevSong(self):
        pass