# Finding sum of digits of a non-negative number until sum becomes single digit

# Non-negative means 0 and positive numbers

def digSum(n): 
  # if n is 0
  if (n == 0):
    return 0
  # if n is positive
  # n % 9 works for non-multiples of 9
  # subtracting 1 and adding 1 accounts for multiples of 9
  # or you get 0 as the sum of the digits
  return (n - 1) % 9 + 1

print(digSum(987653))

# Source: http://www.sjsu.edu/faculty/watkins/Digitsum00.htm
# Main takeaway: ex) 12 % 9 = (1 + 2) % 9

# DigitSum(k) = (k-1) % 9 + 1
