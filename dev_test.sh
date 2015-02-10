#!/bin/sh
if ! grep -r -n -i --include=.gitignore "dev_test" 1> /dev/null
then
   echo "default settings"
   /usr/sbin/lightdm --test-mode --debug --config data/lightdm-efl-greeter.conf
else
   echo "write into dev_test"
   mkdir -p ./dev_test/{log,run,cache} 
   /usr/sbin/lightdm --test-mode --debug --log-dir ./dev_test/log --run-dir ./dev_test/run --cache-dir ./dev_test/cache --config data/lightdm-efl-greeter.conf 
fi

