import sys
sys.stdin = open('input.txt', 'r')
# sys가 stdin을 가지고 있는데 buffer에 저장될 값들을 local에 존재하는 input.txt
# I/O Devices에서 입력되는 값들은 buffer에 저장되고
# std.in 이라는 파일에서 읽어온다.
# text 파일을 read해서 keyboard input 처럼 사용한다 
def getMax(idx):
    tmax = heights[idx-2]

    if tmax < heights[idx - 1]: tmax = heights[idx - 1]
    if tmax < heights[idx + 1]: tmax = heights[idx + 1]
    if tmax < heights[idx + 2]: tmax = heights[idx + 2]
    return tmax

TC = 10
for tc in range(1, TC+1):

    N = int(input())
    heights = list(map(int, input().split()))
    view = 0

    for i in range(2, N-2):
        side = getMax(i)
        if side < heights[i] :
            view += heights[i] - side

    print(f"{tc} {view}")