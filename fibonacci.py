prevNum = 1 
newNum = 1 
total = 0  
while prevNum <= 4000000:  # The previous number should not exceed 4000000 so this loop runs until the prevNum value is less than 4mill
    if prevNum % 2 == 0:  # Checking if the prevNum is even or odd if even
        total += prevNum   # it is added to the total
    newNum = prevNum              # fibonacci series
    prevNum = prevNum+newNum      # as shown in the algorithm
print(total) 
