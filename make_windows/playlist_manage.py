from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Muplayer
from PySimpleGUI import T, B, P, Window
# from shared_utils import chunkit
from sql_database import get_moods
from .window_utils import layout_playlists


# def finalize(base_rows, playlists, size = 6):
#     if not playlists:
#         return base_rows
#     else:
#         chunks = chunkit(playlists, size)
#         for chunk in chunks:
#             elements = []
#             for playlist in chunks:
#                 elements.append(T(playlist))
#             base_rows.append(elements)
#         return base_rows


def mw_playlist_manage(mp: Muplayer, max_elements = 4):
    mp.window.close()

    layout = [
        [P(), B('New Playlist'), B('Rename Playlist'), B('Delete Playlist'), P()],
        [P(), B('Back', key='Menu Main'), P()],
        [P(), T('Playlists'), P()]
    ]

    if additional_rows := layout_playlists(get_moods(), max_elements):
        for row in additional_rows:
            layout.append(row)

    mp.window = Window('Setup Playlists', layout, font = mp.font, size = mp.window_size, use_custom_titlebar = True)
