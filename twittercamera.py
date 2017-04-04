from twython import Twython from picamera import PiCamera from time import sleep

from auth import ( consumer_key, consumer_secret, access_token, access_token_secret, )

twitter = Twython( consumer_key, consumer_secret, access_token, access_token_secret, )

while True: name = input("What's your Name? ") twitterhandle = input("What's your Twitter handle? ") emailaddress = input("What's your Email address? ") postcode = input("What's your Postcode? ")

concatenated = name + ", " + twitterhandle + ", " + emailaddress + ", " + postcode

fh = open("data.csv","a")
fh.write(concatenated)
fh.write("\n")
fh.close() 

print("Nice to meet you " + name + "! Now... smile for the camera...in 3,2,1...!")
print("")
sleep(3)
camera = PiCamera()

message = twitterhandle + " Hi there! Here's some more information about Code Club www.codeclub.org.uk"

camera.start_preview()
sleep(3)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()
camera.close()

with open('/home/pi/image.jpg', 'rb') as photo:
    twitter.update_status_with_media(status=message, media=photo)
