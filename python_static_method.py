# methods - Method is just a function object created by def statement.

class A:
   message = "class message"

   @classmethod
   def cfoo(cls):
      print(cls.message)

   def foo(self, msg):
      self.message = msg
      print(self.message)

   def __str__(self):
      return self.message

a=A()
print a.foo("instance call")  # instance call   None
print A.foo(a,"class call")  # class  call
print A.cfoo() # class message


