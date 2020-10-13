import numpy

N = int(raw_input())
A = numpy.array([ map(int, raw_input().split()) for i in range(N) ])
B = numpy.array([ map(int, raw_input().split()) for i in range(N) ])

print numpy.dot(A, B)
