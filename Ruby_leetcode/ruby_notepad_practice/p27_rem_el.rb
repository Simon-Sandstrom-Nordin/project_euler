# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, val)
  counter = 0
  nums.each_with_index do |num, index|
    if num == val
      counter += 1
      nums[index] = Float::INFINITY
    end
  end
  nums.sort!
  return counter
end

int_arr = [1,2,3,4,5, 4]
val = 4
puts remove_element(int_arr, val)

