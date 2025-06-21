from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=["gz", "sim", "-v", "4", "/usr/share/ignition/ignition-gazebo6/worlds"],
            output="screen"
        ),
        Node(
            package="ros_gz_bridge",
            executable="parameter_bridge",
            arguments=[
                "/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist",
                "/lidar@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan"
            ],
            output="screen"
        ),
    ])

