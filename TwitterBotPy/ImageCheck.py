import os
import time
import TwitterBot
import DetectChanges

TxtFile = "Uplaoded.txt"
ImgDir = "Images"

#Creates a Folder and the text file If it doesn't Exist
def FileCreate():
    print("File Created!")
    if not os.path.exists(ImgDir) and ImgDir not in os.getcwd():
        os.mkdir(ImgDir)
        os.chdir(ImgDir)
    else:
        if ImgDir not in os.getcwd():
            os.chdir(ImgDir)
    if not os.path.exists(TxtFile):
        Uplaoded = open(TxtFile,"x")
        Uplaoded.close()

#Checks if the image is already Uplaoded or Not and returns a list of new Images
def ImageCh():
    print("Image Started")
    CheckUplaoded = open(TxtFile,"r+")
    UplaodedList = set()

    UplaodedList = CheckUplaoded.read().split(",")

    for img in os.listdir():
        if img.endswith(".png") and img not in UplaodedList:
            CheckUplaoded.write(img+",")
            print("new image!")
            time.sleep(3)
    CheckUplaoded.close()
    DetectChanges.CheckForChanges()

if __name__ == "__main__":
    ImageCh()
    FileCreate()
