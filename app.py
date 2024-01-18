import PySimpleGUI as pg
from PySimpleGUI import Window
from PySimpleGUI import WIN_CLOSED
import json
from make_windows import main_menu, playlist_setup

class Muplayer:
    def __init__(self, font = ('helvetica', 12), button_size = (8, 2), window_size = (600, 400)):
        self.font = font
        self.button_size = button_size
        self.window_size = window_size
        self.window: Window
        self.playlists: dict = self.read_playlists()
        self.initial_window()


    def initial_window(self):
        if self.playlists:
            layout = main_menu(self.playlists)
        else:
            layout = main_menu()
        self.window = Window('Muplayer', layout, font = self.font , size = self.window_size, use_custom_titlebar = True)


    def read_playlists(self):
        try:
            with open('playlists.json', 'r') as fh:
                data = json.loads(fh.read())
                return data
        except FileNotFoundError:
            self.playlists = {}


    def save_playlists(self):
        new_contents = json.dumps(self.playlists, indent = 4)
        with open('playlists.json', 'w') as fh:
            fh.write(new_contents)


mp = Muplayer()


while True:
    event, value = mp.window.read()
    match event:
        case 'Setup':
            playlist_setup(mp)
        case 'Assign':
            pass
        case 'Back':
            break
        case WIN_CLOSED:
            break


mp.window.close()