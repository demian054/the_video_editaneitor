import pygame as pg
import pygame_gui as pgu


class MenuModule:

    def __init__(self, _manager, dest=(0, 0), size=(800, 600)):
        self.manager = _manager
        self.dest = dest
        self.size = size
        self.menu_panel = pgu.elements.UIPanel(manager=_manager, starting_layer_height=0, relative_rect=pg.Rect(dest, size))

        self.btn_open_file_dest = (0, 0)
        self.btn_open_file_size = (100, size[1] - 5)

        self.lbl_file_opened_dest = (self.btn_open_file_size[0], 0)
        self.lbl_file_opened_size = (400, size[1] - 5)

        self.btn_open_file = pgu.elements.UIButton(
                relative_rect=pg.Rect(self.btn_open_file_dest, self.btn_open_file_size),
                text='Open',
                manager=self.manager, container=self.menu_panel)

        self.lbl_file_opened = pgu.elements.UITextBox(html_text="N/A", manager=self.manager,
                               container=self.menu_panel,
                               relative_rect=pg.Rect(self.lbl_file_opened_dest, self.lbl_file_opened_size))

        self.file_dialog = None
        #
        # rect: pygame.Rect,
        # manager: IUIManagerInterface,
        # window_title: str = 'File Dialog',
        # initial_file_path: Union[str, None] = None,
        # object_id: str = '#file_dialog',
        # allow_existing_files_only: bool = False,
        # allow_picking_directories: bool = False
        # ):



    def update(self, file_module):

        if self.btn_open_file.check_pressed():
            self.file_dialog = pgu.windows.UIFileDialog(
                rect=pg.Rect((0, 0), (600, 700)),
                manager=self.manager,
                allow_picking_directories=True)

        if self.file_dialog is not None and self.file_dialog.ok_button.check_pressed():
            selected_path = str(self.file_dialog.current_file_path)

            self.lbl_file_opened.kill()
            self.lbl_file_opened = pgu.elements.UITextBox(html_text=selected_path, manager=self.manager,
                                                          container=self.menu_panel,
                                                          relative_rect=pg.Rect(self.lbl_file_opened_dest,
                                                                                self.lbl_file_opened_size))

            file_module.set_files_path(selected_path)
            self.file_dialog = None




