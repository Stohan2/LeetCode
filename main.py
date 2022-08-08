# This is a sample Python script.
import time
#3###############################################333
# s = "ggububgvfk"
# resa = ""
#
# max_len = 1 if s != "" else 0
# for ch in s:
#     if max_len <len(resa):
#         max_len = len(resa)
#     if ch in resa:
#         if resa[0] == ch:
#             resa = resa[1:] + ch
#         else:
#             resa = resa[resa.index(ch)+1:] + ch
#     else:
#         resa += ch
# if max_len < len(resa):
#     max_len = len(resa)
# print(max_len)

#4#########################################
time_start = time.time()
nums1 = [1, 2,5,9,10,15]
nums2 = [1,5,9,11,20]

merg = []
leng = len(nums1)+len(nums2)
i = 0
j = 0
while i+j < leng:
    if i<len(nums1) and j<len(nums2):
        if nums1[i] > nums2[j]:
            merg.append(nums2[j])
            j += 1
        elif nums1[i] < nums2[j]:
            merg.append(nums1[i])
            i += 1
        else:
            merg.append(nums2[j])
            merg.append(nums1[i])
            i, j = i + 1, j + 1
    elif not i<len(nums1):
        merg.append(nums2[j])
        j += 1
    elif not j<len(nums2):
        merg.append(nums1[i])
        i += 1
b =len(merg)
if len(merg) % 2:
    mean = merg[int(b//2)]
else:
    mean = (merg[int(b//2)]+merg[int(b//2)-1])/2
time_finish = time.time()
print(merg)
print(mean)
print("timepast", round(time_finish-time_start, 9))