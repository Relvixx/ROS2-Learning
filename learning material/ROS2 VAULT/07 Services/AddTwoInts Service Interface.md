---
type: example
status: verified
depth: must-know
language: Hinglish
---

# AddTwoInts Service Interface

Actual interface:

```text
example_interfaces/srv/AddTwoInts
```

CLI:

```bash
ros2 interface show example_interfaces/srv/AddTwoInts
```

Actual observed output:

```text
int64 a
int64 b
---
int64 sum
```

---

# Request

```text
int64 a
int64 b
```

Generated conceptual Request Object:

```python
request = AddTwoInts.Request()
```

Then:

```python
request.a = 5
request.b = 7
```

Object view:

```text
request
├── a = 5
└── b = 7
```

---

# Response

```text
int64 sum
```

Server:

```python
response.sum = request.a + request.b
```

Result:

```text
response
└── sum = 12
```

---

# Service Type Path

```text
example_interfaces
       ↓ package

srv
       ↓ service interface category

AddTwoInts
       ↓ service interface name
```

---

# Important

Service name:

```text
/add_two_ints
```

Service type/interface:

```text
example_interfaces/srv/AddTwoInts
```

Dono same nahi.

See [[Service Name vs Node Name]] and [[Service CLI]].
