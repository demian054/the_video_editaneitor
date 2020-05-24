import pygame as pg
import pygame_gui as pgu
import glob
import os

from src.modules.videoFileRowModule import VideoFileRow

class VideoFileModule:

    def __init__(self, _manager, dest=(0, 0), size=(800, 600), page_size=18):
        self.manager = _manager
        self.dest = dest
        self.size = size

        self.row_size = (self.size[0] - 5, int(self.size[1] / page_size))

        self.page = 0
        self.last_page = 0
        self.page_size = page_size

        self.btn_page_back_dest = (30, size[1] - 35)
        self.btn_page_back_size = (100, 30)

        self.btn_page_next_dest = (self.btn_page_back_dest[0] + self.btn_page_back_size[0] + 30, size[1] - 35)
        self.btn_page_next_size = (100, 30)

        self.lbl_page_info_dest = (self.btn_page_next_dest[0] + self.btn_page_next_size[0] + 30, size[1] - 35)
        self.lbl_page_info_size = (50, 30)

        self.files_panel = pgu.elements.UIPanel(
            manager=self.manager,
            starting_layer_height=0,
            relative_rect=pg.Rect(self.dest, self.size))

        self.btn_page_back = pgu.elements.UIButton(
                relative_rect=pg.Rect(self.btn_page_back_dest, self.btn_page_back_size),
                text='Back',
                manager=self.manager, container=self.files_panel)

        self.btn_page_next = pgu.elements.UIButton(
                relative_rect=pg.Rect(self.btn_page_next_dest, self.btn_page_next_size),
                text='Next',
                manager=self.manager, container=self.files_panel)

        self.lbl_page_info = self.lbl_page_info = pgu.elements.UILabel(
                text="{}/{}".format(0, 0),
                manager=self.manager,
                container=self.files_panel,
                relative_rect=pg.Rect(self.lbl_page_info_dest, self.lbl_page_info_size))

        self.files_path = ""
        self.is_video_loaded = True
        self.is_page_loaded = True
        self.video_file_rows = []

    def load_file(self):
        if not self.is_video_loaded:
            self.video_file_rows = []

            result = [y for x in os.walk(self.files_path) for y in glob.glob(os.path.join(x[0], '*.mp4'))]

            for file_path in result:
                self.video_file_rows.append(VideoFileRow(file_path, self.row_size, self.manager, self.files_panel))

            self.set_page(0)
            self.last_page = int(len(self.video_file_rows) / self.page_size) + 1
            self.is_video_loaded = True

    def draw_page(self):
        if not self.is_page_loaded:
            row_page_ini = self.page * self.page_size
            row_page_end = ((self.page + 1) * self.page_size) - 1

            for i, video_file_row in enumerate(self.video_file_rows):
                if row_page_ini <= i < row_page_end:
                    video_file_row.draw((0, self.row_size[1] * (i - row_page_ini)))
                else:
                    video_file_row.kill()

            self.lbl_page_info.text = "{}/{}".format(self.page + 1, self.last_page)
            self.lbl_page_info.rebuild()

            self.is_page_loaded = True

    def set_files_path(self, _files_path):
        self.files_path = _files_path
        self.is_video_loaded = False

    def set_page(self, page=0):
        print("page = {}".format(page))
        self.page = page
        self.is_page_loaded = False

    def update(self, vm):

        self.load_file()
        self.draw_page()

        if self.btn_page_next.check_pressed():
            if self.page + 1 < self.last_page:
                self.set_page(self.page + 1)

        if self.btn_page_back.check_pressed():
            if self.page - 1 >= 0:
                self.set_page(self.page - 1)

        for video_file in self.video_file_rows:
            if video_file.is_draw:
                if video_file.load_button.check_pressed():
                    video_file.selected()
                    vm.load_video(video_file.path_video)
                else:
                    video_file.unselected()

