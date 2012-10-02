"""Multi-repository version control tools for Adv ProgBio"""

import os
import sys

def cl_do_all(command, workdirs):
    """Run the same command line argument from each working directory"""
    for workdir in workdirs:
        os.system("( cd %s ; %s)" % (workdir, command))
        
def update_all(workdirs):
    """Update all repositories"""
    cl_do_all('svn update', workdirs)
    
def commit(message, workdirs):
    """Commit to all repositories"""
    cl_do_all('svn commit -m "%s"' % (message), workdirs)
    
def add_files(file_list, workdirs):
    """Add files to all repositories"""
    currentdir = os.getcwd()
    for eachfile in file_list:
        cl_do_all('cp %s/%s ./' % (currentdir, eachfile), workdirs)
        cl_do_all('svn add %s' % (eachfile), workdirs)

repos = ['andy-kleinhesselink', 'bryan-dayton', 'erica-christensen',
         'jonathan-koch', 'martin-schilling', 'morgan-ernest', 'nancy-huntly',
         'paulwolf', 'zachary-portman']

workdir = '/home/ethan/Dropbox/Teaching/ProgBiol/Assignments/adv/'
workdirs = [workdir + repo for repo in repos]

if __name__ == '__main__':
    if sys.argv[1] == 'update':
        update_all(workdirs)
    elif sys.argv[1] == 'add':
        file_list = sys.argv[2:]
        update_all(workdirs)
        add_files(file_list, workdirs)
    elif sys.argv[1] == 'commit':
        message = sys.argv[2]
        assert message, "You must include a commit message."
        update_all(workdirs)
        commit(message, workdirs)
    else:
        print("Unknown command")