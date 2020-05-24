from tkinter import Tk, messagebox
import pygame as pg
import pygame_gui as pgu

from src.modules.videoModule import VideoModule
from src.modules.menuModule import MenuModule
from src.modules.videoFilesModule import VideoFileModule

window_size = (1000, 700)

menu_panel_dest = (0, 0)
menu_panel_size = (window_size[0], 50)

video_panel_dest = (0, menu_panel_size[1])
video_panel_size = (650, window_size[1] - menu_panel_size[1])

files_panel_dest = (video_panel_size[0], menu_panel_size[1])
files_panel_size = (window_size[0] - video_panel_size[0], window_size[1] - menu_panel_size[1])


pg.init()
pg.display.set_caption('The Video Editaneitor')
window_surface = pg.display.set_mode(window_size)

background = pg.Surface(window_size)
background.fill(pg.Color('#000000'))

manager = pgu.UIManager(window_size)


video_module = VideoModule(manager, dest=video_panel_dest, size=video_panel_size)

menu_module = MenuModule(manager, dest=menu_panel_dest, size=menu_panel_size)
file_module = VideoFileModule(manager, dest=files_panel_dest, size=files_panel_size)

#.set_files_path('D:\\livenessData\\videos_original\\Vm9VdmOpzcs\\original\\')

clock = pg.time.Clock()

running = True
while running:
    time_delta = clock.tick(video_module.fps) / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position

            # checks if mouse position is over the button

            # if button.collidepoint(mouse_pos):
            #     # prints current location of mouse
            #     print('button was pressed at {0}'.format(mouse_pos))

        # Keyboard events
        if event.type == pg.KEYDOWN:

            # Play
            if event.key == pg.K_p:
                video_module.play()

            # Pause
            if event.key == pg.K_SPACE:
                video_module.pause()

            # One frame backward
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                video_module.one_frame_backward()

            # One frame forward
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                video_module.one_frame_forward()

            # Set ini
            if event.key == pg.K_1:
                video_module.select_frame_ini()

            # Set end
            if event.key == pg.K_2:
                video_module.select_frame_end()

            # Export
            if event.key == pg.K_s:
                video_module.export()
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showinfo('Saved', 'OK')

            # New analyze
            if event.key == pg.K_n:
                video_module.load_video(path_video)

        manager.process_events(event)

    video_module.update()
    file_module.update(video_module)
    menu_module.update(file_module)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pg.display.update()
