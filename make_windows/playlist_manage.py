from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Muplayer

from PySimpleGUI import T, B, P, Window
from sql_database import get_moods
from .window_utils import layout_playlists


def mw_playlist_manage(mp: Muplayer, max_elements = 4):
    mp.window.close()

    base = [
        [P(), B('New Playlist'), B('Rename Playlist'), B('Delete Playlist'), P()],
        [P(), B('Back', key='Menu Main'), P()],
        [P(), T('Playlists'), P()]
    ]

    layout = layout_playlists(base, max_elements)

    mp.window = Window('Setup Playlists', layout, font = mp.font, size = mp.window_size, use_custom_titlebar = True)
