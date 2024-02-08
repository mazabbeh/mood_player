import PySimpleGUI as pg
from PySimpleGUI import Window
from PySimpleGUI import WIN_CLOSED
import os
from make_windows import mw_playlist_new, mw_playlist_manage, mw_main_menu, confirm_new_playlist
from sql_database import get_moods, remake_db, create, Mood
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
        mw_main_menu(self)


    def create_playlist(self, name, midi_key=None, sorting=None):
        #TODO unpack kwargs to mood
        playlist = Mood(name = name)
        create(playlist, reraise=True)


mp = Muplayer()


while True:
    event, value = mp.window.read()
    match event:
        case 'Menu Main':
            mw_main_menu(mp)
        #Manage Playlists Menu
        case 'Menu Playlists':
            mw_playlist_manage(mp)
        case 'New Playlist':
            mw_playlist_new(mp)
        case 'Accept New Playlist':
            confirm_new_playlist(value, mp)
        case 'Rename Playlist':
            pass
        case 'Accept_Rename_Playlist':
            pass
        case 'Delete Playlist':
            pass
        case 'Accept_Delete_Playlist':
            pass
        case _:
            if event == WIN_CLOSED:
                break
            else:
                print(event)
#TODO start fleshing out the behavior in this.....  Ugly, ugly...  Ugly and massive case list.
#Should probably make every menu option a case and then like, I don't know, make the else case a Selector for the playlists?
#That could work, you just need to remember that every Case must not be dynamic


mp.window.close()