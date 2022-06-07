# Smart-Traffic-Light-With-Pedestrian-Detection-System

## YOLO V5

  

This version is specifically chosen to aid the application in train newer models via transfer learning and that too efficiently. The Yolo v5 helps us in instantly converting the model trained into the “lite” version.

  

Since not only one but 2 separate models will be trained for  the complete build of the application, it is necessary to keep check of the computation power at hand. There are sparse chances of the machine being monitoring everything through the application being equipped with high-end computation power, so we must make a trade-off of training a less powerful classifier.

  

Knowing there is Yolov5 which is a more efficient model than the other object detection techniques, yet this choice have been made keeping in mind that PyTorch not only ships with  object detection algorithms but also ways in which detection of the objects could be put to good use. For Example, a simple python code with optimal use of API’s provided by PyTorch could even help us in tagging every object  in the frame and even calculating speed relative to the near-by objects.

  

## Data
Will be exclusively prepared for this project.The classifier inside the model that is being used is a combination of Convolutional Neural Nets and Dense networks. Neural Nets have the  property, “Better the data, Better the job done”. After trying for weeks, a suitable dataset has not been identified or free as well as paid services. There are datasets available but the images, inside it, are not the portraying the Indian traffic. The core of the application lies inside the data and  if we are not able to identify vehicles, Hence, it has been decided by the team that a dataset will be prepared for the application, and it would be comprising around more than 1000 images

  

## Machine chosen:
 A local machine with decent processing power in case of CPU as well as GPU.

  

We will be training two models for  the application which will be performing completely different tasks. For the first prototype of the application both the models will be trained via transfer learning on a local machine, so that the dataset requirements can be altered at any time. Training on a local machine will be aiding us in the documentation part and since we have limited space on the cloud, we have made the choice of local machine. The local machine that will be used will be having an i5 9th gen-  as  CPU, 16 gigs of RAM, 4GB Nvidia GTX  1650  as  GPU  and a dedicated disk drive of 100gbs. Such high-end configuration is chosen because we might need to train a single model multiple times for the efficiency. Once a model is trained it would be able to work at 15 frames per second even on a lowly powered device in accordance with the research we have conducted till now.

  

## Proposed Workflow

  

Installing the appropriate versions of the dependencies such as  YOLO, PyTorch, pandas, NumPy, OpenCV etc. such that all of them are compatible with one another into a new virtual environment.

Installing and diagnosing the PyTorch object detection API.

Install Nvidia Cuda toolkit to provide development environment for  high performance GPU-accelerated applications.

Collecting the dataset and resizing all  the images.

Label each object  in every image that the  object detector should be able to detect.

Configuring the training process.

Initiating the training process until we get the required accuracy and preventing overfitting.

Using this Inference to test for  our results.

If not satisfied with  the results restart training else using the same model as our Object detector.

After we have successfully trained the model to achieve optimum results. Connecting Pedestrian and vehicle detection the models, so that the output of models can be fed as an input to the other, An A.I. Traffic Management System in  True Sense”.

Switching the lights on the base of the output other models.

Finding the proper flow required for  interconnecting the various modules of the system.

Making a prototype for  the complete application build.

  
## Vehicle Detection Module:

  

The proposed system will use YOLO to locate the vehicle. It provides good accuracy with  the high FPS required for speeding vehicles. The custom YOLO model will be trained for the purpose of finding vehicle and it will also be able to detect vehicles of different categories such as cars, bicycles, rickshaws(light vehicle) etc and heavy vehicles (buses and trucks). The Custom trained dataset for the model is labelled as “Trained.pt” .The model will be trained using a large database Collected and labelled by us and then with pre-trained weights downloaded from the YOLO website. This module is designed for detection and counting vehicles on Lanes and the output is a feed to signal switching module to calculate the time given for each route.

  

The Custom trained dataset for  the model is labelled as “Trained.pt” to test object  with our custom dataset. we have to provide source and location of weights for the successful execution which ion our case is same as current working directory. The Input/Source can be in form of Webcam, Image, Video, Directory, Global File Type, RTSP stream, RTMP stream or  HTTP stream. The Supported video can also be live streamed form video streaming platforms such as YouTube. List of Supported image and video formats.

