---
type: comparison
status: locked
language: Hinglish
---

# Topic vs Service

## Topic

Pattern:

```text
Publisher
   ↓ Message
Topic
   ↓
Subscriber
```

Use when data publish/subscribe pattern me flow karna hai.

Publishing periodic, event-driven, sparse ya bursty ho sakti hai.

---

# Service

Pattern:

```text
Client
  ↓ Request
Server
  ↓ Response
Client
```

Specific request ka specific response.

---

# Objects

## Topic

```text
Message Object
```

## Service

```text
Request Object
Response Object
```

---

# Interface

## Topic message example

```text
std_msgs/msg/String
```

## Service example

```text
example_interfaces/srv/AddTwoInts
```

---

# CLI

```text
topic pub
↔
service call
```

But mechanisms literally same nahi hain.

Publisher = Server aur Subscriber = Client bolna technically exact nahi.

---

# Related

- [[Topic Mental Model]]
- [[Why Services Exist]]
