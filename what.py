from PIL import Image
import pytesseract

def addJPG():
    picture = Image.open('/home/jolteon/Desktop/raw-manga.jpg')
    picture.show()
    
def readJPG():
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    print(pytesseract.image_to_string('/home/jolteon/Desktop/c.png'))
    
if __name__ == '__main__':
    readJPG()
