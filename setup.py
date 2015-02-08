#!/usr/bin/env python
from distutils.core import setup
from efl.utils.setup import build_extra, build_i18n, build_edc, uninstall


setup(
    name = 'lightdm-efl-greeter',
    version = '0.0.1',
    description = 'A LightDM greeter for the EFL',
    license="GNU General Public License v3 (GPLv3)",
    author = 'Wolfgang Morawetz (wfx) & Davide Andreoli (davemds)',
    author_email = 'wolfgang.morawetz@gmail.com',
    url="https://github.com/wfx/enter",
    requires = ['efl (>= 1.13)'],
    scripts = ['bin/lightdm-efl-greeter'],
    data_files = [
        ('/usr/share/xgreeters', ['data/desktop/lightdm-efl-greeter.desktop']),
    ],
    cmdclass = {
        'build': build_extra,
        'build_edc': build_edc,
        # 'build_i18n': build_i18n,
        'uninstall': uninstall,
    },
    command_options={
        'install': {
            'record': ('setup.py', 'installed_files.txt'),
            'prefix': ('setup.py', '/usr')
        }
    },
)


# Reference:
# https://lazka.github.io/pgi-docs/#LightDM-1
# http://www.mattfischer.com/blog/?p=5
# http://people.ubuntu.com/~robert-ancell/lightdm/reference/
# https://wiki.ubuntu.com/LightDM
