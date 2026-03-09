# A happy number is a number that eventually becomes 1 after repeating a special process.
# The process
# Take a number.
# Square each digit.
# Add the squares.
# Repeat the process with the new number.
# n = 19
# 1² + 9²
# = 1 + 81
# = 82

# 8² + 2²
# = 64 + 4
# = 68

# 6² + 8²
# = 36 + 64
# = 100

# 1² + 0² + 0²
# = 1

n = int(input("enter a number: ")) #19
while(n!=1 and n!=4):
    add=0
    while(n>0):
        rem = n%10 #19 % 10 = 9      # 1 % 10 = 1
        add=add+(rem**2) #add = 81     #82
        n=n//10  #1
    n=add
if (n==1):
    print("Happy number")
else:
    print("not happy")
