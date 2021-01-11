

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    fishes = 0
    s = []

    for i in range(len(A)):
        a = A[i]
        b = B[i]
        if b == 0:
            if not s:
                fishes +=1
            else:
                while s and a > s[-1]:
                    s.pop()
                if not s:
                    fishes += 1
        else:
            s.append(a)
            
    return fishes + len(s)

