from sys import stdin, stdout
a,b,c,d = map(int, stdin.readline().split())

stdout.write(str((c*60 +d) - (a*60 + b)))