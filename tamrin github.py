def cheragh():
    n = int(input())
    s = int(input())
    c = 0 
    for _ in range (n-1):
        s2 = int(input())
        if s2 != s :         
            c +=1
        s = s2
    print(c)
cheragh()





def digit_number(n):
    m = 0
    while n >=10:
        n = sum(int(digit) for digit in str(n))
        return n
n = int(input())
for i in range(n):
    n = sum(int(digit) for digit in str(n))
print(n)
