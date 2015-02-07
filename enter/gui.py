#!/usr/bin/env python
# encoding: utf-8
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, print_function, unicode_literals

import os

from efl import ecore
from efl import evas
from efl import elementary
from efl.evas import EXPAND_BOTH, EXPAND_HORIZ, EXPAND_VERT, FILL_BOTH, FILL_HORIZ, FILL_VERT
from efl.elementary.background import Background
from efl.elementary.window import StandardWindow, DialogWindow
from efl.elementary.box import Box
from efl.elementary.ctxpopup import Ctxpopup
from efl.elementary.entry import Entry
from efl.elementary.icon import Icon
from efl.elementary.image import Image
from efl.elementary.label import Label
from efl.elementary.frame import Frame
from efl.elementary.genlist import Genlist, GenlistItemClass, ELM_GENLIST_ITEM_TREE
from efl.elementary.button import Button
from efl.elementary.table import Table
from efl.elementary.check import Check
from efl.elementary.fileselector_button import FileselectorButton
from efl.elementary.fileselector import Fileselector
from efl.elementary.popup import Popup
from efl.elementary.progressbar import Progressbar
from efl.elementary.separator import Separator



class MainWin(StandardWindow):
    def __init__(self):
        # the window
        StandardWindow.__init__(self, 'enter', 'Enter')
        self.autodel_set(True)
        self.callback_delete_request_add(lambda o: self.exit())

        # background
        background = Background(self)
        self.resize_object_add(background)
        background.file_set("bg_radgrad.png")
        background.size_hint_weight_set(evas.EVAS_HINT_EXPAND, evas.EVAS_HINT_EXPAND)
        background.show()

        # main box
        main_bx = Box(self, size_hint_weight=EXPAND_BOTH)
        self.resize_object_add(main_bx)
        main_bx.show()

        # settings box (horizontal)
        settings_bx = Box(self, size_hint_weight=EXPAND_BOTH)
        settings_bx.horizontal_set(True)
        main_bx.pack_end(settings_bx)
        settings_bx.show()

        # desktop logo box
        desktop_logo_bx = Box(self, size_hint_weight=EXPAND_BOTH)
        main_bx.pack_end(desktop_logo_bx)
        desktop_logo_bx.show()

        # desktop logo image
        session_image = Image(self)
        session_image.file_set("desktop_e.png")
        w, h = session_image.object_size_get()
        session_image.resize(w, h)
        desktop_logo_bx.pack_end(session_image)
        session_image.show()


        # username box (horizontal)
        username_bx = Box(self, size_hint_weight=EXPAND_BOTH)
        username_bx.horizontal_set(True)
        main_bx.pack_end(username_bx)
        username_bx.show()

        # button users
        bt_users = Button(self, text=('Users'))
        #bt_users.callback_clicked_add( show inwin list of users )
        username_bx.pack_end(bt_users)
        bt_users.show()

        icon = Icon(self, size_hint_min=(24,24))
        icon.file_set("icon_system_users.png")
        bt_users.content = icon
        icon.show()

        # entry usersername
        en_username = Entry(self,
                            editable=True, scrollable=True,single_line=True,
                            size_hint_min=(100, 20),size_hint_weight=EXPAND_BOTH, size_hint_align=FILL_BOTH)
        username_bx.pack_end(en_username)
        en_username.show()

        # box pasword (horizontal)
        bx_pasword = Box(self, size_hint_weight=EXPAND_BOTH)
        bx_pasword.horizontal_set(True)
        bx_pasword.pack_end(main_bx)
        bx_pasword.show()

        # button password
        bt_password = Button(self, text=('Login'))
        #bt_password.callback_clicked_add( execute login )
        bx_pasword.pack_end(bt_password)
        bt_password.show()

        icon = Icon(self, size_hint_min=(24,24))
        icon.file_set("icon_system_run.png")
        bt_password.content = icon
        icon.show()

        # entry password
        en_password = Entry(self,
                            editable=True, scrollable=True,single_line=True,
                            size_hint_min=(100, 20),size_hint_weight=EXPAND_BOTH, size_hint_align=FILL_BOTH)
        bx_pasword.pack_end(en_password)
        en_password.show()

        self.resize(600, 480)
        self.show()



if __name__ == "__main__":
    elementary.init()
    ui = MainWin()
    elementary.run()
    elementary.shutdown()


