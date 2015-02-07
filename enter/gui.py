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
from efl.elementary.entry import Entry
from efl.elementary.icon import Icon
from efl.elementary.image import Image
from efl.elementary.label import Label
from efl.elementary.button import Button
from efl.elementary.progressbar import Progressbar


# session_image

# users_bt : users_bt_clicked_cb
# username_en : username_en_enter_cb

# password_bt : password_bt_clicked_cb
# password_en : password_en_enter_cb

class MainWin(StandardWindow):
    def __init__(self):
        # the window
        StandardWindow.__init__(self, 'enter', 'Enter')
        self.autodel_set(True)
        self.callback_delete_request_add(lambda o: self.close())

        # background win
        background = Background(self)
        background.file_set("bg_radgrad.png")
        background.size_hint_weight_set(evas.EVAS_HINT_EXPAND, evas.EVAS_HINT_EXPAND)
        self.resize_object_add(background)
        background.show()

        # main box ----------------------------------------------------
        box = Box(self,
                      size_hint_weight=(1, 1),
                      size_hint_align=(0, 0),
                      size_hint_min=(200, 52),
                      position=(0, 0)
                     )
        self.resize_object_add(box)
        box.show()

        # interface box -----------------------------------------------
        interface = Box(self,
                        size=(200, 320),
                        size_hint_min=(200, 320),
                        size_hint_weight=(1, 1),
                        size_hint_align=(0.50, 0.50),
                        padding=(0, 4)
                       )
        box.pack_end(interface)
        interface.show()

        # settings box (horizontal) -----------------------------------
        box = Box(self,
                  size_hint_weight=(1, 1),
                  size_hint_align=(0.50, 0.50),
                  size_hint_min=(200, 52),
                  padding=(0, 4)
                 )
        box.horizontal_set(True)
        interface.pack_end(box)
        box.show()

        # session & power button's(sub menu as inwin view)

        # desktop logo box --------------------------------------------
        box = Box(self,
                  size_hint_weight=(1, 1),
                  size_hint_align=(0.50, 0.50),
                  size_hint_min=(200, 52),
                  padding=(0, 4)
                 )
        interface.pack_end(box)
        box.show()

        # views the selected desktop logo
        session_image = Image(self)
        session_image.file_set("desktop_e.png")
        w, h = session_image.object_size_get()
        session_image.resize(w, h)
        box.pack_end(session_image)
        session_image.show()

        # username box (horizontal) -----------------------------------
        box = Box(self,
                  size_hint_weight=(1, 1),
                  size_hint_align=(0.50, 0.50),
                  size_hint_min=(200, 52),
                  padding=(4, 0)
                 )
        box.horizontal_set(True)
        interface.pack_end(box)
        box.show()

        users_bt = Button(self)
        users_bt.callback_clicked_add(self.users_bt_clicked_cb)
        box.pack_end(users_bt)
        users_bt.show()

        icon = Icon(self, size_hint_min=(24,24))
        icon.file_set("icon_system_users.png")
        users_bt.content = icon
        icon.show()

        username_en = Entry(self,
                            scrollable=True,
                            single_line=True,
                            size=(100, 20),
                            size_hint_min=(100, 20),
                            size_hint_weight=(1, 1),
                            size_hint_align=(0.50, 0.50)
                           )
        box.pack_end(username_en)
        username_en.show()

        # pasword box (horizontal) ------------------------------------
        box = Box(self,
                  size_hint_weight=(1, 1),
                  size_hint_align=(0.50, 0.50),
                  size_hint_min=(200, 52),
                  padding=(4, 0)
                 )
        box.horizontal_set(True)
        interface.pack_end(box)
        box.show()

        password_bt = Button(self)
        password_bt.callback_clicked_add(self.password_bt_clicked_cb)
        box.pack_end(password_bt)
        password_bt.show()

        icon = Icon(self, size_hint_min=(24,24))
        icon.file_set("icon_system_run.png")
        password_bt.content = icon
        icon.show()

        password_en = Entry(self,
                            scrollable=True,
                            single_line=True,
                            size=(100, 20),
                            size_hint_min=(100, 20),
                            size_hint_weight=(1, 1),
                            size_hint_align=(0.50, 0.50)
                           )
        box.pack_end(password_en)
        password_en.show()

        self.resize(600, 480)
        self.show()

    def users_bt_clicked_cb(self, bt):
        return True

    def password_bt_clicked_cb(self, bt):
        return True


if __name__ == "__main__":
    elementary.init()
    ui = MainWin()
    elementary.run()
    elementary.shutdown()


