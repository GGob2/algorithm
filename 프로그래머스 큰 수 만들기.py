def solution(number, k):
    stack = []

    for n in number:
        while stack and stack[-1] < n and  k > 0:
            stack.pop()
            k-=1
        stack.append(n)

    if k > 0:
        stack = stack[:-k]
    
    answer = "".join(stack)
    return answer

print(solution("1924", 2))

name = [[1,2,4], [3,4,2]]

print(len(name), len(name[0]))
