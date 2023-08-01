user_name=input("Enter your full name:")
mobile_num=input("""Enter your mobile number *your mobile number should be according to this format(05x-xxxx-xxx)* :""")
year_of_birth=input("Enter year of birth:")
year_of_birth=int(year_of_birth)
user_current_age=2023-year_of_birth
print(user_name)
print(user_current_age)
print(mobile_num.split("-"))
