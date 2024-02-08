a=10
def mainfunc():
    global a
    print(a)
    a=100
mainfunc()
print(a)