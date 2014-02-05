__author__ = 'Mark Anthony Pequeras'
__software__ = 'Invictuz Online Game'
__year__ = '2013'
__python__ = '2.7'
__developers__ = 'CoreSEC Software Development Group'



open_buildDir = open('buildPath.swide','r').read()
from distutils.core import setup
import py2exe

# If you want to Edit this, Do it on 'Edit Custom' Instead.

# START DO NOT TOUCH!

options = {'py2exe': {
           'compressed':1,  
           'bundle_files': 2, 
           'dist_dir': open_buildDir,
           'dll_excludes': ['w9xpopen.exe'],
           }}
setup(console=['swideBuild.py'], options=options,zipfile=None)

# END DO NOT TOUCH!