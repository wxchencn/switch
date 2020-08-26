'''
Description: 
Version: 1.0
Autor: wxchen
Date: 2020-08-08 21:19:36
LastEditTime: 2020-08-08 22:18:50
'''
import rosbag
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
import cv2

# bag_file = '/mnt/d/datasets/switch/20200807_170504.bag'
bag_file = '/home/wxchen/datasets/switch/20200807_170504.bag'
bag = rosbag.Bag(bag_file, "r")

print(bag)

# info = bag.get_type_and_topic_info()
# print(info)

# bag_data = bag.read_messages('/device_0/sensor_1/Color_0/image/data')
# bag_data = bag.read_messages('/device_0/sensor_0/Depth_0/image/data')


bridge = CvBridge()
for topic,msg,t in bag.read_messages():
    if topic == "/device_0/sensor_0/Depth_0/image/data":
        try:
            cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
            timestr = "%.f" %  msg.header.stamp.to_sec()
            image_name = '/home/wxchen/zjwork/switch/depth/'+timestr+ ".jpg"
            cv2.imwrite(image_name, cv_image)
        
        except CvBridgeError as error:
            print(error)
    elif topic == "/device_0/sensor_1/Color_0/image/data":
        try:
            cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
            timestr = "%.f" %  msg.header.stamp.to_sec()
            image_name = '/home/wxchen/zjwork/switch/images/'+timestr+ ".jpg"
            cv2.imwrite(image_name, cv_image)
        
        except CvBridgeError as error:
            print(error)
            

cv2.imshow("RGBimage", cv_image)

if cv2.waitKey(0) == ord("x"):
    cv2.destroyAllWindows()