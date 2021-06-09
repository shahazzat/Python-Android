from . import Application
from rubicon.java import JavaClass
from testpkg.hello import *

activity_class = JavaClass('org/beeware/android/MainActivity')
app = Application()
activity_class.setPythonApp(app)
print('Python app launched & stored in Android Activity class')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.age)

hello()