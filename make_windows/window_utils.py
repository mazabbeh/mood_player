from shared_utils import chunkit, gimme_a_squiggly
from PySimpleGUI import Push, Text, Button


def layout_playlists(playlists, size, button_size = (8, 2)):
    if not playlists:
        return

    additional_rows = []
    for i, group in enumerate(chunkit(playlists, size)):
        buttons = []
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