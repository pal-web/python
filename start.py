n = int(input("enter the no"))
if n%2==0:
    print('even')
else:
    print("odd")

def pallindrome(word):
     return word==word[::-1]