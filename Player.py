import dearpygui.dearpygui as dpg
from tkinter.filedialog import askopenfilenames
import sounddevice as sd
import soundfile as sf

class Player:
    def selectFile(self):
        self.filename = askopenfilenames()
        self.ind = 0
        self.showSongsName(self.ind)
        # self.song = sf.SoundFile(self.filename[self.ind])
        # self.duration = self.song.frames / self.song.samplerate
    def showSongsName(self, ind):
        dpg.add_text([song.split('/')[-1] for song in self.filename], post=(50, 50), parent='main_window')
    def play(self, ind):
        data, fs = sf.read(self.filename[self.ind], dtype='float32')
        sd.play(data, fs)
    def stop(self):
        sd.stop()
    def nextSong(self, ind):
        if self.ind < len(self.filename) - 1:
            self.ind += 1
            self.play(self.ind)
    def prevSong(self):
        if self.ind > 0:
            self.ind -= 1
            self.play(self.ind)