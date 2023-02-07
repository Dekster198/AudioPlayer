import dearpygui.dearpygui as dpg
from tkinter.filedialog import askopenfilename
from Player import Player

def main():
    player = Player()

    dpg.create_context()

    dpg.create_viewport(title='Media Player', width=600, height=500)

    with dpg.window(width=600, height=500):
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Select file", callback=player.selectFile)

        dpg.add_button(label='Play', width=50, height=20, pos=(250, 400), callback=player.play)
        dpg.add_button(label='Stop', width=50, height=20, pos=(320, 400), callback=player.stop)
        dpg.add_button(label='Prev Song', width=80, height=20, pos=(150, 400), callback=player.prevSong)
        dpg.add_button(label='Next Song', width=80, height=20, pos=(390, 400), callback=player.nextSong)


    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == '__main__':
    main()