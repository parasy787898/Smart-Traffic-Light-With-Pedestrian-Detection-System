#importing required Modules
import time
import random
import matplotlib.pyplot as plt
 

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


x=[]
y=[]

run=True

while run:
  
  gst=inital_default_time
  l1="Green"    

  l1="Yellow"

  lis=no_of_vehicles()
  gst=gst_calculation(lis)

  total=lis[0]+lis[1]
  x.append(total)
  y.append(gst)


  l1="Red"

  print()
  
  l2="Green"
  

  l2="Yellow"

  lis=no_of_vehicles()
  gst=gst_calculation(lis)
  total=lis[0]+lis[1]
  x.append(total)
  y.append(gst)


  l2="Red"


  l3="Green"
  

  l3="Yellow"

  lis=no_of_vehicles()
  gst=gst_calculation(lis)
  total=lis[0]+lis[1]
  x.append(total)
  y.append(gst)


  l3="Red"

  l4="Green"
  


  l4="Yellow"
  lis=no_of_vehicles()
  gst=gst_calculation(lis)
  total=lis[0]+lis[1]
  x.append(total)
  y.append(gst)

  l1="Red"

  inital_default_time=gst
  loop_count+=1

  if loop_count>5:
    run=False



 
# plotting points as a scatter plot
plt.scatter(x, y, label= "stars", color= "green", s=30)
 
# x-axis label
plt.xlabel('No of Vehicle (Light+Heavy)')
# frequency label
plt.ylabel('Green Time Given')
# plot title
plt.title('')
# showing legend
plt.legend()
 
# function to show the plot
plt.show()







