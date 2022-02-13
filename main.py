# Author : Prakriti Regmi 
# A simple Face Counter Application made using open cv and Haarcascade algorithm

import cv2

# Loading the dataset into the model and create a classifier 
def load_dataset():
    dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    return dataset

#Chosing the current frame  to detect face

def DisplayFrameData(img):
 
    # get dimensions of image
    dimensions = img.shape
    
    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    
    print('Image Dimension    : ',dimensions)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)
    
    #Grayscale the Frame 
    
    GrayScaleImage(img)
   
 


#Function to conver the captured frame in to grayscale  
def GrayScaleImage(Image):
    grayscaleImg = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    DetectFace(grayscaleImg , Image)
 
#Function to detect the face in the captured frame
def DetectFace(grayscaleImg , ColoredImage):
    
    dataset = load_dataset()
    
    Image = grayscaleImg
    theCoordinates = dataset.detectMultiScale(grayscaleImg)
    # the type of font
    # to be used.
    font = cv2.FONT_HERSHEY_SIMPLEX
    def DrawRectangle(Image, coordinates):
        print(theCoordinates) 
        #Drawing Rectangle and writing the result in text 
        for (x, y, w, h) in theCoordinates:
            cv2.rectangle(Image, (x, y), (x + w, y + h), (255,255, 255, 10))
            cv2.putText(Image,("Faces Recognized : "+ str(len(theCoordinates))),(50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
   
    DrawRectangle(ColoredImage, theCoordinates)
    cv2.imshow("Face Detector", ColoredImage)
   
    print(key)
   # print('Number of Faces Detected : ',len(theCoordinates))
 
   
    



while True:
    # Capture the frame from the default camera
    webcam = cv2.VideoCapture(0) 
    key = 0
    frame_read , img = webcam.read()
    
    DisplayFrameData(img)
    key = cv2.waitKey(9)
    if key== 81 or key == 113:
        # close all windows
        cv2.destroyAllWindows()
        webcam.release()
        print("App Terminated")
        break
  
    
   


