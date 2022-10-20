#!/usr/bin/env python3
import sys

PI = 3.1415926535897932384626433832795028841971693993751058209749445923
n = int(sys.argv[1])


class Math:
  # Exponentiate: x^b
  def exp(x, b):
    return x**b


  # Factorial: x!
  def fac(x: int):
    b = x
    j = 1
    while b != 0:
      j *= b
      b -= 1

    return j

  # Floor n.
  def floor(n) -> int:
    return int(n)


  # self explanatory.
  def cos(x) -> float:
    k = 0
    accuracy = 20
    
    # Check the wikipedia article on how this works.
    # https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
    for _k in range(accuracy):
      k += (Math.exp(-1,_k)/Math.fac((2*_k)))*(Math.exp(x, 2*_k))

    return k


def f(x):
  try:
    return Math.floor(Math.exp((Math.cos(((Math.fac(x-1)+1)/x)*PI)), 2))
  except OverflowError:
    print(f"Woops! {n} is too big!")
    sys.exit(4)

match f(n):
  case 1:
    print(f"{n} is prime!")
  case _:
    print(f"{n} is composite")