**Images:** bmp, jpg, jpeg, png, tif, tiff, dng, webp, mpo

**Videos:** mov, avi, mp4, mpg, mpeg, m4v, wmv, mkv

  

## Pedestrian Detection Module
 For pedestrian detection also YOLO module is used. In the proposed system when any pedestrian approaches the cross-section to cross the road. This module will detect them and it will create a request to the signal switching module to allots some time for them. This will happen in an order after switching all that light once or completing one complete circle it will provide calculate time to the pedestrians to cross the road. The Custom trained dataset for the model is labelled as “Trained_pedes.pt”. The model will be trained using a large database Collected and labelled by us and then with pre-trained weights downloaded from the YOLO website. This module is designed for detection and counting vehicles on Lanes and the output is a feed to signal switching module to calculate the time given for each route.

  

The Custom trained dataset for  the model is labelled as “Trained_pedes.pt” to test object  with our custom dataset. we have to provide source and location of weights for the successful execution which ion our case is same as current working directory.

  

## Signal Switching Module

  

The Work of Signal Switching Module (SSM) is to adjust the time for  the green signal on the terms of the traffic density and time adjustment for pedestrians which is provide to this module the output of the vehicles detection module and pedestrian detection module. It will also switch the light in a cyclic order and will break the order for the pedestrians This module gets its input form the other modules. The input  is  in form of no of vehicles and no of people as already explained. The Red Light and Yellow will also follow the green light pattern. The Algorithm can also be scaled in  any way according the size of intersection or to the average amount of time taken by vehicles.

  

Requirements for  considering Algo Development:

  

1. Analyse the time algorithm for  calculating traffic congestion and the duration of the green light - this determines when the image should be captured.

  

2. Number of routes

  

3. Total number of vehicles for  each  class such as cars, trucks, motorcycles, etc.

  

4. Traffic congestion is calculated using the above factors

  

5. Overtime due to the speed at which each car suffers at the start and  the non-linear rise of the lag suffered by rear cars.

  

6. The average speed of each phase of the car when the green light starts which is  the amount of time required to cross the signal in  each phase of the car.

  

7. Maximum and minimum and time limit for  green light - to prevent starvation

  

8. A pedestrian waiting time on the sidewalk to cross.

  
  

When the algorithm is activated, the default time is  set  for  the first signal of the first cycle and the time for  all other first loop signals and  for  all subsequent cycle signals set by the algorithm. It starts a separate thread that handles car detection across the main indicator that controls the current signal timer. When the current green light timer (or red light timer for the next green signal) reaches 0 seconds, the acquisition filters take a summary of the next path. The result is then transmitted and the next green signal timer is  set. All of this happens in the background while the main cable counts down the timer to the current green signal. This allows the timer allotment to be unobtrusive and prevents any slowing down. If the green time counter for the current signal becomes zero, the next signal becomes green at the time set by the algorithm.

  

The picture is taken when the  next  green signal time is  0 seconds. This gives the system a total of 5 seconds (Variable) to process the image, find the number of cars for  each  class present in the image, calculate the time of the green signal, and then properly set the times for this signal and red. next signal signal time. To get the best green signal time based on the number of cars of each class on the signal, the average speed of the cars at the time of start and their acceleration times are used, with the average amount of time each class takes to cross the road. road found. The green signal time is then calculated using the formula below.

  

The average time each section of the vehicle it takes to cross the intersection can be set by location, i.e., regional intelligence, city intelligence, local intelligence, or even intersection based on intersection factors, to make traffic. more effective management. Data from the relevant transport authorities can be analyzed in this regard.

  

The signals change in a rotating manner. This is  in line with the current system where the signals turn green respectively with a pattern that does not change and does not require people to change their methods or cause any confusion. The signal sequence is also the same as the current system, and the yellow signals are also counted.

  

Order of signals: Red → Green → Yellow → Red
