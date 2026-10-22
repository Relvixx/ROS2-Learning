---
type: comparison
status: verified
language: Hinglish
---

# `setup.py` vs `package.xml` for Launch

Dono ka launch chapter me different role.

---

# `setup.py`

```text
Launch FILES ko install/package output me include karta hai.
```

Relevant:

```python
glob('launch/*.launch.py')
```

---

# `package.xml`

Learned dependencies:

```xml
<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
```

Role:

```text
launch-related software/runtime dependencies declare karna
```

---

# Mental Model

```text
setup.py
→ meri launch files install karo

package.xml
→ mujhe launch software dependencies chahiye
```

Same job nahi.
