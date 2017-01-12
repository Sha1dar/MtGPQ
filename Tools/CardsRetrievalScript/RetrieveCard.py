import urllib.request
import urllib
import os

KaladeshURL = "https://d3go.com/wp-content/uploads/cards/mtgpq/5gf85x9f_kaladesh/"
KaladeshFolder = "Kaladesh"

CurrentImageSetURL = KaladeshURL
CurrentImageFolder = KaladeshFolder


#Create the appropriate directories
if not os.path.exists(CurrentImageFolder):
    os.makedirs(CurrentImageFolder)

#Retrieve the html code as string
req = urllib.request.Request(CurrentImageSetURL, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
inputString = html.decode('ascii')


#Iterate over the html string in order to substract the corrent card name, download it and save it
while True:
    try:
        firstPngIndex = inputString.index(".png")
        secondPngIndex = inputString.index(".png", firstPngIndex+1)
    except ValueError:
        print("No more occurance")
        break

    
    startingIndex = firstPngIndex + 7
    endingIndex = secondPngIndex + 4
    imageName = inputString[startingIndex:endingIndex]
    imageURL = CurrentImageSetURL + imageName
    inputString = inputString[endingIndex:len(inputString)]
    
    imageReq = urllib.request.Request(imageURL, headers={'User-Agent': 'Mozilla/5.0'})
    imageData = urllib.request.urlopen(imageReq).read()
    localImagePath = CurrentImageFolder + "/" + imageName

    imageFile = open(localImagePath, 'wb')
    imageFile.write(imageData)

    print(imageName + " Downloaded")
    
