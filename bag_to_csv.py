#!/usr/bin/env python
# -*- coding: utf-8 -*-



import rospy
from nav_msgs.msg import Odometry
from nav_msgs.msg import Path
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import Range
import csv
import os

class OdomLogger:
    def __init__(self, topic_name, msg_type, filename):
        self.filename = filename
        self.file_exists = os.path.isfile(self.filename)
        
        # CSV 파일 열기. 파일이 이미 존재하지 않으면, 헤더를 추가합니다.
        self.csv_file = open(self.filename, mode='a')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        if not self.file_exists:
            self.csv_writer.writerow(["timestamp", "x", "y", "z", "qx", "qy", "qz", "qw"])
        
        # Odometry 데이터를 구독합니다.
        rospy.Subscriber(topic_name, Odometry, self.callback)
        

    def callback(self, msg):
        # 메시지에서 위치(position)과 자세(orientation) 데이터를 추출합니다.
        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation
        timestamp = msg.header.stamp.to_sec() 
        
        # 데이터를 CSV 파일에 씁니다.
        self.csv_writer.writerow([timestamp, position.x, position.y, position.z,
                                  orientation.x, orientation.y, orientation.z, orientation.w])
        
        
class PoseLogger:
    def __init__(self, topic_name, msg_type, filename):
        self.filename = filename
        self.file_exists = os.path.isfile(self.filename)
        
        # CSV 파일 열기. 파일이 이미 존재하지 않으면, 헤더를 추가합니다.
        self.csv_file = open(self.filename, mode='a')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        if not self.file_exists:
            self.csv_writer.writerow(["timestamp", "x", "y", "z", "qx", "qy", "qz", "qw"])
        
        # Odometry 데이터를 구독합니다.
        rospy.Subscriber(topic_name, Pose, self.callback)
    
    def callback(self, msg):
        # 메시지에서 위치(position)과 자세(orientation) 데이터를 추출합니다.
        position = msg.position
        orientation = msg.orientation
        timestamp = msg.header.stamp.to_sec() 
        
        # 데이터를 CSV 파일에 씁니다.
        self.csv_writer.writerow([timestamp, position.x, position.y, position.z,
                                  orientation.x, orientation.y, orientation.z, orientation.w])
        
        
class PoseStampedLogger:
    def __init__(self, topic_name, msg_type, filename):
        self.filename = filename
        self.file_exists = os.path.isfile(self.filename)
        
        # CSV 파일 열기. 파일이 이미 존재하지 않으면, 헤더를 추가합니다.
        self.csv_file = open(self.filename, mode='a')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        if not self.file_exists:
            self.csv_writer.writerow(["timestamp", "x", "y", "z", "qx", "qy", "qz", "qw"])
        
        # Odometry 데이터를 구독합니다.
        rospy.Subscriber(topic_name, PoseStamped, self.callback)
    
    def callback(self, msg):
        # 메시지에서 위치(position)과 자세(orientation) 데이터를 추출합니다.
        position = msg.pose.position
        orientation = msg.pose.orientation
        timestamp = msg.header.stamp.to_sec() 
        
        # 데이터를 CSV 파일에 씁니다.
        self.csv_writer.writerow([timestamp, position.x, position.y, position.z,
                                  orientation.x, orientation.y, orientation.z, orientation.w])        
        
class PathLogger:
    def __init__(self, topic_name, msg_type, filename):
        self.filename = filename
        self.file_exists = os.path.isfile(self.filename)
        
        # CSV 파일 열기. 파일이 이미 존재하지 않으면, 헤더를 추가합니다.
        self.csv_file = open(self.filename, mode='a')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        if not self.file_exists:
            self.csv_writer.writerow(["timestamp", "x", "y", "z", "qx", "qy", "qz", "qw"])
        
        # Odometry 데이터를 구독합니다.
        rospy.Subscriber(topic_name, Path, self.callback)
    
    def callback(self, msg):
        # 메시지에서 위치(position)과 자세(orientation) 데이터를 추출합니다.
        position = msg.poses.pose.position
        orientation = msg.poses.pose.orientation
        timestamp = msg.header.stamp.to_sec() 
        
        # 데이터를 CSV 파일에 씁니다.
        self.csv_writer.writerow([timestamp, position.x, position.y, position.z,
                                  orientation.x, orientation.y, orientation.z, orientation.w])     
        
