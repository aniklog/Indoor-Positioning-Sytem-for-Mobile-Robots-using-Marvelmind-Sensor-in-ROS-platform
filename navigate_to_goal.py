#!/usr/bin/env python  
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point


#Method for moving the robot to destination

def go_to_destination(xGoal,yGoal):

   #Defining Action Client

   ac = actionlib.SimpleActionClient("move", MoveBaseAction)

   #Waiting fro response from action server

   while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
           rospy.loginfo("Waiting for the move_base action server to respond")

   goal = MoveBaseGoal()
   
   
   #Frame parameters
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()

   # moving towards the destination*/

   goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
   goal.target_pose.pose.orientation.x = 0.0
   goal.target_pose.pose.orientation.y = 0.0
   goal.target_pose.pose.orientation.z = 0.0
   goal.target_pose.pose.orientation.w = 1.0

   rospy.loginfo("Calibrating destination co-ordinate")
   ac.send_goal(goal)

   ac.wait_for_result(rospy.Duration(60))

   if(ac.get_state() ==  GoalStatus.SUCCEEDED):
           rospy.loginfo("Robot reached destination")
           return True

   else:
           rospy.loginfo("Failed to reach destination")
           return False

if __name__ == '__main__':
   rospy.init_node('map_navigation', anonymous=False)
   x_goal = float(input("Set goal in x co-ordinate:"))
   y_goal = float(input("Set goal in x co-ordinate:"))
   
   go_to_destination(x_goal,y_goal)
   rospy.spin()
