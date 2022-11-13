#Nested if - else

x=int(input("Enter the element you want to :"))
if x>=0:
    if x==0:
        print('It is zero')
    else:
        print('+ve Number')
else:
    print('-ve Number')


y=int(input("Enter the element you want to :"))
if not y>=0:
    print("-ve Number")
else:
    print('+ve Number')