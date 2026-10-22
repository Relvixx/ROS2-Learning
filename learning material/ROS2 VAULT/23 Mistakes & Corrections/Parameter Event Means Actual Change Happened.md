---
type: correction
status: canonical
language: Hinglish
---

# Parameter Event Means Actual Change Happened

A set **attempt** alone changed-parameter event ke liye enough nahi.

Actual practical:

```text
4.0 request
→ accepted
→ actual change
→ event ✅
```

```text
9.0 request
→ rejected
→ no actual change
→ no changed event ❌
```

So:

> `/parameter_events` ko validation request stream mat samjho. Humne itna verify kiya ki accepted actual change event me visible hua, rejected change attempt changed-parameter event me visible nahi hua.
