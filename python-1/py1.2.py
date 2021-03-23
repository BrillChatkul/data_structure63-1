print(' *** Wind classification ***')
a = float(input('Enter wind speed (km/h) : '))
if a < 52 :
    print("Wind classification is Breeze.")
elif a < 56 :
    print("Wind classification is Depression.")
elif a < 102 :
    print("Wind classification is Tropical Storm.")
elif a < 209 :
    print("Wind classification is Typhoon.")
elif a >= 209 :
    print("Wind classification is Super Typhoon.")

