---
type: correction
status: canonical
language: Hinglish
---

# Request and Response are Different Objects

Wrong:

> `a`, `b`, `sum` ek hi object ke fields hain.

❌

Correct:

```text
Request Object
├── a
└── b

Response Object
└── sum
```

Server callback:

```python
def callback(self, request, response):
```

Yahan do separate objects/roles hain.

---

# Related

- [[Request Object]]
- [[Response Object]]
- [[Service Interface]]
