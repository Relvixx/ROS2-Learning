---
type: correction
status: canonical
language: Hinglish
---

# Descriptor and Callback are not the Same

Final corrected understanding:

```text
Descriptor
→ mostly static/general declared metadata + constraints

Callback
→ custom/context-dependent validation logic
```

Practical proof:

```text
max_speed 8.0
→ callback reason

acceleration 5.0
→ descriptor range error
```

Different mechanisms, same broad goal of safer configuration.
