class A:
    def read(self):
        print("I am reading\n")
    
class B(A):
    def write(self):
        print("I am writing")

s=B()
s.read()
s.write()
        
