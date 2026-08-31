import rclpy
from rclpy.node import Node


class ParameterNode(Node):

    def __init__(self):
        super().__init__('parameter_node')

        self.declare_parameter('max_speed', 2.0)
        
        speed = self.get_parameter('max_speed').value
        self.get_logger().info(f'max_speed is: {speed}')


def main(args=None):
    rclpy.init(args=args)

    node = ParameterNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()