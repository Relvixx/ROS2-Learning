---
type: concept
status: locked
depth: must-know
language: Hinglish
---

# Multiple Parameter Validation

Callback receives:

```text
params = list of proposed Parameter objects
```

So:

```python
for param in params:
```

important hai.

---

# Why?

Ek request me multiple proposed parameters ho sakte hain.

Example:

```text
max_speed = 4.0      ✅
robot_mode = turbo   ❌
```

Callback ko sab relevant proposed values inspect karne chahiye.

---

# Important loop logic

Invalid milte hi:

```python
return SetParametersResult(
    successful=False,
    reason='...'
)
```

But success:

```python
return SetParametersResult(successful=True)
```

loop complete hone ke baad.

See [[Why successful True is Outside the Loop]].
