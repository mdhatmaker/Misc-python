from os import *
import shutil

startDir = "/users/michael/Downloads/Books - rapid"

dirs = listdir(startDir)
for d in dirs:
        srcDir = startDir + "/" + d
        if path.isdir(srcDir): 
            destDir = startDir
            print srcDir
            files = listdir(srcDir)
            print len(files), "file(s)"
            for f in files:
                src = srcDir + "/" + f
                dst = destDir + "/" + f
                shutil.move(src, dst)
            rmdir(srcDir)            
