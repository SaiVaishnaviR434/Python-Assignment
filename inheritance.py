
# Superclass A
class A:
    def __init__(self):
        self.value = "Value in A"

    def method1(self):
        print("A: method1")

    def method2(self):
        print("A: method2")

    def common(self):
        print("A: common (overridden method)")

# Subclass B
class B(A):
    def __init__(self):
        super().__init__()
        self.value = "Value in B"  

    def method3(self):
        print("B: method3")

    def method4(self):
        print("B: method4")

    def common(self):
        print("B: common (overridden method)")

# Subclass C
class C(B):
    def __init__(self):
        super().__init__()
        self.value = "Value in C"  

    def method5(self):
        print("C: method5")

    def method6(self):
        print("C: method6")

    def common(self):
        print("C: common (overridden method)")


def main():
    print("=== Creating object of A ===")
    a = A()
    a.method1()
    a.method2()
    a.common()

    print("\n=== Creating object of B ===")
    b = B()
    b.method1()
    b.method2()
    b.method3()
    b.method4()
    b.common()

    print("\n=== Creating object of C ===")
    c = C()
    c.method1()
    c.method2()
    c.method3()
    c.method4()
    c.method5()
    c.method6()
    c.common()

    print("\n=== Runtime Polymorphism (Overridden Method) ===")
    ref: A

    ref = B()
    ref.common()  

    ref = C()
    ref.common()  

    print("\n=== Runtime Polymorphism with Data Members ===")
    ref = A()
    print("A ref to A object:", ref.value)

    ref = B()
    print("A ref to B object:", ref.value) 

    ref = C()
    print("A ref to C object:", ref.value)  

if __name__ == "__main__":
    main()
