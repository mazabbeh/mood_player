from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Muplayer
from PySimpleGUI import Text, Button, Push, Input, Window
from sqlalchemy.exc import SQLAlchemyError
from .playlist_manage import mw_playlist_manage


def mw_playlist_new(mp: Muplayer):
    mp.window.close()
    
    layout = [
        [Push(), Text('Name your Legendary Playlist'), Push()],
        [Push(), Input(''), Push()],
        [Push(), Text(key='Informant', text_color='red'), Push()],
        [Push(), Button('Ok', key='Accept New Playlist'), Button('Cancel', key='Menu Playlists'), Push()]
        ]

    mp.window = Window('Setup Playlists', layout, font = mp.font, size = mp.window_size, use_custom_titlebar = True)



def confirm_new_playlist(value, mp: Muplayer):


    if not value[0]:
        mp.window['Informant'].update('MUST NOT BE BLANK')
    else:
        try:
            name = value[0]
            mp.create_playlist(name)
            mw_playlist_manage(mp)
        except SQLAlchemyError:
            mp.window['Informant'].update(f'PLAYLIST {value[0]} ALREADY EXISTS')