#!/usr/bin/bash
unset YOUR_NAME

CONFIG=/etc/my-first-program.conf

[ -f $CONFIG ] && . $CONFIG

[ ! -z "$YOUR_NAME" ] && echo -en "Hello, ${YOUR_NAME}."
echo "This is a very simple shell script as an example of a packaged program."

