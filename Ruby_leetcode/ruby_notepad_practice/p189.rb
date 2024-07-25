# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
    
    to_be_put = nums[0]
    stored = nil;
    k.times do
    	nums.each_with_index do |num, ind|
        	if ind == 0
            		next
       		end
        	stored = nums[ind]
       		nums[ind] = to_be_put
		to_be_put = stored
    	end
        nums[0] = to_be_put
    end    
    return nums
end

# O(k*nums.length)
puts rotate([1,2,3,4,5,6,7], 3)