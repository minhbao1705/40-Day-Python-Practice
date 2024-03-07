
import math
def quadratic_equation(a, b, c):
    x1=0
    x2=0
    theta=b*b - 4*a*c
    if theta > 0:
        x1 = (-b-math.sqrt(theta))/(2*a)
        x2 = (-b+math.sqrt(theta))/(2*a)
    elif theta == 0:
        x1=x2= -b/(2*a)
    elif theta < 0:
        print('Phương trình vô nghiệm')

    return (x1, x2)

a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))

x1, x2 = quadratic_equation(a, b, c)
print('x1 =', x1, 'x2 =', x2)