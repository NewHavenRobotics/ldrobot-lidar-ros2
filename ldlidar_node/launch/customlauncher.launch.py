# Save this file as 'my_humble_launch.py'

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():
    return LaunchDescription([
        # Include and launch another launch file with output='screen'
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join('launch', 'ldlidar_with_mgr.launch.py')),
            launch_arguments={'output': 'screen'}.items(),
        ),
        
        # You can add more actions or nodes here if needed
        Node(
            package='ldlidar',
            executable='your_node_executable',
            name='your_node_name',
            output='screen',  # or 'log'
        ),
    ])
