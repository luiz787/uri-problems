"""Problem 1035 from URI Judge Online"""
# pylint: disable-msg=C0103
line = raw_input()
nums = map(int, line.split())
b_greater_than_c = nums[1] > nums[2]
d_greater_than_a = nums[3] > nums[0]
sum_cd_greater_than_ab = nums[2]+nums[3] > nums[0]+nums[1]
c_is_positive = nums[2] > 0
d_is_positive = nums[3] > 0
a_is_even = nums[0]%2 == 0
if b_greater_than_c and d_greater_than_a \
and sum_cd_greater_than_ab and c_is_positive \
and d_is_positive and a_is_even:
    print "Valores aceitos"
else:
    print "Valores nao aceitos"
