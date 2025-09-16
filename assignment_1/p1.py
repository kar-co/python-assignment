from datetime import date

d1 = date(2025, 9, 13)
d2 = date(2025, 9, 10)

diff = d1 - d2
print("Difference ", diff.days, " days")