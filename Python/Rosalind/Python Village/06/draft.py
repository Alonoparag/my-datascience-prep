from collections import Counter

def answer(s):
    count = Counter(s.split(' '))
    ans = ''
    for key in count.keys():
        ans+='%s %d\n'%(key, count[key])
    print(ans[:-1])

answer(input('>>>'))