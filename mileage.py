print("How many km did you cycle today?")
kms = input()
miles = float(kms)/1.60934 # you can round this using round()
miles = round(miles, 2) # sets floated miles to 2 decimal points
# print("Ok, you said " + miles) this wont work because you cant concat float to str
print(f"Your {kms}km ride is {miles} miles") # need to use format f