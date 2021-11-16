#! /usr/bin/env python3

#python2
import roslib
import rospy
from std_msgs.msg import Header
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from visualization_msgs.msg import Marker, MarkerArray
from perception_msgs.msg import Obstacle, ObstacleArray
# from ros_numpy import msgify
# from cv_bridge import CvBridge
import sys
sys.path.remove('/opt/ros/melodic/lib/python2.7/dist-packages')
from socketserver import BaseRequestHandler,ThreadingTCPServer
import threading
import time
import numpy as np
import MeanH_Test as biao
BUF_SIZE=5000
#python3

global_data="wo shi ni die"*100

class SubscribeAndPublish:
    def __init__(self):
        self.all_obstacle_str=''

        self.sub1_name="/usb_cam/image_raw"
        self.sub1= rospy.Subscriber(self.sub1_name, Image,self.callback_rgb)
        self.sub2_name=rospy.get_param("~sub2")
        self.sub2= rospy.Subscriber(self.sub2_name, Image,self.callback_dual)

        self.pub1_name=rospy.get_param("~pub1")
        self.pub1= rospy.Publisher(self.pub1_name, Image,,queue_size=20)
        self.pub2_name=rospy.get_param("~pub2")
        self.pub2= rospy.Publisher(self.pub2_name, Image,,queue_size=20)

       
    def callback_rgb(self,img):
        B=biao.bd()
        img_rgb=B.Htest_rgb(img)
        self.pub1.publish(img_rgb)
     
    def callback_dual(self,img):
        B=biao.bd()
        img_dual=B.Htest_dual(img)
        self.pub2.publish(img_dual)



def main():
    rospy.init_node('road_mks_tcp_server', anonymous=True)
    #####################
    #开启ros
    t=SubscribeAndPublish()
    #####################
    rospy.spin()
if __name__ == "__main__":
    main()
