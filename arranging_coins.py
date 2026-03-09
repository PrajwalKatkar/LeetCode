# You have to arrange the coins in rows such that:
# 1st row → 1 coin
# 2nd row → 2 coins
# 3rd row → 3 coins
# 4th row → 4 coins
# and so on…

# n = 8 coins
# Arrange:

# Row 1 → 1 coin → remaining 7
# Row 2 → 2 coins → remaining 5
# Row 3 → 3 coins → remaining 2
# Row 4 → needs 4 coins ❌

#  Total complete rows = 3

n= int(input("Enter a number: ")) 
rows=1 
remaining=n
while(remaining>=rows):  
    remaining= remaining-rows  
    rows=rows+1       

print(rows-1)

