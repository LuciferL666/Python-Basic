years = float(input())
gender = input()

if gender == 'm' and years >= 16:
        print("Mr.")
elif gender == 'm' and years < 16:
        print("Master")

if gender == 'f' and years >= 16:
        print("Ms.")
elif gender == 'f' and years < 16:
        print("Miss")
