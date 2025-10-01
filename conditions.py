user = int(input("Enter your age :"))
if user >= 18 :
    print(" you are old enough to learn to drive")
else:
    print(f"you need {18 - user}  more years  to learn to drive ")

my_age = int(input("enter age:"))
your_age =int(input("your age is :"))
if my_age == your_age :
    print(f"we both are of same age {my_age} ,{your_age}")
elif my_age > your_age :
    print(f"you are {my_age - your_age} younger to me")
else:
    print(f"you are {your_age - my_age } years older to me.")

              
my_age = 25   # You can change this to your actual age
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {diff} years older than you.")
else:
    print("We are the same age!") 

a = int(input("enter number (a) :"))
b = int(input("enter number (b) :"))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

### GRADEING SYSTEM
## Grade to Students According to Their Scores
marks = float(input("Enter Your Marks:"))

if marks >=90 and marks <= 100:
    print(f"Your {marks} marks ,Grade : A")
elif 70 <= marks <= 89:
    print(f"Your {marks} marks ,Grade : B")
elif 60 <= marks <= 69:
    print(f"Your {marks} marks ,Grade : C")
elif 50 <= marks <= 59:
    print(f"Your {marks} marks ,Grade : D")
else:
    print(f"Your {marks} marks ,Grade :F") 

mark = int(input("your marks :"))

if mark >= 0 and mark <= 49:
    print(f"Your {mark} marks ,Grade :F")
elif mark >= 50 and mark <= 59:
    print(f"Your {mark} marks ,Grade :D")
elif mark >= 60 and mark <= 69:
    print(f"Your {mark} marks ,Grade :C")
elif mark >= 70 and mark <= 79:
    print(f"Your {mark} marks ,Grade :B")
elif mark >= 80 and mark <= 100:
    print(f"Your {mark} marks ,Grade :A")
else:
    print("Your marks  are unvalid") 

# To check wheather 
#Autumn, Winter, Spring or Summer
month = input("Enter Month :")
if month in ["september" ,"october" , "november"]:
    print("Season is :Autumn")
elif month in ["december" , "january" , "february"]:
    print("Season is : Winter")
elif month in [ "april" , "may" , "march"]:
    print("Season is :Spring")
elif month in ["june" , "july" , "august"]:
    print("Season is :Summer")
else :
    print("You have entered invalid") 


fruits = ['banana', 'orange', 'mango', 'lemon']
print(type(fruits))
print(fruits[0])
fruits.append("jackfruit")
print(fruits)

person={
    'first_name': 'harsha',
    'last_name': 'palle',
    'age': 24,
    'country': 'India',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '517000'
    }
    }
print(person)

print(person['first_name'])

if "skills" in person:
    print(f"yues skills is present: {person["skills"]}")
    print(f"yes skill in skills is :{person["skills"][2]}")
else:
    print("skills not present in person Dict")


if "skills" in person:
        if "Python" in person["skills"]:
                print(f"yues skills is present: {person["skills"]}")
                print("yes python is presnt")
        else:
                print("no such skill python")
else:
        print("no such skills in person")

####
if person["skills"] ==["JavaScript","React"]:
    print("he is front end developer")
elif person['skills'] == ["Node","Python","MangoDB"] :
    print("he is a backed developer")
elif person["skills"] ==["React","Node","MangoDB"]:
    print("He os a fullstack developer")
else:
    print("he is full skilled person")



#####



person={
    'first_name': 'harsha',
    'last_name': 'palle',
    'age': 24,
    'country': 'India',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '517000'
    }
    }

if person['is_marred']== True:
    if person['country'] == "Finland":
        print(f"{person['first_name']} {person['last_name']} lives in {person['country']}.He is Married")
    else:
        print("person doesnot live in finland")
else:
    print("he is not marrieed")