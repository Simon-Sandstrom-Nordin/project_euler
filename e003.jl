# Function stolen from internet, but I kind of understand it :).
function is_prime(num)
    is_prime_boolean = true
      for i in 2:num-1
          if num % i == 0
              is_prime_boolean = false
              break
          end
      end
    return is_prime_boolean
end

number = 600851475143

sqrt_number = floor(sqrt(number))

max_prime = 0

for i in 1:sqrt_number
    if is_prime(i) == true
        if number % i == 0
            println(i)
            global max_prime = i
        end
    end
end

print("Max prime is")
print(max_prime)
