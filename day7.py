def encode(letter, number): 
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    newstr = ""
    for i in letter:
        total = (alphabets.index(i) + number)%26
        newstr += alphabets[total]  
    
    print(newstr)


def decode(letter, number): 
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    newstr = ""
    for i in letter:
        total = (alphabets.index(i) - number)%26
        newstr += alphabets[total]  
    
    print(newstr)



name=input("Enter msg")
num=int(input("Enter shift number"))
user=input("encode or decode")
if user=="encode":
    encode(name, num)
else:
    decode(name, num)





