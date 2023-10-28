#!/usr/bin/env python3

a = set('a t g g g g g g g t t')  
b = set('a a a a t t c c g')

message = "difference"
print(a - b , message)

message = "intersection"
print(a , b , message)

message = 'union'
print(a | b , message)

message = 'symmetrical difference'
print(a ^ b , message)
