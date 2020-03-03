'''Calculating the BMI using the formula weight/height^2'''

weight=int(input('Enter your weight (in kgs)'))
unit_of_height=input("What is your preferred unit of height? Type F for feet and inch  and  M for meters")
if unit_of_height=='F':
    print('You will enter your height given as feet and inches.')
    feet=int(input("First enter in feet"))
    inch=int(input("enter inch"))
    m=feet/3.2808
    meter_inch=inch*0.0254
    total_length=m+meter_inch
    print(total_length)
    bmi=weight/total_length**2
    print('the bmi is ',bmi)
    if bmi<18.5:
        print("underweight")
    elif 18.5<=bmi<25:
        print('normal')
    elif 25<=bmi<30:
        print('overweight')
    else:
        print("very-overweight")

if unit_of_height=='M':
    meter=int(input('Enter height in meter'))
    bmi=weight/meter**2
    print('jj')
    print("the bmi is ",bmi)
    if bmi<18.5:
        print("underweight")
    elif 18.5<=bmi<25:
        print('normal')
    elif 25<=bmi<30:
        print('overweight')
    else:
        print("very-overweight")
