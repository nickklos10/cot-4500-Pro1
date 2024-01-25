def root_two():
  x0 = 1.5
  tol = 0.000001
  iter = 0
  diff = x0
  x = x0

  print("Iterative Method for Square Root of 2:")
  print(f"{iter}: {x}")

  while diff >= tol:
    iter += 1
    y = x
    x = (x / 2) + (1 / x)
    print(f"{iter}: {x}")
    diff = abs(x - y)

  print(f"\nConvergence after {iter} iterations\n")


def bisection_method(f, a, b, tol, max_iter):
  left = a
  right = b
  iter = 0
  p = None

  while abs(right - left) > tol and iter < max_iter:
    iter += 1
    p = (left + right) / 2
    if f(left) * f(p) < 0:
      right = p
    else:
      left = p

  return p


def f(x):
  return x**2 - 2


def fixed_point_iteration(g, p0, TOL, N0):
  i = 1
  while i <= N0:
    p = g(p0)
    if abs(p - p0) < TOL:
      return p, "SUCCESS"
    i += 1
    p0 = p
  return "FAILURE"


def g(x):
  return 1 + 1 / x


def newton_method(f, df, initial_approximation, TOL, max_iterations):
  p_prev = initial_approximation
  for i in range(1, max_iterations + 1):
    if df(p_prev) == 0:
      return "FAILURE", "Derivative was zero"

    p_next = p_prev - f(p_prev) / df(p_prev)

    if abs(p_next - p_prev) < TOL:
      return p_next, "SUCCESS"

    p_prev = p_next
  return "FAILURE", "Maximum iterations reached"


def df(x):
  return 2 * x


# Run all four methods and print their results.
root_two()
root_bisect = bisection_method(f, 1, 2, 1e-6, 100)
print(f"Bisection Method Result: {root_bisect}\n")
result_fixed_point = fixed_point_iteration(g, 1.5, 1e-6, 100)
print(f"Fixed Point Iteration Result: {result_fixed_point}\n")
newton_result = newton_method(f, df, 1.5, 1e-6, 100)
print(f"Newton's Method Result: {newton_result}\n")
