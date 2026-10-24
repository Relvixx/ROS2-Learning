from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    parameter_node = Node(
        package='my_first_pkg',
        executable='parameter_node',
        name='config_node',
        parameters=[
            {'max_speed': 0.8}
        ]
    )

    return LaunchDescription([
        parameter_node
    ])