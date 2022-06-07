#importing required Modules
import time
import random


avg_light_vehicle_time=5
avg_heavy_vehicle_time=10

no_of_lanes=2

inital_default_time=60

max_green_time=150
mini_green_time=20

#Initializing all Light Variables with Red Color  
l1,l2,l3,l4="Red","Red","Red","Red"
  

def no_of_vehicles():
  arr=[]
  #Currently using random no of vehicles.

  #Light Vehicles =  Light Motor Vehicle Category of non-transport class.
  light_vehicles=random.randint(0,50)
  arr.append(light_vehicles)
  
  #Heavy vehicles =Vehicles like trailers, larger trucks, and other similar vehicles
  heavy_vehicles=random.randint(0,20)
  arr.append(heavy_vehicles)

  return arr
  

def gst_calculation(ar):
  t=0
  t+=(avg_light_vehicle_time*ar[0])/no_of_lanes
  t+=(avg_light_vehicle_time*ar[1])/no_of_lanes
  
  if t>max_green_time:
    t=max_green_time
  elif t<mini_green_time:
    t=mini_green_time 

  t=int(t)

  return t

loop_count=0

while True:
  
  gst=inital_default_time
  l1="Green"
  if loop_count==0:
    print("Time Given:",gst,"\nL1:",l1,"\nL2:",l2,"\nL3:",l3,"\nL4:",l4,"\n")
  else:
    print("No of light Vehicles:",lis[0],"No of heavy Vehicles:",lis[1],"Time Given:",gst,"\nL1:",l1,"\nL2:",l2,"\nL3:",l3,"\nL4:",l4,"\n")


  time.sleep(gst-5)
  l1="Yellow"
  print("L1:",l1,"\nL2:",l2,"\nL3:",l3,"\nL4:",l4,"\n")

  lis=no_of_vehicles()
  gst=gst_calculation(lis)
  time.sleep(5)
  l1="Red"

  print()
  
  l2="Green"
  print("No of light Vehicles:",lis[0],"No of heavy Vehicles:",lis[1],"Time Given:",gst,"\nL1:",l1,"\nL2:",l2,"\nL3:",l3,"\nL4:",l4,"\n")

  time.sleep(gst-5)
  l2="Yellow"
  print("L1:",l1,"\nL2:",l2,"\nL3:",l3,"\nL4:",l4,"\n")

  lis=no_of_vehicles()
  gst=gst_calculation(lis)
  time.sleep(5)
  l2="Red"


  l3="Green"
  print("No of light Vehicles:",lis[0],"No of heavy Vehicles:",lis[1],"Time Given:",gst,"\nL1:",l1,"\nL2:",l2,"\nL3:",l3,"\nL4:",l4,"\n")

  time.sleep(gst-5)
  l3="Yellow"
  print("L1:",l1,"\nL2:",l2,"\nL3:",l3,"\nL4:",l4,"\n")

  lis=no_of_vehicles()
  gst=gst_calculation(lis)
  time.sleep(5)
  l3="Red"

  l4="Green"
  print("No of light Vehicles:",lis[0],"No of heavy Vehicles:",lis[1],"Time Given:",gst,"\nL1:",l1,"\nL2:",l2,"\nL3:",l3,"\nL4:",l4,"\n")

  time.sleep(gst-5)
  print("L1:",l1,"\nL2:",l2,"\nL3:",l3,"\nL4:",l4,"\n")

  l4="Yellow"
  lis=no_of_vehicles()
  gst=gst_calculation(lis)
  time.sleep(5)
  l1="Red"

  inital_default_time=gst
  loop_count+=1
  print("Cycle ",loop_count,"Completed\n\n")








