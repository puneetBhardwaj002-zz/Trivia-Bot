import pytesseract
import pyscreenshot as pysc
from PIL import Image , ImageEnhance
import cv2
#import numpy as np
#import webbrowser
import threading
term=""
def getText(t,l,w,h,x):
    global term    
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    im = pysc.grab(bbox=(t,l,w,h))
    im.save('sc'+ str(x) +'.png',dpi=(300,300))
    img = cv2.imread('sc'+ str(x) +'.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imwrite('sc'+ str(x) +'.png',gray)
    text = pytesseract.image_to_string(Image.open('sc'+ str(x) +'.png'),lang='eng')
    term = term + "  " + text.encode("utf-8")


if __name__ == '__main__':
    t1=threading.Thread(target=getText,args=(45,468,290,520,1))
    t2=threading.Thread(target=getText,args=(45,327,290,380,2))
    t3=threading.Thread(target=getText,args=(45,399,290,449,3))
    t4=threading.Thread(target=getText,args=(18,190,346,282,0))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    #url = "https://www.google.com.tr/search?q={}".format(term)
    #webbrowser.open_new_tab(url)
    term=[x for x in term.split("  ")]
    m=0
    for i in range(len(term)):
        if len(term[i]) > len(term[m]):
            m=i
    q=term[m]
    q=q.replace('\n',' ')
    print(q)