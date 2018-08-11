import glob
import os
import time

class getFileTypes:
    def __init__(self):
        self.basePath = 'E:\Music2018\Music'
        self.artist = []
        self.albums = []
        self.fileStats = []
        self.files = []

    """
    for root, dirs, files in os.walk(".", topdown=False):
       for name in files:
          print(os.path.join(root, name))
       for name in dirs:
          print(os.path.join(root, name))
    """

        
    def fileTypeCounter(self,path='E:\Music2018\Music'):
        counts =   {}  
        files = glob.glob(os.path.join(path, "\*")) # get all files in path
        for root, dirs, files in os.walk(path):
            for name in files:
 #               print("File ", name)
                self.files.append(name)
#                print(os.path.join(root, name))
#            for name in dirs:
#                print("Directory ", name)
#                print(os.path.join(root, name))
        for file in self.files:
 #           if os.path.isfile(file):
                path_ext = os.path.splitext(file)
            #    if os.path.isfile(file):
                if path_ext[1] in counts:
                        counts[path_ext[1]] += 1
                else:
                    #
                        counts[path_ext[1]] = 1
#        print("File Extensions in:",os.path.abspath(path))         
#        for i in counts:
#                print(i,":", counts[i])
        return counts

    def fileTypeCounter2(self,path='E:\Music\Amazon MP3\Joe Henderson\The Elements'):
        counts =   {}  
        files = glob.glob(os.path.join(path, "*")) # get all files in path
        for file in files:
#            if os.path.isfile(file):
                print("X file is ", file)
                path_ext = os.path.splitext(file)
                print("path extension is ", path_ext)
                if path_ext[1] in counts:
                    counts[path_ext[1]] += 1
                else:
                    counts[path_ext[1]] = 1
        print("Path: ",os.path.abspath(path))         
#        for i in counts:
#                print(i,":", counts[i])
        return counts
    
    
#    def get_File_Split(self,path="."):
#        fileSplits=[]
#        for file in glob.glob(os.path.join(path,"*")):
#            print(file)
#            if os.path.isfile(file):
#                self.artist.append(os.path.split(file)[1])
#        return fileSplits
    
if __name__ == '__main__':
#    https://www.tutorialspoint.com/python/dictionary_get.htm
#    pathFiles = 'E:\Music\Amazon MP3\Joe Henderson\The Elements'
    pathFiles = 'E:\Music2018\Music'
    extension = ".mp3"
    fileObj = getFileTypes()
    result = fileObj.fileTypeCounter(pathFiles)
    print(result)
    dicItems = result.items()
    print(dicItems)
    print(result.keys())
    print(result.values())

#    for key, value in result:
#        print(key, value)
#        print(itm[0],itm[1])

    counts = fileObj.fileTypeCounter2(pathFiles)
    print("counts", counts)