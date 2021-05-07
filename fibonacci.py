# This is a sample Python script for Fibonacci.
# Python program to generate Fibonacci series until 'n' value
def fibinacciSeries(n):
  a, b, sum, count = 0, 1, 0, 1
  result = []

  if n >= 0:
   while count <= n:
      count += 1
      a = b
      b = sum
      sum = a + b
      result.append(b)
   return result
  else:
    print("Please Enter the Positive Number")

def main():
  try:
    n = int(input("Enter the Numeric Value : "))
    print(fibinacciSeries(n))
  except:
    print("Please Enter Number ")

if __name__ == '__main__': main()



