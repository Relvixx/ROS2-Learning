---
type: correction
status: canonical
language: Hinglish
---

# Topic is not a Python Variable

Code:

```python
self.publisher_ = self.create_publisher(
    String,
    "chatter",
    10
)
```

Ye two different worlds hain:

```text
self.publisher_
→ Python attribute/reference

"chatter"
→ ROS Topic name
```

Topic ka naam Python variable se match hona required nahi.

---

# Correct mental model

```text
Python Object Reference
self.publisher_
      ↓
Publisher Object
      ↓ configured for
ROS Topic
/chatter
```

---

# Related

- [[Topic Mental Model]]
- [[Publisher Object and create_publisher]]
