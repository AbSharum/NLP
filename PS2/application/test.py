import math
def softmax(out):
    e = math.e
    temp = [0] * len(out)
    k = 0
    for i in out:
        curr = 0
        for j in out:
            curr += math.pow(e,j)
        temp[k] = round(math.pow(e,i) / curr , 2)
        k += 1
    return temp
out = [.2,.75,.3]
probs = softmax(out)
for p in probs:
    print(p)
print(sum(probs))