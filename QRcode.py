#pip install qrcode

#get display the given message

import qrcode
# qr = qrcode.make("Hello....Welcome to Mr.Praveen Mittakadapala")
# data = "https://www.youtube.com/results?search_query=python+life+channel"
#  qr.save("docpy.jpg")
# qr = qrcode.make(data)
# qr.save("pythonlife.jpg")
# qr.show()

qr = qrcode.QRCode(version=5,
                   box_size=5,
                   border=2)

name=input("enter your name:")
age=int(input("enter your age:"))
email=input("enter your email:")
mobileNo=int(input("enter your mobileNo:"))

data={"Name":name,"Age":age,"Email":email,"MobileNO":mobileNo}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("purple-flower-2212075.jpg")
img.show()
