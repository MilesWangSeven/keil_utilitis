import sys
import os
from hashlib import md5, sha1
from zlib import crc32
import os
import time
import shutil

def get_filename_modifyTime(filename):
    time.ctime(os.stat(filename).st_mtime)
    time.ctime(os.stat(filename).st_ctime)
    time.localtime(os.stat(filename).st_mtime)
     
    ModifiedTime=time.localtime(os.stat(filename).st_mtime)
    # y=time.strftime('%Y', ModifiedTime)
    # m=time.strftime('%m', ModifiedTime)
    # d=time.strftime('%d', ModifiedTime)
    # H=time.strftime('%H', ModifiedTime)
    # M=time.strftime('%M', ModifiedTime)
    # S=time.strftime('%S', ModifiedTime)
    return time.strftime('%y%m%d_%H%M%S', ModifiedTime)

def getMd5(filename):
    mdfive = md5()
    with open(filename, 'rb') as f:
        mdfive.update(f.read())
    return mdfive.hexdigest()

def getSha1(filename):
    sha1Obj = sha1()
    with open(filename, 'rb') as f:
        sha1Obj.update(f.read())
    return sha1Obj.hexdigest()

def getCrc32(filename):
    with open(filename, 'rb') as f:
        return crc32(f.read()) & 0xffffffff

def get_filePath_Name_Ext(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath, shotname, extension

def print_fmt(str):
    print("\r\n ")
    print("{}".format(str))
    print("\r\n ")

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) <= 2:
        print_fmt("Warn: No file to convert!")
        return 1    

    fileDir = argv[1]
    if os.path.isdir(fileDir) == False:
        print_fmt("Error: The path is not correct!")
        return -1        
    releaseDir = os.path.join(fileDir,'AdvancedRelease')
    if os.path.isdir(releaseDir) == False:
        print_fmt("Create directory {}".format(releaseDir))
        os.mkdir(releaseDir)

    for filename in argv[2:]:
        filename = os.path.join(fileDir,filename)
        if os.path.isfile(filename):
            filepath, shotname, extension = get_filePath_Name_Ext(filename)
            crc32 = "{:08X}".format(getCrc32(filename))
            time_str = get_filename_modifyTime(filename)
            dst_filename = "{}_{}_{}{}".format(shotname, time_str, crc32, extension)
            shutil.copyfile(filename, os.path.join(releaseDir, dst_filename))
        else:
            print_fmt("Error: the file below is not exist!\r\n{}".format(filename))
            return -1    
    return 0

if __name__ == "__main__":
    sys.exit(main())