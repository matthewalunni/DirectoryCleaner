import shutil

from os import listdir
from os import mkdir
from os.path import isfile, join, exists

directoryPath = "C:\\Users\\matth\\Desktop"
typeAndFolder = {
  "jpg": "Images",
  "png": "Images",
  "jpeg": "Images",
  "bmp": "Images",
  "ico": "Images",
  "pdf": "PDFs",
  "doc": "Office",
  "docx": "Office",
  "xls": "Office",
  "xlsx": "Office",
  "xlsm": "Office",
  "xltx": "Office",
  "xltm": "Office",
  "ppt": "Office",
  "pptx": "Office",
  "pptm": "Office",
  "ppsm": "Office",
  "accdb": "Office",
  "accde": "Office",
  "accdt": "Office",
  "accdr": "Office",
  "pub": "Office",
  "xps": "Office",
  "zip": "Zip"
}

def main():
    onlyfiles = [f for f in listdir(directoryPath) if isfile(join(directoryPath, f))]
    #printAList(onlyfiles)
    for file in onlyfiles:
      try:
        moveAFile(directoryPath + "\\" + file, directoryPath + "\\" + getFileType(file))
        pass
      except Exception as e:
        print(str(e))
        pass
      

#this method returns the type of a file
def getFileType(fileName):
    result = fileName.split('.')
    return result[-1]


# this method moves a file from location fromFile to location toFile
# this first will check if a directory exists, and if it does not, then it will create it
def moveAFile(fromFile, toFile):
  fileType = getFileType(fromFile)
  if not exists(directoryPath + "\\" + fileType) and typeAndFolder.__contains__(fileType):
    mkdir(directoryPath + "\\" + fileType)
  
  shutil.move(fromFile, toFile)

# this function prints a list to the console
def printAList(aList):
    for element in aList:
        print(element)



if __name__ == '__main__':
    main()


