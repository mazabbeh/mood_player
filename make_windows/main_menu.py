from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Muplayer

from PySimpleGUI import Text, Button, Push, Window
from sql_database import get_moods
from .window_utils import layout_playlists


def mw_main_menu(mp: Muplayer, current_song = 'None', current_playlist = 'None', button_size = (8, 2), max_elements = 4):
    row_playlist = [Text(f'Playlist: {current_playlist}'), Push()]
    row_song = [Text(f'Track: {current_song}'), Push()]
    row_controls = [Button('Play/Pause'), Button('Pick Track')]
    row_config = [Button('Setup', key='Menu Playlists', size = button_size), Push(), Button('Assign', size = button_size)]
    row_divider = [Push(), Text('~~~PUSH BUTTONS BELOW TO CHANGE MUSIC~~~'), Push()]
    layout = [row_playlist, row_song, row_controls, row_config, row_divider]

    if additional_rows := layout_playlists(get_moods(), max_elements):
        for row in additional_rows:
            layout.append(row)

    mp.window = Window('Setup Playlists', layout, font = mp.font, size = mp.window_size, use_custom_titlebar = True)