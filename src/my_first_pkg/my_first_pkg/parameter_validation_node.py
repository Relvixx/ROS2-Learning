import rclpy
from rclpy.node import Node

from rcl_interfaces.msg import (
    SetParametersResult,
    ParameterDescriptor,
    FloatingPointRange
)


class ParameterValidationNode(Node):

    def __init__(self):
        super().__init__('parameter_validation_node')

        # ---------------------------
        # max_speed
        # Callback validation
        # ---------------------------
        self.declare_parameter(
            'max_speed',
            2.0
        )

        # ---------------------------
        # robot_mode
        # Callback validation
        # ---------------------------
        self.declare_parameter(
            'robot_mode',
            'normal'
        )

        # ---------------------------
        # acceleration
        # Descriptor range validation
        # ---------------------------
        acceleration_range = FloatingPointRange(
            from_value=0.0,
            to_value=2.0,
            step=0.1
        )

        acceleration_descriptor = ParameterDescriptor(
            description='Allowed robot acceleration from 0.0 to 2.0',
            floating_point_range=[acceleration_range]
        )

        self.declare_parameter(
            'acceleration',
            1.0,
            acceleration_descriptor
        )

        # Register parameter validation callback
        self.add_on_set_parameters_callback(
            self.parameter_callback
        )

        # Timer for demonstrating dynamic reconfiguration
        self.timer = self.create_timer(
            2.0,
            self.control_loop
        )

        self.get_logger().info(
            'Parameter Validation Node started'
        )


    def parameter_callback(self, params):

        for param in params:

            if param.name == 'max_speed':

                if param.value < 0.0 or param.value > 5.0:

                    return SetParametersResult(
                        successful=False,
                        reason='max_speed must be between 0.0 and 5.0'
                    )

            if param.name == 'robot_mode':

                if param.value not in [
                    'safe',
                    'normal',
                    'sport'
                ]:

                    return SetParametersResult(
                        successful=False,
                        reason='robot_mode must be safe, normal, or sport'
                    )

        return SetParametersResult(
            successful=True
        )


    def control_loop(self):

        max_speed = self.get_parameter(
            'max_speed'
        ).value

        robot_mode = self.get_parameter(
            'robot_mode'
        ).value

        self.get_logger().info(
            f'Robot mode: {robot_mode} | Max speed: {max_speed}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = ParameterValidationNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()