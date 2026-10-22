---
type: python-reference
status: verified
language: Hinglish
---

# `os.path.join()` for Launch Destination

Code:

```python
os.path.join(
    'share',
    package_name,
    'launch'
)
```

If:

```python
package_name = 'my_first_pkg'
```

conceptual path:

```text
share/my_first_pkg/launch
```

---

# Role in `data_files`

```text
os.path.join(...)
→ destination

glob(...)
→ source files
```

This distinction Rahul correctly answered before first practical.
