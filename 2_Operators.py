age = 24
height= 1.79
a = 1 + 1j

print(type(a))

## area of triangle
base = float(input("enter the base of triangle :"))
height = float(input("enter the height :"))
area = 0.5 * base *height
print("area of triangle :",area)

###perimetr of triangle
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c :"))
perimeter = a+b+c
print("the preimeter of triangle is :",perimeter)

##area and perimeter of rectangle
length = float(input("enter the length :"))
width = float(input("enter the width:"))
area = length * width
perimeter = 2 * (length + width)
print("area of rectangle:",area)
print("perimeter of rectangle :",perimeter)


## area  of circle
radius = float(input("enter radius :"))
pi = 3.14
area = pi * radius *radius
print("area of circle :",area)
#circumference of circle is 2 pir
ci = 2*pi*radius
print("circumference of circle is:",ci)

###
##Calculate the slope, x-intercept and y-intercept of y = 2x -2
#y = mx+c
#m = 2 , c = -2
slope = m = 2
print("slope  :",slope)
c = -2
# for y intercept  x= 0
x=0
y = 2*x -2
y_intercept = (x , y)
print("Y-intercept is : ",y_intercept)

# for x intercept on x axis (y=0)
#here we can't get the value so y = mx+c
#y =0 then we have find x so the values we know is m and c
y = 0
x = -c /m
x_intercept = (x , y)
print("x- intercept is :",x_intercept) 
#
## 

slope1 = m = 2
import math
x1,y1 =(2,2)
x2,y2 = (6,10)
y3 = y2 - y1
x3= x2 - x1
slope  = y3 / x3
print("slope m :",slope)

# Euclidian Distance squrt((x2 - x1)**2+(y2 - y1)**2)
ed = math.sqrt((x3)**2 + (y3)**2)
print("Euclidian distance",ed)

if slope1 ==slope :
    print("equals")
else:print("not equals")


############
print(len("python"))
print(len('drGON'))
print("on" not in "python" and 'on' not in "dragon")
a = "I hope this course is not full of jargon"
print('jargon' in a)
b = "python"
print(float(len("python")) and str(len("python")))

##
num = int(input("enter number:"))
res = num % 2
if res == 0:
    print("even number ",res)
else:
    print("odd number",res)


###
if 7//3 == int(2):
    print("true")
else:
    print("false")

if type("10") ==type(10):
    print("true")
else:
    print("false")

if int(9.8) == int(10):
    print("true")
else:
    print("false")

###
hr = float(input("enter hours:"))
rate = float(input("enter rate:"))
week_earn = hr * rate
print("your weekly earning :",week_earn)

###
years=int(input("enter number of years you have lived :"))
#hr = 60 min ,min = 60sec,day=24 hrs year = 365 and 364
seconds = 24*60*60*365*years
print(seconds)

###
xval= list(range(-5,3))
for x in xval:
    y=x**2 + 6*x +9
    print('x =',x,'y =',y)


for i in range (1,6):
    print(i,1,i,i**2,i**3)
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""



#AGE Calculator

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor")
elif 18 <= age <= 33:
    print("You are a youth")
elif 34 <= age <= 60:
    print("You are an adult")
else:  # age >= 61
    print("You are a senior citizen")



#AREA CALCULATOR

Shape	    Formula	
Rectangle	 Area = length × width	
Square	    Area = side²	
Triangle	 Area = ½ × base × height	
Circle	     Area = π × radius²	"""
print("Choose an option to " \
"calculate area of which kind you have to calculate")
print("1.Rectangle")
print("2.Square")
print("3.Trianlge")
print("4.circle")
choice = int(input("Enter the choice  you have to calculate :"))
if choice == 1 :
    length = float(input("enter the length :"))
    width = float(input("enter the width :"))
    area = length * width
    print("The area of rectangle is:",area)
elif choice == 2 :
    side = float(input("Enter the side :"))
    area = side **2
    print("The area of circle is :",area)
elif choice ==3:
    base = float(input("Enter the base :"))
    height = float(input("Enter height:"))
    area = 1/2 * base * height
    print("Area of Triangle : ",area)
elif choice ==4:
    pi = 3.1416
    radius = float(input("Enter radius :"))
    area = pi * radius**2
    print("Area of circle :",area)
else :
    print("your choice is wrong")

