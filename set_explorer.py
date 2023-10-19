#!/usr/bin/env python3

a = set('3 14 15 9 26 5 35 9')  
b = set('60 22 14 0 9')

message = "difference"
print(a - b , message)

message = "intersection"
print(a , b , message)

message = 'union'
print(a | b , message)

message = 'symmetrical difference'
print(a ^ b , message)
