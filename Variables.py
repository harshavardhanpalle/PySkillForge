# 30 Days challenge python 
#python forge skills
#Python Variables
first_name="harsha"
last_name ='palle'
full_name = "harshapalle"
country ="india"
city="banglore"
age='24'
year='2002'
is_married = False
if_true = True
is_light_on = True
x,y,z='harsha ','is','bestprogrammer'

#datatypes of variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(if_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(z))

########
if len(first_name) >len(last_name):
    print(first_name)
else:print(last_name)

##
print(len(first_name))
####
num_one=5
num_two =3
total = num_one + num_two
print(f"total is {total}")
diff =num_one -num_two
print(f"difference is {diff}")
product =num_one*num_two
print(f"product id {product}")
remainder=num_one%num_two
print(f"Remainder is {remainder}")
exp = num_one**num_two
print(f"power of two variables is   {exp}")
floor_division= num_one//num_two
print(f"floor division is { floor_division}")
#############
help('keywords')

####
#area of circle
#radius of circle is 30 given
#area of cirlce is pi r**2 
#pi value is 3.14


"""radius =30
area_of_circle=3.14*radius**2
print(area_of_circle)
#circumference of circle is 2 pi r
radius = 30
pi=3.14
circum_of_circle =2*pi*radius
print(f"cricumference of circle is{circum_of_circle}")
#####"""
pi = 3.14
radius =int(input("enter the user radius: "))
area_fc = pi*radius**2
print(f"area of circle from user radius is{area_fc}")

#####
#using built in function to get user names and deatils
firstname =input("Enter User FirstName : ")
print(firstname)
lastname = input("Enter user LastName : ")
print(lastname)
county= input("enter the country : ")
print(country)
age = input("enter the age :")
print(age)
