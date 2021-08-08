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
        self.bridge      = CvBridge()
        self.speed       = Twist()
        self.image       = None
        self.image_topic = "camera/rgb/image_raw"     
        self.rangess     = LaserScan()
        self.min_dist    = 0
        self.speed.linear.x = 0.0
        self.speed.angular.x = 0.0


        # Node cycle rate (in Hz)
        self.loop_rate = rospy.Rate(2)
     
        #Publishers
        
        #FOR LASER
        #self.laser_pub = rospy.Publisher('/revised_scan', LaserScan, queue_size = 10)
        
         #FOR CAMERA
     #--------------------------
     #Camera için Publisher yok|
     #--------------------------    
        
         #FOR SPEED
        self.cmd_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------        
        #Subscribers
        
         #FOR LASER
        rospy.Subscriber('/scan', LaserScan, self.callback)    #pub laser scan
        
         #FOR CAMERA
        #rospy.Subscriber(self.image_topic, Image, self.image_callback)
        
         #FOR SPEED
                
    #def scann_callback(self, msg):
     #self.rangess = self.msg.ranges
     #self.min_distance = min(self.rangess)
     #print(self.min_distance)

    #CALLBCACK FOR TWIST() for to subscribe 
    def callback_vel(self,data):
        print(data)
        #self.loop_rate.sleep()


    #Callback function For LASER      
    def callback(self, msg):
     current_time=rospy.Time.now()
     self.rangess.header.stamp=current_time
     self.rangess.header.frame_id='base_scan'
     self.rangess.ranges=msg.ranges[0:72]
     self.rangess.intensities=msg.intensities[0:72]
     #self.min_dist = min(self.rangess.ranges)
     self.laser_pub.publish(self.rangess)
     #print(self.min_dist)

    def scan_callback(self, msg):
        
        for i in range(len(msg.ranges)):
            self.min_dist = min(msg.ranges)
        
        print(self.min_dist)    

      
#------------------------------------------------------------------------------------------         
    #Callback function For CAMERA
    def image_callback(self, msg):
	    print("Received an image!")
	    try:
	 
	 	   self.image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
	       
	    except self.cv2.error as e:
	 	    print(e)
	 
	    else:
	 	   self.foto = cv2.imwrite('camerax_sonimage.jpeg', self.image)
	    self.loop_rate.sleep()		 	 	
#------------------------------------------------------------------------------------------		 
#------------------------------------------------------------------------------------------		 
    def start_robot(self):
             
        while not rospy.is_shutdown():
         self.laser_pub = rospy.Publisher('/revised_scan', LaserScan, queue_size = 10)  
         rospy.Subscriber("/cmd_vel", Twist, self.callback_vel)  
         
         self.speed.linear.x = 0.22
         self.speed.angular.x = 0.0
         self.cmd_pub.publish(self.speed)

         
         rospy.Subscriber('/revised_scan', LaserScan, self.scan_callback)
         
         if(self.min_dist<1):
             self.speed.linear.x  = 0.0
             self.speed.angular.x = 0.0
             self.cmd_pub.publish(self.speed)
             rospy.Subscriber(self.image_topic, Image, self.image_callback)    
         
         else:
             print("fuuuu")
             self.speed.linear.x  = 0.22
             self.speed.angular.x = 0.0
             self.cmd_pub.publish(self.speed)
             #self.loop_rate.sleep() 
       
if __name__ == '__main__':
     
     rospy.init_node('Robot', anonymous=True)		 
     
     robot_node = Robot()
     robot_node.start_robot() 
		 
