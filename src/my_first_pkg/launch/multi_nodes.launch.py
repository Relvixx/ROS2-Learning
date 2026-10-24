from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    publisher = Node(
        package='my_first_pkg',
        executable='publisher_node',
        name='launch_publisher'
    )

    subscriber = Node(
        package='my_first_pkg',
        executable='subscriber_node',
        name='launch_subscriber'
    )

    return LaunchDescription([
        publisher,
        subscriber
    ])