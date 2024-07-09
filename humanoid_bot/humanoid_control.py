#!/usr/bin/env python

import sys
import rclpy
from rclpy.duration import Duration
from rclpy.action import ActionClient
from rclpy.node import Node
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

class HumanoidActionClient(Node):

    def __init__(self):
        super().__init__('humanoid_action_client')
        self._action_client = ActionClient(self, FollowJointTrajectory, '/joint_trajectory_controller/follow_joint_trajectory')

    def send_goal(self):
        goal_msg = FollowJointTrajectory.Goal()

        # Define joint names
        joint_names = [ 'rlj',
      'rlj1', 'rlj2',
      'rlj3', 'rlj4',
      'rlj5', 'llj',
      'llj1', 'llj2',
      'llj3', 'llj4', 'llj5']
    #  'rhj',
    #   'rhj1', 'rhj2',
    #   'rhj3', 'lhj',
    #   'lhj1', 'lhj2',
    #   'lhj3']

        # Create trajectory points
        points = []
        initial_point = JointTrajectoryPoint()
        initial_point.positions = [0.0] * len(joint_names)
        initial_point.time_from_start = Duration(seconds=0, nanoseconds=0).to_msg()

        final_point = JointTrajectoryPoint()
        final_point.positions = [0.0] * len(joint_names)
        final_point.time_from_start = Duration(seconds=1, nanoseconds=0).to_msg()

        points.append(initial_point)
        points.append(final_point)

        # Fill in goal message
        goal_msg.goal_time_tolerance = Duration(seconds=1, nanoseconds=0).to_msg()
        goal_msg.trajectory.joint_names = joint_names
        goal_msg.trajectory.points = points

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: ' + str(result))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        #self.get_logger().info('Received feedback: ' + str(feedback))

def main(args=None):
    rclpy.init(args=args)
    action_client = HumanoidActionClient()
    action_client.send_goal()
    rclpy.spin(action_client)

if __name__ == '__main__':
    main()
