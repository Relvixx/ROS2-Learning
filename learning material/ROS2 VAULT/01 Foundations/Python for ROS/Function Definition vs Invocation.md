---
type: concept
status: verified
depth: must-know
language: Hinglish
---

# Function Definition vs Invocation

Ye concept Node se pehle clear kiya gaya tha kyunki ROS code me functions aur callbacks baar-baar aate hain.

---

# Function define karna

```python
def say_hello():
    print("Hello")
```

Is line se function **define** hua.

Abhi `Hello` print nahi hoga.

Mental model:

> Function definition = future ke liye instructions ko ek naam ke andar store karna.

---

# Function invoke/call karna

```python
say_hello()
```

Ab stored instructions execute hongi.

Mental model:

> Function invocation = stored instructions ko actually run karna.

---

# Important ROS connection

Future me ye distinction bahut important bana:

```python
self.callback
```

vs

```python
self.callback()
```

First:

```text
callback ka reference
```

Second:

```text
callback ko abhi call karo
```

ROS registration APIs me aksar **reference** diya jata hai taaki ROS event aane par callback ko later call kare.

---

# `main()` connection

```python
def main():
    ...
```

sirf definition hai.

`main()` tab execute hota hai jab koi usko call kare.

See [[main Function]].

---

# Knowledge Check Mental Model

```text
def xyz():
    ...
```

= instructions store

```text
xyz()
```

= instructions execute

---

# Related

- [[main Function]]
- [[__name__ and __main__]]
- [[Node Runtime Flow]]
