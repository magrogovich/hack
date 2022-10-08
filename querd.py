from random import*
import time


test = True
while test == True:
    lat = uniform(-90.0, 90.0)
    lng = uniform(-180.0, 180.0)
    speed = randint(0,100)
    sat = randint(0,10)	
    with open("coordinates.txt", "w") as data:
        data.write(f"{lat}\n{lng}\n{speed}\n{sat}\n")
        print(f"{lat} {lng} {speed} {sat}\n")

    time.sleep(1)



