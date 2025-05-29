thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
x = 2
for x in range(50):
    print(next(myiter))  =       StopIteration
2/0  =                           ZeroDivisionError
assert x==4, "x should be 2"  =  AssertionError
import aaa  =                    ImportError
thisdict['']  =                  KeyError
for i in s  =                    SyntaxError
if 1 in []:
print("")  =                     IndentationError
x + 1  =                         TypeError
