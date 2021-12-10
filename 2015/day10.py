def lookandsay(x):
    counts = []
    nums = []
    for i in x:
        if len(nums) != 0:
            if i == nums[-1]: counts[-1] += 1
            else:
                nums.append(i)
                counts.append(1)
        else:
            nums.append(i)
            counts.append(1)
        #print(nums, counts)
    return ''.join([str(counts[i])+nums[i] for i in range(len(counts))])

x = '1321131112'
#x = '1'
for i in range(50):
    x = lookandsay(x)
print(len(x))