# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    
	ha = Hash.new(0)
		nums.each do |num|
		ha[num] += 1
	end
    
	ha.each do |key, value|
		if value > nums.length / 2
			return key
		end
	end


end

nums = [3,2,3]
puts majority_element(nums)