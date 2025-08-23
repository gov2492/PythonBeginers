
age = input("What is your age?")
age =int(age)
if age>=18:
    print("eligible for voting")
elif 16 <= age < 18:
    print("you must wait for {0} year to vote".format(str(18-age)))
else:
    print("Not eligible for voting");