class RangeLogger:
    def __init__(self, topic_name, msg_type, filename):
        self.filename = filename
        self.file_exists = os.path.isfile(self.filename)
        
        # CSV 파일 열기. 파일이 이미 존재하지 않으면, 헤더를 추가합니다.
        self.csv_file = open(self.filename, mode='a')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        if not self.file_exists:
            self.csv_writer.writerow(["timestamp", "range"])
        
        # Odometry 데이터를 구독합니다.
        rospy.Subscriber(topic_name, Range, self.callback)
    
    def callback(self, msg):
        # 메시지에서 위치(position)과 자세(orientation) 데이터를 추출합니다.
        
        timestamp = msg.header.stamp.to_sec() 
        range_ = msg.range
        
        # 데이터를 CSV 파일에 씁니다.
        self.csv_writer.writerow([timestamp, range_])   

if __name__ == '__main__':
    rospy.init_node('data_logger_node')
    
    #UAV1_GPS = OdomLogger('/UAV1/gps_modified/odom', Odometry, "exp1_w_UAV1_gps_pose.csv")
    #UAV1_VINS = OdomLogger('/UAV1/vins_modified/odometry', Odometry, "exp1_w_UAV1_vins_pose.csv")
    #UAV1_OURS = PoseStampedLogger('/UAV1_vins_scaled_pose_closed',PoseStamped,"exp1_w_UAV1_ours_pose.csv")
    #UAV2_GPS = OdomLogger('/UAV2/gps_modified/odom', Odometry, "exp1_w_UAV2_gps_pose.csv")
    #UAV2_VINS = OdomLogger('/UAV2/vins_modified/odometry', Odometry, "exp1_w_UAV2_vins_pose.csv")
    #UAV2_OURS = PoseStampedLogger('/UAV2_vins_scaled_pose_closed',PoseStamped,"exp1_w_UAV2_ours_pose.csv")
    #UAV3_GPS = OdomLogger('/UAV3/gps_modified/odom', Odometry, "exp1_w_UAV3_gps_pose.csv")
    #UAV3_VINS = OdomLogger('/UAV3/vins_modified/odometry', Odometry, "exp1_w_UAV3_vins_pose.csv")
    #UAV3_OURS = PoseStampedLogger('/UAV3_vins_scaled_pose_closed',PoseStamped,"exp1_w_UAV3_ours_pose.csv")
    # UGV1_GPS = OdomLogger('/UGV1/gps_modified/odom', Odometry, "exp1_w_UGV!_gps_pose.csv")
    # UGV1_VINS = OdomLogger('/UGV1/vins_modified/odometry', Odometry, "exp1_w_UGV1_vins_pose.csv")
    # UGV1_OURS = PoseStampedLogger('/UGV1_vins_scaled_pose_closed',PoseStamped,"exp1_w_UGV1_ours_pose.csv")
    #UAV5_GPS = OdomLogger('/UAV5/gps_modified/odom', Odometry, "exp1_w_UAV5_gps_pose.csv")
    #UAV5_VINS = OdomLogger('/UAV5/vins_modified/odometry', Odometry, "exp1_w_UAV5_vins_pose.csv")
    #UAV5_OURS = PoseStampedLogger('/UAV5_vins_scaled_pose_closed',PoseStamped,"exp1_w_UAV5_ours_pose.csv")
    

    ### exp1 with init
    # UAV1_GPS = OdomLogger('/UAV1_gps_pose', Odometry, "exp1_w_UAV1_s2gps_pose.csv")
    # UAV1_VINS = PoseStampedLogger('/UAV1/vins_global/pose', PoseStamped, "exp1_w_UAV1_vins_pose.csv")
    # UAV1_SOTA2 = PoseStampedLogger('/UAV1/vins_optimized/pose', PoseStamped, "exp1_w_UAV1_sota2_pose.csv")

    # UAV2_GPS = OdomLogger('/UAV2_gps_pose', Odometry, "exp1_w_UAV2_s2gps_pose.csv")
    # UAV2_VINS = PoseStampedLogger('/UAV2/vins_global/pose', PoseStamped, "exp1_w_UAV2_vins_pose.csv")
    # UAV2_SOTA2 = PoseStampedLogger('/UAV2/vins_optimized/pose', PoseStamped, "exp1_w_UAV2_sota2_pose.csv")
    
    # UAV3_GPS = OdomLogger('/UAV3_gps_pose', Odometry, "exp1_w_UAV3_s2gps_pose.csv")
    # UAV3_VINS = PoseStampedLogger('/UAV3/vins_global/pose', PoseStamped, "exp1_w_UAV3_vins_pose.csv")
    # UAV3_SOTA2 = PoseStampedLogger('/UAV3/vins_optimized/pose', PoseStamped, "exp1_w_UAV3_sota2_pose.csv")
    
    # UAV5_GPS = OdomLogger('/UAV5_gps_pose', Odometry, "exp1_w_UAV5_s2gps_pose.csv")
    # UAV5_VINS = PoseStampedLogger('/UAV5/vins_global/pose', PoseStamped, "exp1_w_UAV5_vins_pose.csv")
    # UAV5_SOTA2 = PoseStampedLogger('/UAV5/vins_optimized/pose', PoseStamped, "exp1_w_UAV5_sota2_pose.csv")

    # UGV1_GPS = OdomLogger('/UGV1_gps_pose', Odometry, "exp1_w_UGV1_s2gps_pose.csv")
    # UGV1_VINS = PoseStampedLogger('/UGV1/vins_global/pose', PoseStamped, "exp1_w_UGV1_vins_pose.csv")
    # UGV1_SOTA2 = PoseStampedLogger('/UGV1/vins_optimized/pose', PoseStamped, "exp1_w_UGV1_sota2_pose.csv")


    ### exp2 with init
    UAV1_GPS = PoseStampedLogger('/UAV1_gps_pose', PoseStamped, "exp2_w_UAV1_s2gps_pose.csv")
    UAV1_VINS = PoseStampedLogger('/UAV1/vins_global/pose', PoseStamped, "exp2_w_UAV1_vins_pose.csv")
    UAV1_SOTA2 = PoseStampedLogger('/UAV1/vins_optimized/pose', PoseStamped, "exp2_w_UAV1_sota2_pose.csv")

    UAV2_GPS = PoseStampedLogger('/UAV2_gps_pose', PoseStamped, "exp2_w_UAV2_s2gps_pose.csv")
    UAV2_VINS = PoseStampedLogger('/UAV2/vins_global/pose', PoseStamped, "exp2_w_UAV2_vins_pose.csv")
    UAV2_SOTA2 = PoseStampedLogger('/UAV2/vins_optimized/pose', PoseStamped, "exp2_w_UAV2_sota2_pose.csv")
    
    UAV3_GPS = PoseStampedLogger('/UAV3_gps_pose', PoseStamped, "exp2_w_UAV3_s2gps_pose.csv")
    UAV3_VINS = PoseStampedLogger('/UAV3/vins_global/pose', PoseStamped, "exp2_w_UAV3_vins_pose.csv")
    UAV3_SOTA2 = PoseStampedLogger('/UAV3/vins_optimized/pose', PoseStamped, "exp2_w_UAV3_sota2_pose.csv")
    
    UAV4_GPS = PoseStampedLogger('/UAV4_gps_pose', PoseStamped, "exp2_w_UAV4_s2gps_pose.csv")
    UAV4_VINS = PoseStampedLogger('/UAV4/vins_global/pose', PoseStamped, "exp2_w_UAV4_vins_pose.csv")
    UAV4_SOTA2 = PoseStampedLogger('/UAV4/vins_optimized/pose', PoseStamped, "exp2_w_UAV4_sota2_pose.csv")

    UAV5_GPS = PoseStampedLogger('/UAV5_gps_pose', PoseStamped, "exp2_w_UAV5_s2gps_pose.csv")
    UAV5_VINS = PoseStampedLogger('/UAV5/vins_global/pose', PoseStamped, "exp2_w_UAV5_vins_pose.csv")
    UAV5_SOTA2 = PoseStampedLogger('/UAV5/vins_optimized/pose', PoseStamped, "exp2_w_UAV5_sota2_pose.csv")
   
    rospy.spin()
