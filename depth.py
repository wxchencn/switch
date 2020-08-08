'''
Description: 
Version: 1.0
Autor: wxchen
Date: 2020-08-08 21:19:36
LastEditTime: 2020-08-08 22:18:50
'''
import rosbag
from cv_bridge import CvBridge
import cv2

bag_file = '/home/wxchen/datasets/switch/20200807_170504.bag'
bag = rosbag.Bag(bag_file, "r")

# info = bag.get_type_and_topic_info()
# print(info)

# bag_data = bag.read_messages('/device_0/sensor_1/Color_0/image/data')
bag_data = bag.read_messages('/device_0/sensor_0/Depth_0/image/data')

print(bag_data)

bridge = CvBridge()
for topic,msg,t in bag_data:
    cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imshow("RGBimage", cv_image)
    if cv2.waitKey(0) == ord("x"):
        cv2.destroyAllWindows()