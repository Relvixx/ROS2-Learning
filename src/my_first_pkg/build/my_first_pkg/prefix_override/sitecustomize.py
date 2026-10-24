import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/relvixx/ros2_jazzy/src/my_first_pkg/install/my_first_pkg'
