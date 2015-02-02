#!/usr/bin/env python
# encoding: utf-8

import os
import sys

#from gi.repository import GObject
#from gi.repository import GLib
from gi.repository import LightDM

from efl import elementary
from efl.utils.erigo import ErigoGui

prj_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui")
json_file = os.path.join(prj_path, "enter.egui")

class Enter(ErigoGui):
    def __init__(self, *args, **kargs):
        ErigoGui.__init__(self, *args, **kargs)
        self.elm_win1.callback_delete_request_add(lambda o: elementary.exit())
        self.greeter = LightDM.Greeter()


    def elm_button_login_clicked_cb(self, btn):
        self._login_cb()


    def _login_cb(self):
        print (sys.stderr, "login_cb")
        if self.greeter.get_is_authenticated():
            # user is already authenticated, starting session
            start_session()
        elif self.greeter.get_in_authentication():
            # username was passed in already, send password to LightDM
            self.greeter.authenticate(self.elm_entry_password.entry_get())
        else:
            # Initial entry of username, send it to LightDM
            self.greeter.authenticate(self.elm_entry_username.entry_get())


if __name__ == '__main__':
    elementary.init()
    app = Enter(json_file, verbose=True)
    elementary.run()
    elementary.shutdown()
