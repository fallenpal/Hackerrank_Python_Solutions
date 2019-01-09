n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    foo = input()
    command = 's.{0}({1})'.format(*foo.split(), ' ')
    eval(command)

print(sum(s))
