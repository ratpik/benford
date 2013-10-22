from fabric.api import env, local, require
from fabric.context_managers import lcd
import os

def analyze():
    pwd = os.getcwd()
    data_dir = os.path.join(pwd, 'data')
    files = os.listdir(data_dir)
    for f in files:
        x = dict()
        for i in xrange(1,10):
            
            x[i] = int(local("cat %s |awk '{print $NF}'|tr -sc [0-9] '\n'|sort -rn|grep ^%s|wc -l" %(os.path.join(data_dir,f), i), capture=True))
        
        print f
        print x
