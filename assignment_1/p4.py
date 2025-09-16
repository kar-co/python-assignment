import math

angles = [0, 30, 45, 60, 90]
print(f"Angle\tsin\tcos\ttan")

for angle in angles:
    rad = math.radians(angle)
    sin_val = round(math.sin(rad), 3)
    cos_val = round(math.cos(rad), 3)

    if(cos_val == 0):
        tan_val = "Undefined"
    else:
        tan_val = round(math.tan(rad), 3)

    print(f"{angle}\t{sin_val}\t{cos_val}\t{tan_val}")
