#!/usr/bin/env python3
x = 5
if x > 0:
  message = "positive"
  print(message)
  if x < 50:
    message = "it is less than 50"
    print(message)
if x < 0:
  message = "negative"
  print(message)
elif x == 0:
  message = "equals zero!"
  print(message)
