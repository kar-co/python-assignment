from datetime import date,datetime 

today = date.today() 
DOB = input("Enter Birthdate in yyyy-mm-dd format: ") 
dob = datetime.strptime(DOB, "%Y-%m-%d").date() 

print("Your birthdate is : ",dob,", :)") 
age_indays = (today- dob).days 
print("You are ",age_indays," days old. :)") 

years = today.year - dob.year 
months = today.month - dob.month 
days = today.day - dob.day 
if days< 0: 
months -= 1 
days += 30 
if months<0: 
years -=1 
months += 12 
print("You are", years, "years and", months, "months and ",days," days old.")