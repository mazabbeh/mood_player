from PySimpleGUI import T, B, P, Window
from shared_utils import chunkit



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


def playlist_setup(mp):
    mp.window.close()
    rows = [
        [P(), B('New Playlist'), B('Rename Playlist'), B('Delete Playlist'), P()],
        [P(), B('Back'), P()],
        [P(), T('Playlists'), P()]
    ]
    layout = finalize(rows, mp.playlists)
    mp.window = Window('Setup Playlists', layout, font = mp.font, size = mp.window_size, use_custom_titlebar = True)