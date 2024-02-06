from PySimpleGUI import Text, Button, Push
from shared_utils import gimme_a_squiggly, chunkit


def layout_playlists(playlists, size, button_size = (8, 2)):
    if not playlists:
        return

    additional_rows = []
    for i, group in enumerate(chunkit(playlists, size)):
        buttons = []
        #fuck the rules, I have a very specific reason to repeat myself here.
        buttons.append(Text(gimme_a_squiggly(i)))
        if i % 2 == 0:
            buttons.append(Push())

        for playlist in group:
            button = Button(button_text = playlist, size = button_size)
            buttons.append(button)
        additional_rows.append(buttons)
        if i % 2 == 1:
            buttons.append(Push())
        buttons.append(Text(gimme_a_squiggly(i)))

    return additional_rows

def mw_main_menu(*playlists, current_song = 'None', current_playlist = 'None', button_size = (8, 2), max_elements = 4):

    row_playlist = [Text(f'Playlist: {current_playlist}'), Push()]
    row_song = [Text(f'Track: {current_song}'), Push()]
    row_controls = [Button('Play/Pause'), Button('Pick Track')]
    row_config = [Button('Setup', key='Menu Playlists', size = button_size), Push(), Button('Assign', size = button_size)]
    row_divider = [Push(), Text('~~~PUSH BUTTONS BELOW TO CHANGE MUSIC~~~'), Push()]
    rows = [row_playlist, row_song, row_controls, row_config, row_divider]

    if additional_rows := layout_playlists(playlists, max_elements):
        for row in additional_rows:
            rows.append(row)

    return rows