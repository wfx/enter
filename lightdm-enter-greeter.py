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
# API: https://lazka.github.io/pgi-docs/#LightDM-1
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
        self.elm_entry_username.text = ""
        self.elm_entry_username.focus = True
        self.elm_entry_password.text = ""
        self.elm_entry_password.password = True

        ecore_x_win = ecore_x.Window_from_xid(self.elm_win1.xwindow_xid)
        ecore_x_win.focus()

        # connect: LightDM
        self.greeter = LightDM.Greeter()
        self.greeter.connect ("authentication-complete", self.authentication_complete_cb)
        self.greeter.connect ("show-message", self.show_message_cb)
        self.greeter.connect ("show-prompt", self.show_prompt_cb)
        self.greeter.connect_sync()

        # system informations
        self.can_hibernate = LightDM.get_can_hibernate()
        self.can_restart = LightDM.get_can_restart()
        self.can_shutdown = LightDM.get_can_shutdown()
        self.can_suspend = LightDM.get_can_suspend()
        self.hostname = LightDM.get_hostname()
        self.language = LightDM.get_language()
        self.languages = {}
        for l in LightDM.get_languages():
            #self.languages.append(LightDM.Language.get_name(l))
            self.languages[LightDM.Language.get_code(l)] = \
                [{'name':LightDM.Language.get_name(l)},{'territory':LightDM.Language.get_territory(l)}]
        self.sessions = []
        for s in LightDM.get_sessions():
            self.sessions.append(LightDM.Session.get_key(s))
        self.users = []
        i = LightDM.UserList.get_instance()
        for u in LightDM.UserList.get_users(i):
            self.users.append(LightDM.User.get_name(u))


    def bt_login_clicked_cb(self, bt):
        self.login_cb()

    def tb_shutdown_cb(self, tb):
        self.system_shutdown()

    def tb_reboot_cb(self, tb):
        self.system_restart()

    def get_username(self):
        return self.elm_entry_username.entry_get()

    def get_password(self):
        return self.elm_entry_password.entry_get()

    def system_hibernate(self):
        if self.can_hibernate:
            LightDM.hibernate()
        else:
            self.log("system cannot hibernate!")

    def system_restart(self):
        if self.can_restart:
            LightDM.restart()
        else:
            self.log("system cannot restart!")

    def system_shutdown(self):
        if self.can_shutdown:
            LightDM.shutdown()
        else:
            self.log("system cannot shutdown!")

    def system_suspend():
        if self.can_suspend:
            LightDM.suspend()
        else:
            self.log("system cannot suspend!")

    def login_cb(self):
        self.log("login_cb: " + str(self.greeter.get_is_authenticated()))

        if self.greeter.get_is_authenticated():
            self.log("user is already authenticated, starting session")
            self.greeter.start_session_sync("enlightenment")
        elif self.greeter.get_in_authentication():
            self.log("username was passed in already, send password to LightDM")
            self.greeter.respond(self.get_password())
        else:
            self.log("Initial entry of username, send it to LightDM")
            self.greeter.authenticate(self.get_username())

    def show_prompt_cb(self, greeter, text, promptType):
        if promptType == LightDM.PromptType.SECRET:
            self.log("show_prompt_cb: please enter password.")
            self.elm_entry_password.focus = True
        else:
            self.log("show_prompt_cb: none password promt")

    # If LightDM sends a message back to the greeter, for example, "Login
    # failed" or "invalid password" we display it in our message box.
    def show_message_cb(self, text, message_type):
        self.log("show_message_cb: " + str(message_type) + " -> " + text)

    def authentication_complete_cb(self, greeter):
        if self.greeter.get_is_authenticated():
            # API has ways to query available sessions, please see the docs.
            if not self.greeter.start_session_sync("enlightenment"):
                self.log("authentication_complete_cb: Failed to start enlightenment")
            else:
                # user is authenticated, starting session
                self.log("start session: " + str(self.greeter.start_session_sync("enlightenment")))
                self.greeter.start_session_sync("enlightenment")
        else:
            self.log("authentication_complete_cb: login failed")

    def log(self, txt):
        #debug helper
        self.elm_label1.text_set(txt)
        #sys.stderr.write(txt)


if __name__ == '__main__':
    elementary.init()
    app = Enter(json_file, verbose=True)
    ecore.main_loop_glib_integrate()
    elementary.run()
    elementary.shutdown()
