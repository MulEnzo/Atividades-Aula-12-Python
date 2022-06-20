class A:
    def	m1(self):
        print('Método de A')

class B(A):
    def m2(self):
        print('Método de B')

class C(A):
    def	m2(self):
        print('Método de C')


class D(B, C):
    pass


if __name__ == '__main__':

    d = D()

    d.m1()

    d.m2()

    print(D.__mro__)