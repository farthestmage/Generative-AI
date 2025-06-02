def add_numbers(x, y):
  """Adds two numbers."""
  return x + y

if __name__ == "__main__":
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  sum_of_numbers = add_numbers(num1, num2)
  print("The sum is:", sum_of_numbers)