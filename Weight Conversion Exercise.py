weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
if(( unit == 'L') or (unit == 'l')):
    print('Weight in Kg: ', (float(((float(weight))/2.2))))
elif ((unit == 'K') or (unit == 'k')):
    print('Weight in Lbs: ', (float(weight)*2.2)
