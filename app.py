#import Qrcode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

#String  which represent the qr code
s = "www.iqsmartboost.com";

#Generate Qr Code
url = pyqrcode.create(s)

#create and save the png file nameing "myqr.png"
url.png("myqr.png", scale = 6)
