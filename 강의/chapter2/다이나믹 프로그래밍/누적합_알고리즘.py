
def get_sum(a, b):
    global psum
    return psum[b] - psum[a-1]

N = 9
arr = [0,1,3,10,-2,3,-4,10,3,8]
psum = [0] * (N+1)

for n in range(1, N+1):
    psum = psum[n-1] + arr[n]
    
print(get_sum(3, 9))