p1="free"
p2="click this link"
p3='offer'
message=input("enter your message: ")
if(p1 in message or p2 in message or p3 in message):
    print('this is a spam message ')

else:
    print('this is not a spam')