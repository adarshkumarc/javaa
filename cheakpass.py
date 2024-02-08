correct_password='python'
max_attempts=3
attempts=0
while attempts<max_attempts:
    password=input("input the number:")
    if password==correct_password:
        print("welcome to python")
        break
    else:
        attempts+=1
        remaining_attempts=max_attempts-attempts
        if remaining_attempts >0:

print("incorrect the password {} ".format(remaining_attempts))
else:
print("incorrect password no more attampt")