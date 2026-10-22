---
type: correction
status: canonical
language: Hinglish
---

# `---` = Request / Response Boundary

Service interface:

```text
int64 a
int64 b
---
int64 sum
```

Wrong:

> `---` Client aur Server ko separate karta hai.

❌

Correct:

> `---` Service Interface ke Request section aur Response section ko separate karta hai.

```text
Request
a
b

---

Response
sum
```

See [[Service Interface]].
