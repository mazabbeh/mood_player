from shared_utils import chunkit, gimme_a_squiggly
from PySimpleGUI import Push, Text, Button


def layout_playlists(layout: list, size, button_size = (8, 2)):
    additional_rows = []
    for i, group in enumerate(chunkit(layout, size)):
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

    for row in additional_rows:
        layout.append(row)

    return layout