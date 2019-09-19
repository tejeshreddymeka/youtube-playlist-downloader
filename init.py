import re
import urllib.request
from urllib.parse import unquote
import os

def getUrlsAndFileNames():
    urls = []
    try:
        with open('downloadUrls.txt','r') as urlsFile:
                for url in urlsFile:
                    fileName = unquote(url.split('title=')[1]).replace("\n","").replace(".","_").replace(" ","_").replace(":","_")
                    urls.append((url,fileName))
    except:
        print("\n[-] Error: Problem with downloadUrls.txt....! Please make sure it exists and urls that you paste is proper.\n")
    return urls

def downloadVedioFromUrl(url, folderPath, fileName, extension):
    try:
        print("Downloading {}".format(fileName))
        filePath = folderPath + "/" + fileName + "_" +  extension
        urllib.request.urlretrieve(url, filePath)
        return True
    except:
        print("\n[-] Error: Make sure that urls that you paste is proper.\n")
        return False

if __name__ == "__main__":
    print("\t\t Youtube Playlist Downloader")
    print("\t\t-----------------------------\n\n");
    folderPath = input("Enter the destination folder path: ")
    extension = ".mp4"
    
    if( os.path.isdir( folderPath ) ):
        count = 0
        for url, fileName in getUrlsAndFileNames():
            if(downloadVedioFromUrl(url, folderPath, fileName, extension)):
                count+=1
            print("[+] Downloaded {} items....!\n".format(count))
    else:
        print(" Destination folder is Invalid...!")

