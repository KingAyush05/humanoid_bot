import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess, RegisterEventHandler

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='humanoid_bot' #<--- CHANGE ME

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )
    
    load_joint_state_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'start',
             'joint_state_broadcaster'],
        output='screen'
    )

    load_joint_trajectory_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'start', 'joint_trajectory_controller'],
        output='screen'
    )

    # spawn_controller = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["joint_state_broadcaster"],
    #     output="screen",
    # )

    # spawn_controller_traj = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["joint_trajectory_controller"],
    #     output="screen",
    # )
    
    # start_control = Node(package='humanoid_bot', executable='humanoid_control',
    #                      arguments=['-topic', 'robot_description', '-entity', 'my_bot'],
    #                               output='screen')

    # # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    # spawn_entity = Node(package='humanoid_bot', executable='spawn_entity',
    #                     arguments=['-topic', 'robot_description',
    #                                '-entity', 'my_bot', '-x', '0.0', '-y', '0.0', 'z', '0.3'],
    #                     output='screen')
    
    # #Run the teleop node from the frosty_hackathon_ps package
    # teleop = Node(package='frosty_hackathon_ps', executable='bot_teleop',
    #                     output='screen')


    # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        # spawn_controller,
        # spawn_controller_traj,
        # load_joint_state_controller,
        # load_joint_trajectory_controller,
        # spawn_entity,
        # start_control
        
        # teleop,
    ])