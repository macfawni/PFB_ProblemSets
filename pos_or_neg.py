#!/usr/bin/env python3
x = 6
if x > 0:
  message = "positive"
  print(message)
  if x < 50 and x % 2 == 0:
    message = "it is an even number that is smaller than 50"
    print(message)
if x < 0:
  message = "negative"
  print(message)
elif x == 0:
  message = "equals zero!"
  print(message)
