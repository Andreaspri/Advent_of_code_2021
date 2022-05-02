def raw():
    raw = [6,4,12,1,20,0,16]
    for i in raw:
        yield i

prev_nums = {}
nums = raw()
next_num = next(nums)
for i in range(1,30000001):
    if next_num in prev_nums.keys():
        temp = prev_nums[next_num]
        prev_nums[next_num] = i
        next_num = i - temp
    else:
        prev_nums[next_num] = i
        try: next_num = next(nums)
        except: next_num = 0
    if i == 2020:
        [print('Part 1:',k) for k,v in prev_nums.items() if v == 2020]
[print('Part 2:',k) for k,v in prev_nums.items() if v == 30000000]