import sys
import urllib
import urllib2
import json
import os
import subprocess
import re

for change in sys.argv[1:]:
    print change
    f = urllib2.urlopen('http://review.cyanogenmod.com/query?q=change:%s' % change)
    d = f.read()
    # gerrit doesnt actually return json. returns two json blobs, separate lines. bizarre.
    print d
    d = d.split('\n')[0]
    data = json.loads(d)
    project = data['project']

    plist = subprocess.Popen([os.environ['HOME']+"/bin/repo","list"], stdout=subprocess.PIPE)
    while(True):
        retcode = plist.poll()
        pline = plist.stdout.readline().rstrip()
        ppaths = re.split('\s*:\s*',pline)
        if ppaths[1] == project:
            project = ppaths[0]
            break
        if(retcode is not None):
            break

    print project
    number = data['number']
    patch_count = 0
    junk = number[len(number) - 2:]

    if not os.path.isdir(project):
        sys.stderr.write('no project directory: %s' % project)
        sys.exit(1)

    while 0 != os.system('cd %s ; git fetch http://review.cyanogenmod.com/%s refs/changes/%s/%s/%s' % (project, data['project'], junk, number, patch_count + 1)):
        patch_count = patch_count + 1

    while 0 == os.system('cd %s ; git fetch http://review.cyanogenmod.com/%s refs/changes/%s/%s/%s' % (project, data['project'], junk, number, patch_count + 1)):
        patch_count = patch_count + 1

    os.system('cd %s ; git fetch http://review.cyanogenmod.com/%s refs/changes/%s/%s/%s' % (project, data['project'], junk, number, patch_count))
    os.system('cd %s ; git merge FETCH_HEAD' % project)
