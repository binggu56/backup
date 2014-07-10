#!/usr/bin/python


import time,os,sys

def check(dir):
    """
        check if the file exist or not.
    """
    if not os.path.exists(dir):
        sys.exit('The file does not exist.')
    else:
        print("%s will be backuped." %(dir))

def bak2remote(source,remote):

    remote=str(input('what is the name for remmote host\n'))
    target_dir = input('directory you want to put in remote host')
    target = target_dir+time.strftime('%Y%m%d') + '.tar.gz'
    command = 'tar zcvpf - %s | ssh %s "cat > %s"' %(source,remote,target)
    if os.system(command) == 0:
        print('Successful backup to %s:%s',%(remote,target_dir))
    else:
        print('Backup failed.')

def bak2local(source):
        target_dir = str(input('where to put your backup:'))
        name = input('name your backup: ')
        target=target_dir+name+time.strftime('%Y%m%d') + '.tgz'
#        limit = input('Do you want to limit the file size?')
#        cmd = 'tar -cvzf %s %s'%(target,source)
        cmd = 'find %s -type f -size -1024k | xargs tar -cvzf  %s'%(source,target)
        if os.system(cmd) == 0:
            print("Max-size = 1M. \n Successful backup to %s" %(target_dir))
        else:
            print('Backup failed.')


while True:
    try:
        dest=int(input('Where to backup: 1) remote 2) local\n'))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        
while True:
    try:
        todo=int(input('What to do: 1) UPLOAD 2) DOWNLOAD\n'))
        src=input('PATH TO SOURCE: ')
        break
    except ValueError:
        print("Oops!  That was no valid path.  Try again...")

#for arg in sys.argv[1:]:
check(src)
if dest==1 and todo==1:

    bak2remote(arg,remote)
elif dest==2 and todo==1:
    bak2local(src)

#source = sys.argv[1]

# If you are using Windows, use source = [r'C:\Documents', r'D:\Work']
