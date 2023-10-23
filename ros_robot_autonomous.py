#! /usr/bin/env python 

import rospy
import sys

from sensor_msgs.msg import LaserScan
import sensor_msgs.msg

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2


from geometry_msgs.msg import Twist

import os

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------

class Robot:
    
    def __init__(self):
        #Params
        self.bridge      = CvBridge()
        self.speed       = Twist()
        self.image       = None
        self.image_topic = "camera/rgb/image_raw"     
        self.rangess     = LaserScan()
        self.min_dist    = 0
        self.speed.linear.x = 0.0
        self.speed.angular.z = 0.0
        
        # Node cycle rate (in Hz)
        self.loop_rate = rospy.Rate(0.6)
     
        #Publishers
        
        #FOR LASER
        self.laser_pub = rospy.Publisher('/scan', LaserScan, queue_size = 10)
        
        #FOR CAMERA
        #--------------------------
        #Camera için Publisher yok|
        #--------------------------    
        
        #FOR SPEED
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------        

        #Subscribers
        
        #FOR LASER
        rospy.Subscriber('/scan', LaserScan, self.scan_callback)
         
        #FOR CAMERA
        rospy.Subscriber(self.image_topic, Image, self.image_callback)
        
        #FOR SPEED
        rospy.Subscriber("/cmd_vel", Twist, self.callback_vel)

    #CALLBCACK FOR TWIST() for to subscribe 
    def callback_vel(self,data):
        print(data)
        self.loop_rate.sleep()
    
    #CALLBACK FOR LASER() for to subscribe
    def scan_callback(self, msg):
        
        for i in range(len(msg.ranges)):
            self.min_dist = min(msg.ranges)

#------------------------------------------------------------------------------------------      
#------------------------------------------------------------------------------------------         
    
    #Callback function For CAMERA
    def image_callback(self, msg):
	    try:
	 	   self.image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
	       
	    except self.cv2.error as e:
	 	    print(e)
	      		 	   	
#------------------------------------------------------------------------------------------		 
#------------------------------------------------------------------------------------------		 
    
    def start_robot(self):
        
        self.laser_pub.publish(self.rangess)
              
        self.speed.linear.x = 0.13
        self.speed.angular.z = 0.0
        
        self.cmd_pub.publish(self.speed)
        self.cmd_pub.publish(self.speed)

        while not rospy.is_shutdown():
                
         print(self.min_dist)  
         if(self.min_dist<1):
             self.speed.linear.x  = 0.0
             self.speed.angular.z = 0.0
             self.cmd_pub.publish(self.speed)
             
             try:
                 self.foto = cv2.imwrite('camerax_sonimage.jpeg', self.image)
                 print("Image Saved!")
                 
             except cv2.error as e:
                 print(e)

         
         else:
             print("cont")
             self.speed.linear.x  = 0.10
             self.speed.angular.z = 0.0
             self.cmd_pub.publish(self.speed)
         
         self.loop_rate.sleep()
              
       
if __name__ == '__main__':
    rospy.init_node('Robot', anonymous=True)		 
     
    robot_node = Robot()
    robot_node.start_robot()
