---
type: cli-reference
status: verified
depth: must-know
language: Hinglish
---

# Service CLI

Services ko inspect aur manually call karne ke commands.

---

# 1. List

```bash
ros2 service list
```

Meaning:

> Current ROS graph me available Services ke names.

Actual output me:

```text
/add_two_ints
/add_two_ints_server/describe_parameters
/add_two_ints_server/get_parameter_types
/add_two_ints_server/get_parameters
...
```

Hamari actual Service:

```text
/add_two_ints
```

Baaki `/add_two_ints_server/...` parameter/system-related services the.

---

# 2. Type

```bash
ros2 service type /add_two_ints
```

Actual:

```text
example_interfaces/srv/AddTwoInts
```

---

# 3. Info

```bash
ros2 service info /add_two_ints
```

Actual:

```text
Type: example_interfaces/srv/AddTwoInts
Clients count: 0
Services count: 1
```

Interpretation:

```text
Services count: 1
→ one server/service endpoint providing service

Clients count: 0
→ at that observation moment no active registered client
```

---

# 4. Call

General:

```bash
ros2 service call <service_name> <service_type> <request_data>
```

Actual command:

```bash
ros2 service call /add_two_ints \
example_interfaces/srv/AddTwoInts \
"{a: 5, b: 7}"
```

Actual output:

```text
waiting for service to become available...
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=5, b=7)

response:
example_interfaces.srv.AddTwoInts_Response(sum=12)
```

---

# 5. Interface Show

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

# Topic CLI connection

| Topic | Service |
|---|---|
| `ros2 topic list` | `ros2 service list` |
| `ros2 topic type ...` | `ros2 service type ...` |
| `ros2 topic info ...` | `ros2 service info ...` |
| `ros2 topic pub ...` | `ros2 service call ...` |

Topic ke `echo` / `hz` ka Service me same role wala direct mapping nahi.

---

# Related

- [[LAB 04 — AddTwoInts Service CLI]]
- [[Service Name vs Node Name]]
