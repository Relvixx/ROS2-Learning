---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Service Interface

## Simple definition

Service Interface define karta hai:

```text
Request ka structure
+
Response ka structure
```

File extension:

```text
.srv
```

---

# Example

```text
AddTwoInts.srv
```

```text
int64 a
int64 b
---
int64 sum
```

Breakdown:

```text
REQUEST
├── int64 a
└── int64 b

---

RESPONSE
└── int64 sum
```

---

# `---` ka meaning

`---`:

> **Request aur Response definition ka boundary/separator.**

Ye:

❌ Client/Server separator nahi  
❌ network boundary syntax nahi  
❌ object nahi

See [[Service Interface Separator is Request Response Boundary]].

---

# Interface → Generated Types → Objects

Conceptual model:

```text
Service Interface
       ↓
Request type + Response type
       ↓
Request Object + Response Object
```

Example:

```python
request = AddTwoInts.Request()
```

and server callback gets/prepares response.

---

# Fields vs Objects

Interface me:

```text
a
b
sum
```

**fields** hain.

Ye khud Request/Response objects nahi.

Actual values:

```text
a = 5
b = 7
sum = 12
```

objects ke fields ke andar aati hain.

---

# Related

- [[AddTwoInts Service Interface]]
- [[Request Object]]
- [[Response Object]]
- [[ROS 2 Interface Hierarchy]]
