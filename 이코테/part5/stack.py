"""
스택의 개념이해와 기본적인 스택 구현
"""
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
# [5,2,3,7]

stack.pop()
# [5,2,3]

stack.append(1)
stack.append(4)
# [5,2,3,1,4]

stack.pop()
# [5,2,3,1]

print(stack)
