# Numerical Methods for Calculating Square Root

### Introduction

This Python script demonstrates the application of four different numerical methods to compute the square root of 2. The methods included are the Iterative Method, Bisection Method, Fixed-Point Iteration, and Newton's Method. Each method is implemented as a function, and the script showcases their use in calculating an approximation of √2 with specified tolerance levels.

### Methods Implemented

**1. Iterative Method**

The root_two function uses a simple iterative method to approximate the square root of 2. Starting from an initial guess (x0), the function repeatedly applies the formula x = (x / 2) + (1 / x) until the difference between successive approximations is less than the specified tolerance.

**2. Bisection Method**

The bisection_method function implements the bisection method, a root-finding technique that repeatedly bisects an interval and then selects a subinterval in which a root must lie for further processing. It is applied to the function f(x) = x^2 - 2, which has a root at √2.

**3. Fixed-Point Iteration**

The fixed_point_iteration function uses the fixed-point iteration method, where a function g(x) is iteratively applied to an initial guess to converge to a fixed point. Here, g(x) = 1 + 1/x is used, which converges to the square root of 2 when iterated with a proper initial guess.

**4. Newton's Method**

The newton_method function applies Newton's method (or Newton-Raphson method), a powerful technique for finding successively better approximations to the roots (or zeroes) of a real-valued function. The function f(x) and its derivative df(x) are defined to apply this method to find the square root of 2.

### Execution and Results

The script runs all four methods sequentially to find the square root of 2. For each method, the script prints the process of iteration and the final result along with the number of iterations it took to converge to the result within the specified tolerance.

