import PySimpleGUI as pg
from PySimpleGUI import Window
from PySimpleGUI import WIN_CLOSED
import os
from make_windows import mw_playlist_new, mw_playlist_manage, mw_main_menu
from sql_database import get_moods, remake_db
from shared_utils import setup_logger
logger = setup_logger('app', 'logs/app.log')


if not os.path.exists('app.db'):
    remake_db()


class Muplayer:
    def __init__(self, font = ('helvetica', 12), button_size = (8, 2), window_size = (600, 400)):
        self.font = font
        self.button_size = button_size
        self.window_size = window_size
        self.window: Window
        self.playlists: dict = self.read_playlists()
        self.initial_window()


    def read_playlists(self):
        self.playlists = get_moods(logger)


    def initial_window(self):
        if self.playlists:
            layout = mw_main_menu(self.playlists)
        else:
            layout = mw_main_menu()
        self.window = Window('Muplayer', layout, font = self.font , size = self.window_size, use_custom_titlebar = True)


mp = Muplayer()


while True:
    event, value = mp.window.read()
    match event:
        #Manage Playlists Menu
        case 'Menu Playlists':
            mw_playlist_manage(mp)
        case 'New Playlist':
            mw_playlist_new(mp)
        case 'Accept New Playlist':
            print(event, value)
            from make_windows.playlist_new import confirm_new_playlist
            confirm_new_playlist(value, mp)
        case 'Rename Playlist':
            pass
        case 'Accept_Rename_Playlist':
            pass
        case 'Delete Playlist':
            pass
        case 'Accept_Delete_Playlist':
            pass
        case WIN_CLOSED:
            break


mp.window.close()