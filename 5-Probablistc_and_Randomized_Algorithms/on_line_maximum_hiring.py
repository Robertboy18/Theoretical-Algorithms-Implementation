def on_line_maximum(k,n):
    bestscore = -10e10
    for i in range(k):
        if score[i] > bestscore:
            bestscore = score[i]
    for i in range(k+1,n):
        if score[i] > bestscore:
            return i
    return n

score = [1,2,3,4,5,6,7,8,9,10]
print(on_line_maximum(3,10))