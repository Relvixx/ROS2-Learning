---
type: object
status: locked
depth: must-know
language: Hinglish
---

# Action Result Object

Action task complete hone ke baad final output.

Server:

```python
result = Fibonacci.Result()
result.sequence = feedback_msg.partial_sequence
return result
```

---

# Object

```text
result
└── sequence
     └── final Fibonacci sequence
```

---

# Client Extraction

Result Future complete hone ke baad:

```python
result = future.result().result
```

Then:

```python
result.sequence
```

See [[future.result().result]].

---

# Result ≠ Feedback

```text
Feedback
→ intermediate progress

Result
→ final output
```
