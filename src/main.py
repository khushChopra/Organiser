import sys, os, shutil
from pprint import pprint
from datetime import datetime

# get target folder
destination = os.path.abspath(os.path.join(os.getcwd(), sys.argv[1]))
print("Cleaning directory -",destination)

# get all non folder items from folder
items = os.listdir(destination)
files = [x for x in items if os.path.isfile(os.path.abspath(os.path.join(destination, x))) and x[0]!='.' and os.path.abspath(os.path.join(destination, x))!=os.path.abspath(os.path.join(os.getcwd(), sys.argv[0]))]  # also remove hidden files and omit self

# get all seperate extensions
extensions = [os.path.splitext(x)[1] for x in files if os.path.splitext(x)[1] != ""]
extensions = list(set(extensions))

# make all such folders (add some subscript is necessary)
path = os.path.abspath(os.path.join(destination, "Organiser-"+str(datetime.date(datetime.now()))))
try:
    os.mkdir(path)
except FileExistsError: 
    print("Folder already exist you have done cleaning today")
    sys.exit()
for extension in extensions:
    os.mkdir(os.path.abspath(os.path.join(path, extension[1:])))

# move all relevant files to corresponding folder
for aFile in files:
    if os.path.splitext(aFile)[1] in extensions:
        oldLocation = os.path.abspath(os.path.join(destination, aFile))
        newLocation = os.path.abspath(os.path.join(path, os.path.splitext(aFile)[1][1:], aFile))
        shutil.move(oldLocation,newLocation)