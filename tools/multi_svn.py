"""Multi-repository version control tools for Adv ProgBio"""

import os
import sys

def cl_do_all(command, workdirs):
    """Run the same command line argument from each working directory"""
    for workdir in workdirs:
        os.system("( cd %s ; %s)" % (workdir, command))
        
def update_all(workdirs):
    cl_do_all('svn update', workdirs)


repos = ['andy-kleinhesselink', 'bryan-dayton', 'erica-christensen',
         'jonathan-koch', 'martin-schilling', 'morgan-ernest', 'nancy-huntly',
         'paulwolf', 'zachary-portman']

workdir = '/home/ethan/Dropbox/Teaching/ProgBiol/Assignments/adv/'
workdirs = [workdir + repo for repo in repos]

if __name__ == '__main__':
    if sys.argv[1] == 'update':
        update_all(workdirs)
    else:
        print("Unknown command")