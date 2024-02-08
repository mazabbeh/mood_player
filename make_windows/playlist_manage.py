from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Muplayer
from PySimpleGUI import T, B, P, Window
from shared_utils import chunkit
from sql_database import get_moods


def finalize(base_rows, playlists, size = 6):
    if not playlists:
        return base_rows
    else:
        chunks = chunkit(playlists, size)
        for chunk in chunks:
            elements = []
            for playlist in chunks:
                elements.append(T(playlist))
            base_rows.append(elements)
        return base_rows


def mw_playlist_manage(mp: Muplayer):
    mp.window.close()
    rows = [
        [P(), B('New Playlist'), B('Rename Playlist'), B('Delete Playlist'), P()],
        [P(), B('Back', key='Menu Main'), P()],
        [P(), T('Playlists'), P()]
    ]
    #TODO rework the below statement
    layout = finalize(rows, playlists=get_moods())
    mp.window = Window('Setup Playlists', layout, font = mp.font, size = mp.window_size, use_custom_titlebar = True)
