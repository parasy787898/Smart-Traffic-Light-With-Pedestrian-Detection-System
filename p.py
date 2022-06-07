from sqlite3 import Time
from turtle import st
import pygame
import random
from os import path
import time
import shelve
from os import path
from PIL import Image, ImageTk
import yolov5.det as detect

custom = path.join(path.dirname(__file__), "admin","custom")
input=file=path.join(path.dirname(__file__),"yolov5-master","test")
out=file=path.join(path.dirname(__file__),"yolov5-master","lib","test")

try:
    score_file = shelve.open(custom)   
    avg_light_vehicle_time= score_file['avg_light_vehicle_time']         
    avg_heavy_vehicle_time= score_file['avg_heavy_vehicle_time']         
    no_of_lanes= score_file['no_of_lanes']
    yellow_default_time=score_file['inital_default_time']
    max_green_time=score_file['max_green_time']
    mini_green_time=score_file['mini_green_time']
    pedes=score_file['pedes']


except:
    score_file = shelve.open(custom)   
    score_file['avg_light_vehicle_time']=5
    score_file['avg_heavy_vehicle_time']=10
    score_file['no_of_lanes']=2
    score_file['inital_default_time']=5
    score_file['max_green_time']=150
    score_file['mini_green_time']=20
    score_file['pedes']=1
    score_file.close()
    avg_light_vehicle_time=5
    avg_heavy_vehicle_time=10
    no_of_lanes=2
    yellow_default_time=5
    max_green_time=150
    mini_green_time=20
    pedes=1

v7=path.join(path.dirname(__file__),"yolov5","test","v7.jpg")
v6=path.join(path.dirname(__file__),"yolov5","test","v6.jpg")
v5=path.join(path.dirname(__file__),"yolov5","test","v5.jpg")
v4=path.join(path.dirname(__file__),"yolov5","test","v4.jpg")
v3=path.join(path.dirname(__file__),"yolov5","test","v3.jpg")
v2=path.join(path.dirname(__file__),"yolov5","test","v2.jpg")
v1=path.join(path.dirname(__file__),"yolov5","test","v1.jpg")

l3=path.join(path.dirname(__file__),"yolov5","test","l3.png")
l2=path.join(path.dirname(__file__),"yolov5","test","l2.png")
l1=path.join(path.dirname(__file__),"yolov5","test","l1.png")

i3=path.join(path.dirname(__file__),"yolov5","test","i3.jpg")
i2=path.join(path.dirname(__file__),"yolov5","test","i2.jpg")
i1=path.join(path.dirname(__file__),"yolov5","test","i1.jpg")


pygame.init()
#used to initialize the pygame module.    

#Creating a window for our game.
app = pygame.display.set_mode((1920,1020))
pygame.display.set_caption("App")

#loading images form my storage location.

bg = pygame.image.load(path.join(path.dirname(__file__), "i.png"))

#bg = pygame.transform.scale(bg, (500, 500))


red=(255,0,0)
green=(0, 255, 0)
yellow=(255,255,0)
black=(0,0,0)
white=(255,255,255)
pic_loop=0
pedes_loop=0
pedes_time=200
def images(ti,l,ar):
  app.fill(white)
  app.blit(bg, (0, 100))
    

  if l==0:
    pygame.draw.circle(app, red,[128, 380], 57, 0)
    pygame.draw.circle(app, red,[435, 380], 57, 0)
    pygame.draw.circle(app, red,[750, 380], 57, 0)
    pygame.draw.circle(app, red,[1073, 380], 57, 0)

  if l==1:
    if ti>yellow_default_time:
      pygame.draw.circle(app, green,[128, 720], 57, 0)
    else:
      pygame.draw.circle(app, yellow,[128, 550], 57, 0)


    pygame.draw.circle(app, red,[435, 380], 57, 0)
    pygame.draw.circle(app, red,[750, 380], 57, 0)
    pygame.draw.circle(app, red,[1073, 380], 57, 0)

  if l==2:
    pygame.draw.circle(app, red,[128, 380], 57, 0)
    if ti>yellow_default_time:
      pygame.draw.circle(app, green,[435, 720], 57, 0)
    else:
      pygame.draw.circle(app, yellow,[435, 550], 57, 0)

    pygame.draw.circle(app, red,[750, 380], 57, 0)
    pygame.draw.circle(app, red,[1073, 380], 57, 0)

  if l==3:
    pygame.draw.circle(app, red,[128, 380], 57, 0)
    pygame.draw.circle(app, red,[435, 380], 57, 0)
    if ti>yellow_default_time:
      pygame.draw.circle(app, green,[750, 720], 57, 0)
    else:
      pygame.draw.circle(app, yellow,[750, 550], 57, 0)
    
    pygame.draw.circle(app, red,[1073, 380], 57, 0)

  if l==4:
    pygame.draw.circle(app, red,[128, 380], 57, 0)
    pygame.draw.circle(app, red,[435, 380], 57, 0)
    pygame.draw.circle(app, red,[750, 380], 57, 0)
    if ti>yellow_default_time:
      pygame.draw.circle(app, green,[1073, 720], 57, 0)
    else:
      pygame.draw.circle(app, yellow,[1073, 550], 57, 0)
  
  if l==5:
    pygame.draw.circle(app, red,[128, 380], 57, 0)
    pygame.draw.circle(app, red,[435, 380], 57, 0)
    pygame.draw.circle(app, red,[750, 380], 57, 0)
    pygame.draw.circle(app, red,[1073, 380], 57, 0)
    font = pygame.font.SysFont("Times new Roman", 54)  
    app.blit(font.render("Time:"+str(ti)+"sec", True, black),[750,50]) 
    app.blit(pygame.transform.scale(pygame.image.load(ar[1]),(500,300) ), (1350, 250))
    app.blit(pygame.transform.scale(pygame.image.load(ar[2]),(500,300) ), (1350, 600))
    font = pygame.font.SysFont("Times new Roman", 54)  
    app.blit(font.render("Time:"+str(ti)+"sec", True, black),[750,50]) 

    app.blit(font.render("Light:0"+"   Heavy:0", True, black),[100,50]) 

    app.blit(font.render("Image", True, black),[1550,50]) 

  else:
    font = pygame.font.SysFont("Times new Roman", 54)  
    app.blit(font.render("Time:"+str(ti)+"sec", True, black),[750,50]) 

    app.blit(font.render("Light:"+str(ar[0][0])+"   Heavy:"+str(ar[0][1]), True, black),[100,50]) 

    app.blit(font.render("Image", True, black),[1550,50]) 

    app.blit(pygame.transform.scale(pygame.image.load(ar[1]),(500,300) ), (1350, 250))
    app.blit(pygame.transform.scale(pygame.image.load(ar[2]),(500,300) ), (1350, 600))
  
  pygame.display.update() 



