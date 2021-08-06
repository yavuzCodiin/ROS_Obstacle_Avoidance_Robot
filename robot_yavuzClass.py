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
class Robot:
    
    def __init__(self):
        #Params
        self.bridge = CvBridge()
        self.speed = Twist()
        self.image = None
        self.image_topic = "camera/rgb/image_raw"     
        self.rangess = LaserScan()
     
          
        # Node cycle rate (in Hz)
        self.loop_rate = rospy.Rate(2)
     
        #Publishers
        #FOR LASER
        self.laser_pub = rospy.Publisher('/revised_scan', LaserScan, queue_size = 10)
         #FOR CAMERA
     #--------------------------
     #Camera için Publisher yok|
     #--------------------------    
         #FOR SPEED
        self.cmd_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

         
        #Subscribers
         #FOR LASER
        rospy.Subscriber('/scan', LaserScan, self.callback)
         #FOR CAMERA
        rospy.Subscriber(self.image_topic, Image, self.image_callback)
     
                
    #def scann_callback(self, msg):
     #self.rangess = self.msg.ranges
     #self.min_distance = min(self.rangess)
     #print(self.min_distance)
         
    #Callback function For LASER      
    def callback(self, msg):
     current_time=rospy.Time.now()
     self.rangess.header.stamp=current_time
     self.rangess.header.frame_id='base_scan'
     self.rangess.ranges=msg.ranges[0:72]
     self.rangess.intensities=msg.intensities[0:72]
     self.pub.publish(self.rangess)
     print(self.rangess.ranges[0])
      
#------------------------------------------------------------------------------------------         
    #Callback function For CAMERA
    def image_callback(self, msg):
	    print("Received an image!")
	    try:
	 
	 	   self.image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
	 
	    except self.cv2.error as e:
	 	    print(e)
	 
	    #else:
	 	#   self.image.cv2.imwrite('camerax_image.jpeg', cv2.img)
			 	 	
#------------------------------------------------------------------------------------------		 
#------------------------------------------------------------------------------------------		 
    def start_robot(self):
        self.speed.linear.x = 0.22
        self.speed.publish(self.cmd_pub)
     
     
        while not rospy.is_shutdown():
         if(self.min_distance<1):
             self.cmd_pub.linear = 0.0
             #self.cam_sub() 
         
         else:
             self.cmd_pub.linear = 0.22
	  	     
        self.loop_rate.sleep() 
       
if __name__ == '__main__':
     rospy.init_node('Robot', anonymous=True)		 
     
     robot_node = Robot()
     robot_node.start_robot()
