Enter
===
A lightdm elm greeter for e
![Screenshot](https://github.com/wfx/enter/blob/master/data/shot.jpg)

## Requirements ##

* Python 3
* Python-EFL 1.14 or higher
* PyGObject
* accountsservice
* a running lightdm installation

## Installation ##

* For system-wide installation (needs administrator privileges):

 `(sudo) python setup.py install`

* Install in a custom location:

 `python setup.py install --prefix=/MY_PREFIX`

* Setup lightdm:
 `open /etc/lightdm/lightdm.conf and add:
 `greeter-session=lightdm-efl-greeter

## Uninstall ##

* For system.wide deinstallation (need administrator privileges):

 `(sudo) python setup.py uninstall`

## License ##

GNU General Public License v3 - see LICENSE