def no_of_vehicles():
  arr=[]
  global pic_loop
  if pic_loop==10:
    pic_loop=0
  if pic_loop==9:
    arr.append(detect.v7[0])
    arr.append(v7)
    arr.append(detect.v7[1])

  elif pic_loop==8:
    arr.append(detect.v6[0])
    arr.append(v6)
    arr.append(detect.v6[1])

  
  elif pic_loop==7:
    arr.append(detect.v5[0])
    arr.append(v5)
    arr.append(detect.v5[1])

  elif pic_loop==6:
    arr.append(detect.v4[0])
    arr.append(v4)
    arr.append(detect.v4[1])

  elif pic_loop==5:
    arr.append(detect.v3[0])
    arr.append(v3)
    arr.append(detect.v3[1])

  elif pic_loop==4:
    arr.append(detect.v2[0])
    arr.append(v2)
    arr.append(detect.v2[1])

  elif pic_loop==3:
    arr.append(detect.v1[0])
    arr.append(v1)
    arr.append(detect.v1[1])

  elif pic_loop==2:
    arr.append(detect.l3[0])
    arr.append(l3)
    arr.append(detect.l3[1])
  
  elif pic_loop==1:
    arr.append(detect.l2[0])
    arr.append(l2)
    arr.append(detect.l2[1])

  elif pic_loop==0:
    arr.append(detect.l1[0])
    arr.append(l1)
    arr.append(detect.l1[1])
  
  pic_loop+=1

  return arr

def no_of_pedes():
  arr=[]
  global pedes_loop
  if pedes_loop==3:
    pedes_loop=0
  
  elif pedes_loop==2:
    arr.append(detect.i1[0])
    arr.append(i1)
    arr.append(detect.i1[1])
  
  elif pedes_loop==1:
    arr.append(detect.i2[0])
    arr.append(i2)
    arr.append(detect.i2[1])
  
  elif pedes_loop==0:
    arr.append(detect.i3[0])
    arr.append(i3)
    arr.append(detect.i3[1])
  
  pedes_loop+=1
  return arr

def gst_calculation(l):
  
  if l==5:
    ar=no_of_pedes()
    t=0
    if ar[0]:
      t=pedes_time
    

  else:
    ar=no_of_vehicles()
    t=0
    t+=(avg_light_vehicle_time*ar[0][0])/no_of_lanes
    t+=(avg_light_vehicle_time*ar[0][1])/no_of_lanes
    
    if t>max_green_time:
      t=max_green_time
    elif t<mini_green_time:
      t=mini_green_time 

    t=int(t)

  return ar,t


# The window closes after few time to stop that we need to make a loop.
runtime = True
start_time = time.time()
clock = pygame.time.Clock()
l=0
po=0
rem_time=1
first=1

while runtime:
  current_time = time.time()
  elapsed_time = current_time - start_time


  if int(elapsed_time) ==po:
    ar,req_time=gst_calculation(l+1)
    po+=req_time
    l+=1
    if pedes:
      if l>5:
        l=1
    else:
      if l>4:
        l=1
  
  rem_time=po-elapsed_time
    


  clock.tick(36)

  images(int(rem_time),l,ar)

  for event in pygame.event.get():  
      if event.type == pygame.QUIT:  
          pygame.quit()  
          # quit the program.   
          quit()  
      # Draws the surface object to the screen.   
      pygame.display.update() 
pygame.quit()
