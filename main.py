import cv2



# Loading the dataset into the model and create a classifier 
def load_dataset():
    dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    return dataset

#Chossing image to detect face

def Displayimage(img):
   # img = cv2.imread('face3.jpg') #reading an image in 2D-array Source Image  
    # frame_read , img = webcam.read()

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
   
 


#The Algorithm requires it to be gray scale 
def GrayScaleImage(Image):
    grayscaleImg = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    DetectFace(grayscaleImg , Image)
 

# def resize(img):
    
#     print('Original Dimensions : ',img.shape)
    
#     scale_percent = 40 # percent of original size
#     width = int(img.shape[1] * scale_percent / 100)
#     height = int(img.shape[0] * scale_percent / 100)
#     dim = (width, height)
    
#     # resize image
#     resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
#     #cv2.imshow("Image", resized)
   
#     print('Resized Dimensions : ',resized.shape)
#     grayscaleImg = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  

#     DetectFace(grayscaleImg , resized)
#     return resized
   
    
  



def DetectFace(grayscaleImg , ColoredImage):
    dataset = load_dataset()
    
    Image = grayscaleImg
    theCoordinates = dataset.detectMultiScale(grayscaleImg)
   
    def DrawRectangle(Image, coordinates):
        print(theCoordinates) 
        #Drawing Rectangle
        for (x, y, w, h) in theCoordinates:
            cv2.rectangle(Image, (x, y), (x + w, y + h), (255,255, 255, 10))
   
    DrawRectangle(ColoredImage, theCoordinates)
    cv2.imshow("Face Detector", ColoredImage)
    key = cv2.waitKey(1)
   
    print('Number of Faces Detected : ',len(theCoordinates))
    




webcam = cv2.VideoCapture(0) #capturing image from webcam
key = 0

while True:

    webcam = cv2.VideoCapture(0) #capturing image from webcam
    
    frame_read , img = webcam.read()
    Displayimage(img)
    if key== 81 or key == 113:
        break
  
    webcam.release()
   


