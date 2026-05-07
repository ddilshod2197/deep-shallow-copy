# Immutable object
class ImmutableObject:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Mutable object
class MutableObject:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def change_value(self, new_value):
        self.value = new_value

# Immutable object o'zgarmasligini tekshirish
immutable_obj = ImmutableObject(10)
print(immutable_obj.get_value())  # 10
try:
    immutable_obj.value = 20
except AttributeError:
    print("Immutable object o'zgarmas")

# Mutable object o'zgarishi mumkinligini tekshirish
mutable_obj = MutableObject(10)
print(mutable_obj.get_value())  # 10
mutable_obj.change_value(20)
print(mutable_obj.get_value())  # 20
```

```python
# Immutable object
class ImmutableObject:
    def __init__(self, value):
        self.value = value

# Mutable object
class MutableObject:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def change_value(self, new_value):
        self.value = new_value

# Immutable object o'zgarmasligini tekshirish
immutable_obj = ImmutableObject(10)
print(immutable_obj.get_value())  # 10
try:
    immutable_obj.value = 20
except AttributeError:
    print("Immutable object o'zgarmas")

# Mutable object o'zgarishi mumkinligini tekshirish
mutable_obj = MutableObject(10)
print(mutable_obj.get_value())  # 10
mutable_obj.change_value(20)
print(mutable_obj.get_value())  # 20
