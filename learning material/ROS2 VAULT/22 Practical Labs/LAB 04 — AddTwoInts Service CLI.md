---
type: practical
status: verified
language: Hinglish
---

# 🧪 LAB 04 — AddTwoInts Service CLI

## Goal

Running `add_two_ints_server` ko ROS CLI se inspect aur manually call karke Request/Response flow verify karna.

---

# Server Requirement

Server running hona chahiye:

```bash
ros2 run my_first_pkg add_two_ints_server
```

Second terminal me workspace source:

```bash
cd ~/ros2_jazzy
source install/setup.zsh
```

---

# Step 1 — Service List

```bash
ros2 service list
```

Actual output included:

```text
/add_two_ints
/add_two_ints_server/describe_parameters
/add_two_ints_server/get_parameter_types
/add_two_ints_server/get_parameters
/add_two_ints_server/get_type_description
/add_two_ints_server/list_parameters
/add_two_ints_server/set_parameters
/add_two_ints_server/set_parameters_atomically
```

Important:

```text
/add_two_ints
→ hamari Service

/add_two_ints_server
→ Node name prefix in system/parameter services
```

---

# Step 2 — Type

```bash
ros2 service type /add_two_ints
```

Actual:

```text
example_interfaces/srv/AddTwoInts
```

---

# Step 3 — Info

```bash
ros2 service info /add_two_ints
```

Actual:

```text
Type: example_interfaces/srv/AddTwoInts
Clients count: 0
Services count: 1
```

---

# Step 4 — Manual Request

```bash
ros2 service call /add_two_ints \
example_interfaces/srv/AddTwoInts \
"{a: 5, b: 7}"
```

Actual:

```text
waiting for service to become available...
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=5, b=7)

response:
example_interfaces.srv.AddTwoInts_Response(sum=12)
```

---

# What this proved

```text
CLI
 ↓
Request fields a=5, b=7
 ↓
/add_two_ints
 ↓
Server
 ↓
callback(request, response)
 ↓
5 + 7
 ↓
Response sum=12
 ↓
CLI receives response
```

---

# Step 5 — Interface Structure

```bash
ros2 interface show example_interfaces/srv/AddTwoInts
```

Actual:

```text
int64 a
int64 b
---
int64 sum
```

---

# Evidence Summary

```text
Service exists ✅
Correct type ✅
1 server endpoint ✅
Request Object structure visible ✅
Response Object structure visible ✅
Real request sent ✅
Real sum=12 response received ✅
```

---

# Important Boundary

Ye lab **CLI-based Service practical** ko directly verify karta hai.

Python client ka conceptual/code flow separate notes me documented hai.

See [[Service Client]].
