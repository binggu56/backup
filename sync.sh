#!/bin/sh
# Backup files from laptop to pople
rsync -r --partial --progress --rsh=ssh --max-size=10MB <local dir>  <remote host>:/home/bing/backup/
#tar -zvcf ifile.tgz ifile/
#mv ifile.tgz /Users/bing/Dropbox/


