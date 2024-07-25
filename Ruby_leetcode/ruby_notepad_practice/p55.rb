# @param {Integer[]} nums
# @return {Boolean}
def can_jump(nums)
    max_reach = 0
    nums.each_with_index do |num, index|
      return false if index > max_reach
      max_reach = [max_reach, index + num].max
      return true if max_reach >= nums.length - 1
    end
    return false
end

puts can_jump([2,3,1,0,1])


