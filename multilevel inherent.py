class A:
    def read(self):
        print("READING")
class B(A):
    def display(self):
        print("DISPLAYING")
class C(B):
    def show(self):
        print("showing")
c1=C()# creating object for class C
c1.show()
c1.display()
c1.read()
b1=B() # creating object for class B
b1.display()
b1.read()
a1=A()
a1.read()

