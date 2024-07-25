# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.

def merge(nums1, m, nums2, n)
    nums1.slice!(m,n)
    nums2.each {|num| nums1 << num }
    nums1.sort!
    p nums1
end

merge([1,2,3,0,0,0], 3, [2,5,6], 3)

p "hi" while true