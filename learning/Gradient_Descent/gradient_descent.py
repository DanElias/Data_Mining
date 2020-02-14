import math

# f(x) = log(x) * log(x)

def fn(x):
  # return math.pow((math.log(x)), 2)
  return x*x + 4*x + 9

def derivative_fn(x):
  # return 2.0 * math.log(x) / x
  return 2*x + 4

x = 2 # initial value
learning_rate = 0.1

print ("Starting at", "x:", x, "x^2 + 4x + 9:", fn(x))

for step in range(20):
  x = x - learning_rate * derivative_fn(x) 
  print("step", step + 1, "x:", x, "x^2 + 4x + 9:", fn(x))