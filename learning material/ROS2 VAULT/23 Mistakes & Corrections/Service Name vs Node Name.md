---
type: correction
status: canonical
language: Hinglish
---

# Service Name vs Node Name

Actual system me:

```text
/add_two_ints
```

→ **Service Name**

while:

```text
/add_two_ints_server
```

→ **Node Name**

Same nahi.

---

# Similar Topic analogy

```text
publisher_node
→ Node

/hello_topic
→ Topic
```

Services:

```text
add_two_ints_server
→ Node

/add_two_ints
→ Service
```

---

# Service Type bhi alag

```text
/add_two_ints
→ Service Name

example_interfaces/srv/AddTwoInts
→ Service Type / Interface
```

Three-way distinction:

```text
Node Name
Service Name
Service Type
```

---

# Related

- [[Service CLI]]
- [[AddTwoInts Service Interface]]
