#!/opt/homebrew/bin/python3
import time
from numba import jit, njit, prange

@jit
def testFor(n: int, m: int):
  for x in prange(n):
    for y in prange(m):
      pass

@jit
def testWhile(n: int, m: int):
  y = 0
  while y < n:
    x = 0
    while x < m:
      x = x + 1
    y = y + 1

if __name__ == '__main__':
  oldTime = time.perf_counter()
  testFor(20100, 2800)
  print(time.perf_counter() - oldTime)
