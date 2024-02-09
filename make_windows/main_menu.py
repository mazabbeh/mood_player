from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Muplayer

from PySimpleGUI import T, B, P, Window
from sql_database import get_moods
from .window_utils import layout_playlists


def mw_main_menu(mp: Muplayer, current_track = 'None', current_playlist = 'None', btn_size = (8, 2), max_elements = 4):
    base = [
        [T('Playlist: '), T(f'{current_playlist}', key='Current Playlist'), P()],
        [T('Track: '), T(f'{current_track}', key='Current Track'), P()],
        [B('Play/Pause'), B('Pick Track')],
        [B('Setup', key='Menu Playlists', size=btn_size), P(), B('Assign', key='Menu Assignment', size=btn_size)],
        [P(), T('~~~PUSH BUTTONS BELOW TO CHANGE MOOD~~~'), P()]
    ]

    layout = (layout_playlists(base, max_elements))

    mp.window = Window('Setup Playlists', layout, font = mp.font, size = mp.window_size, use_custom_titlebar = True)