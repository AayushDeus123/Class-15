#Finding circumference of a circle
r = int(input('Enter the radius : '))

pi2 = 6.28319
def c(pi2, r):
    return(pi2 * r)
print('The Circumference of the Circle is :',c(pi2 , r),'cm')


#Finding Perimeter of Square
ps = int(input('\nEnter the length of one side (Square) : '))
def p(ps):
    return (4*ps)
print('The Perimeter of the Square is :',p(ps))


#Finding Perimeter of rectangle
pl = int(input('\nEnter the Length of the rectangle : '))
pw = int(input('Enter the Width of the rectangle : '))
def q(pl,pw):
    return(2*pl + 2*pw)
print('The Perimeter of the Rectangle is : ',q(pl,pw))