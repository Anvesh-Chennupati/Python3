"""
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])


"""
"""
def findDog(var):
    v1 = list(var.split(' '))
    for i in v1:
        if i == 'dog' or i == 'Dog':
            print('True')

findDog('Is there a dog here?')
"""
"""
You are driving a little too fast, and a police officer stops you.
Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
If your speed is 60 or less, the result is "No Ticket".
If speed is between 61 and 80 inclusive, the result is "Small Ticket".
 If speed is 81 or more, the result is "Big Ticket".
 Unless it is your birthday (encoded as a boolean value in the parameters of the function) --
 on your birthday, your speed can be 5 higher in all cases.
"""

def caught_speeding(speed, is_birthday):
    if is_birthday == True:
        if speed < 65:
            print('No Ticket')
        elif speed >65 and speed <= 85:
            print('Small Ticket')
        else:
            print('Big Ticket')
    else:
        if speed < 60:
            print('No Ticket')
        elif speed >60 and speed <= 80:
            print('Small Ticket')
        else:
            print('Big Ticket')

caught_speeding(62,False)


s = ['sam','sal','some','asv','werew','dfgfd']

print(list(filter(lambda word:word[0]=='s',s)))
