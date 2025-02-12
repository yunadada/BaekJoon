import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
LOG = set()
for _ in range(n):
    name, log = input().split()
    if (log == 'enter'):
        LOG.add(name)
    else:
        LOG.discard(name)
result = sorted(LOG, reverse=True)
print('\n'.join(result))