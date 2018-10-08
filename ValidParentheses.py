related = {'{': '}', '[': ']', '(': ')'}
s = "){"
is_Valid = True
tmp = []
# 我看有点像是堆栈
# 定义一个list存放左边的括号
left = []
right = []
for ch in s:
    if ch in related.keys():
        left.append(ch)
    else:
        right.append(ch)
if len(left) != len(right):
    is_Valid = False
else:
    for ch in s:
        if ch in related.keys():
            tmp.append(ch)
        else:
            if len(tmp) == 0:
                is_Valid = False
                break
            if related[tmp[-1]] != ch:
                is_Valid = False
                break
            else:
                tmp.pop()
print(right)        
print(left)
print(is_Valid)