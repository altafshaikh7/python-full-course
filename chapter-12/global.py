a=83

def fun():
    # global a  #global variable ko function ke andar access karne ke liye global keyword ka use karte hain
    a=100
    print(a)  #83

fun()
print(a)  #83