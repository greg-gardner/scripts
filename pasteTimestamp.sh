#!/bin/bash
date +"%Y.%M.%d %H:%M" | while read line; do echo -n "$line"; done | xclip -i -selection clipboard
