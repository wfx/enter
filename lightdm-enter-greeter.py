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

import os
import sys

from gi.repository import LightDM

from efl import ecore
from efl import ecore_x
from efl import elementary
from efl.utils.erigo import ErigoGui

prj_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "enter")
json_file = os.path.join(prj_path, "lightdm-enter-greeter.egui")

class Enter(ErigoGui):
    def __init__(self, *args, **kargs):
        ErigoGui.__init__(self, *args, **kargs)
        self.elm_win1.callback_delete_request_add(lambda o: elementary.exit())
        #self.elm_entry_username.text = ""
        self.elm_entry_username.focus = True
        #self.elm_entry_password.text = ""
        self.elm_entry_password.password = True

        ecore_x_win = ecore_x.Window_from_xid(self.elm_win1.xwindow_xid)
        ecore_x_win.focus()

        self.greeter = LightDM.Greeter()
        # connect signal handlers to LightDM
        self.greeter.connect ("authentication-complete", self.authentication_complete_cb)
        self.greeter.connect ("show-message", self.show_message_cb)
        self.greeter.connect ("show-prompt", self.show_prompt_cb)
        # connect to greeter
        self.greeter.connect_sync()


    def msg(self, txt):
        #debug helper
        self.elm_label1.text_set(txt)
        print(sys.stderr, txt)


    def elm_button_login_clicked_cb(self, btn):
        self._login_cb()


    def _login_cb(self):
        self.msg("login_cb: " + str(self.greeter.get_is_authenticated()))

        if self.greeter.get_is_authenticated():
            self.msg("user is already authenticated, starting session")
            start_session()
        elif self.greeter.get_in_authentication():
            self.msg("username was passed in already, send password to LightDM")
            self.greeter.respond(self.elm_entry_password.entry_get())
        else:
            self.msg("Initial entry of username, send it to LightDM")
            self.greeter.authenticate(self.elm_entry_username.entry_get())


    def show_prompt_cb(self, greeter, text, promptType):
        if promptType == LightDM.PromptType.SECRET:
            self.msg("show_prompt_cb: please enter password.")
            self.elm_entry_password.focus = True
        else:
            self.msg("show_prompt_cb: none password promt")



    # If LightDM sends a message back to the greeter, for example, "Login
    # failed" or "invalid password" we display it in our message box.
    def show_message_cb(self, text, message_type):
        self.msg("show_message_cb: " + str(message_type) + " -> " + text)


    def authentication_complete_cb(self, greeter):
        if self.greeter.get_is_authenticated():
            # API has ways to query available sessions, please see the docs.
            if not self.greeter.start_session_sync("enlightenment"):
                self.msg("authentication_complete_cb: Failed to start enlightenment")
            else:
                # user is authenticated, starting session
                self.msg("start session: " + str(self.greeter.start_session_sync("enlightenment")))
                self.greeter.start_session_sync("enlightenment")
        else:
            self.msg("authentication_complete_cb: login failed")


if __name__ == '__main__':
    elementary.init()
    app = Enter(json_file, verbose=True)
    ecore.main_loop_glib_integrate()
    elementary.run()
    elementary.shutdown()
