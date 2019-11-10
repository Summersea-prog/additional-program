year = int(input("Year = "))
if year%4==0 and year%100!=0 or year%400==0:  #if year is divisible by 4 and not divisible by 100 leap year. for century year must be divisible by 4  and 400 therefore it will check for year%100 for century year then check for year %=400
	print(year, " is a leap year")
else:
	print(year, " is not a leap year")