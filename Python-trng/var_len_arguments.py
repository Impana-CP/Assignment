def greatest(*nums):
    great = nums[0]
    for e in nums:
        if e > great:
            great = e
    return great


print(greatest(1, 2, 4, 3, 5))
print(greatest(100, 1, 30, 50))
print(greatest(1, 20, 4, 3))
print(greatest(-1, -2, -4, -3, -5))
