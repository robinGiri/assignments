#1 ask a num with user and filter and add into the old list :
odd_list = []
def filter_odd_even(user_provided_number):
  for num in range(1, user_provided_number + 1):
      if num % 2 == 0:
         odd_list.append(num)

any_number = int(input(f"Please provide odd number: "))
filter_odd_even(any_number)
print(f"Now, the odd list is: {odd_list}")

#2 ask a num with the user and filter even and add into the even list :

even_lits = []
def filter_odd_even(user_provided_number):
  for num in range(1, user_provided_number + 1):
      if num % 2 == 0:
         even_lits.append(num)

any_number = int(input(f"Please provide even number: "))
filter_odd_even(any_number)
print(f"Now, the odd list is: {even_lits}")
#3 ask a age with user and check he/she is eligible for vote(must be greater than 19) or not

age = int(input("Please enter your age: "))

if age > 19:
  print("you are eligible for vote")
else:
    print("you are not eligible to vote")



#Application of loop into the weeks of day :
# for example :
        #Day 1 is --> Sunday
        #Day 2 is --> Monday

days_in_week = [
  "Sun",
  "Mon",
  "Tues",
  "Wed",
  "Thurs",
  "Frid",
  "Sat"
]

counter = 0
for day in days_in_week:
  counter += 1
  print(f"The {counter} of the day is: {day}")
#5Ask a first_name and second_name from user and return its full name as :
    # for example : oh! So, your full name is : John Doe

first_name, last_name = input("Enter first and last name (comma separated): ").split(",")

print(f"hi!, my name is {first_name} {last_name}")