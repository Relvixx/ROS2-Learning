---
type: debugging
status: resolved
language: Hinglish
---

# 🔧 Publisher Crashed After Successful Launch

Multi-node launch output:

```text
publisher_node process started ✅
subscriber_node process started ✅
```

Then publisher:

```text
NameError: name 'node' is not defined
```

and:

```text
publisher process died ❌
```

Subscriber stayed running.

---

# Diagnosis

Launch layer had done its job:

```text
2 processes start hue
```

Problem launched Python program ke andar tha.

Traceback pointed to:

```python
print(node.publisher_)
```

See [[Python Scope Bug print node.publisher]].

---

# Important Lesson

```text
Launch action success
≠
application runtime guaranteed success
```

Different layers debug karo.
