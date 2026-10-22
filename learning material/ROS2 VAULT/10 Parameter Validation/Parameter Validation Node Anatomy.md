---
type: code-anatomy
status: locked
depth: must-know
language: Hinglish
---

# Parameter Validation Node Anatomy

Final learned structure:

```python
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

        self.declare_parameter('max_speed', 2.0)
        self.declare_parameter('robot_mode', 'normal')

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

        self.add_on_set_parameters_callback(
            self.parameter_callback
        )

        self.timer = self.create_timer(
            2.0,
            self.control_loop
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
```

---

# Structure

```text
ParameterValidationNode
├── max_speed
│    └── callback validation 0–5
├── robot_mode
│    └── callback allowed values
├── acceleration
│    └── descriptor range 0–2
├── parameter_callback()
│    └── set-request event
└── control_loop()
     └── timer event
```

`acceleration` intentionally callback me validate nahi kiya gaya tha so descriptor could be isolated and tested.
