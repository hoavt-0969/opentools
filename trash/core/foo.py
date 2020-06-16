


class Foo(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a +self.b
    
    def run(self):
        c = self.sum()
        print(c)


# if __name__ == "__main__":
#     s = Foo(20,10)
#     s.run()

# s = Foo(10,20)

# s.run()