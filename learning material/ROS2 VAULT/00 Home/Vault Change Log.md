---
type: changelog
status: living
language: Hinglish
---

# 📝 Vault Change Log

## Batch 01
Foundation + Node.

## Batch 02
Publisher + Subscriber + Topics.

## Batch 03
Services.

## Batch 04
Actions.

## Batch 05
Parameters.

## Batch 06
Parameter Callbacks & Validation.

## 2026-10-03 — Batch 07
Launch Files.

### Added — Launch Concepts
- Why Launch Files Exist
- Launch File Mental Model
- Launch File vs Node
- rclpy Node vs launch_ros Node
- generate_launch_description
- LaunchDescription Object
- Launch Action Node Object
- package / executable / name
- executable vs node name
- launch parameter override

### Added — Package / Installation
- launch folder structure
- setup.py launch installation
- glob()
- os.path.join()
- setup.py vs package.xml
- build/install/source flow
- symlink-install

### Added — Runtime
- ros2 launch
- single-node runtime flow
- multi-node launch
- multi-node runtime flow
- launch success vs node runtime success

### Added — Actual Practicals
- First `parameter.launch.py`
- Multi-node Publisher + Subscriber
- ROS graph + `/hello_topic` verification

### Added — Debugging
- launch file missing from installed share directory
- unsourced fresh terminal → package not found
- publisher process crash after successful launch
- Python scope bug: `print(node.publisher_)`
- source file vs installed launch file

### Boundary
Launch Arguments sirf introduced state me preserve hua. Full chapter intentionally pre-filled nahi kiya gaya.
