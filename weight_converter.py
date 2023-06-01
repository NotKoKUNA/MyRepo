#WEIGHT CONVERTER

weight = int(input("Weight: "))
type = input("(K)g or (L)bs: ")

if type.upper() == 'L':
    convert = weight * 0.45
    print("Weight in Kg: " + str(convert))
else:
    convert = weight / 0.45
    print("Weight in Lb: " + str(convert))