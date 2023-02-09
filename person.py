class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def __str__(self):
        return f'名前は{self._name}年齢は{self._age}'
    def __repr__(self):
        return f'Person("{self._name}",{self._age})'
p=Person('Alice',10)
print(str(p))
print(repr(p))
p2=eval(repr(p))
print(str(p2))