#imports here
import cv2
import pytesseract
from gtts import gTTS
import osg

def take_picture(camera_index=0, file_name='img.png'):
    # grant camera access
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        return
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(file_name, frame)
        print("Image captured and saved as", file_name)
    else:
        print("Error: Couldn't capture frame from the camera.")
    cap.release()

    #image preprocessing
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = cv2.imread(file_name)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
    extracted_text = pytesseract.image_to_string(binary_image)
    language = 'en'

    #audio
    speech = gTTS(text=extracted_text, lang=language, slow=False)
    speech.save("audio.mp3")
    os.system("start audio.mp3")  # For Windows

#call func
take_picture()


