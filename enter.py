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
        self.elm_win1.activate()
        self.elm_entry_username.focus = True
        self.elm_entry_password.password = True

        self.greeter = LightDM.Greeter()
        # connect signal handlers to LightDM
        self.greeter.connect ("authentication-complete", self.authentication_complete_cb)
        self.greeter.connect ("show-message", self.show_message_cb)
        self.greeter.connect ("show-prompt", self.show_prompt_cb)
        # connect to greeter
        self.greeter.connect_sync()

    def msg(self, txt):
        self.elm_label1.text_set(txt)


    def elm_button_login_clicked_cb(self, btn):
        self._login_cb()


    # This elm signal is called when the user hits enter after entering a
    # username/password or clicks the login button.  Since we re-purposed
    # the text entry box, we have 3 possible cases to handle here.
    # 1) the user is already authenticated, if for example, they don't have
    #  a password set.
    # 2) The username has been passed into LightDM and now we need to pass
    #  the password
    # 3) The username has been entered, but not passed in.  We pass it in
    #  and start the authentication process.
    def _login_cb(self):
        if self.greeter.get_is_authenticated():
            # user is already authenticated, starting session
            start_session()
        elif self.greeter.get_in_authentication():
            # username was passed in already, send password to LightDM
            self.greeter.authenticate(self.elm_entry_password.entry_get())
        else:
            # Initial entry of username, send it to LightDM
            self.greeter.authenticate(self.elm_entry_username.entry_get())


    # The show_prompt callback is oddly named, but when you get this
    # callback you are supposed to send the password to LightDM next.  In
    # our example, we re-purpose the prompt and ask the user for the
    # password which is then sent the next time the user hits the Login
    # button or presses enter.
    def show_prompt_cb(greeter, text, promptType):
        self.msg(text)

        # clear the text entry box so the user can enter the password
        self.msg("clear the text entry box so the user can enter the password")

        print(sys.stderr, "prompt type: " + str(promptType))
        # if this is a password prompt, we want to hide the characters
        if promptType == LightDM.PromptType.SECRET:
            self.msg("password promt")
        else:
            self.msg("none password promt")


    # If LightDM sends a message back to the greeter, for example, "Login
    # failed" or "invalid password" we display it in our message box.
    def show_message_cb(text, message_type):
        self.msg("get message: ", text)


    # Callback for after we send LightDM the password, this method
    # has to handle a successful login, in which case we start the session
    # or a failed login, in which case we tell the user
    def authentication_complete_cb(greeter):
        if greeter.get_is_authenticated():
            # For our simple example we always start Unity-2d.  The LightDM
            # API has ways to query available sessions, please see the docs.
            if not greeter.start_session_sync("enlightenment"):
                self.msg("Failed to start enlightenment")
        else:
            self.msg("Login failed")


if __name__ == '__main__':
    elementary.init()
    app = Enter(json_file, verbose=True)
    elementary.run()
    elementary.shutdown()
