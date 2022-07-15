function proper_divisors(number)

  sum = 0

  for i in 1:number-1

    if number % i == 0

      sum += i

      end

  end

  return sum

end

sum_of_amicable_numbers = 0

vector = []

for k in 1:10000-1
# for k in 219:220

  num_1 = proper_divisors(k)
  num_2 = proper_divisors(num_1)
  both_are_less = k < 10000 && num_1 < 10000

  if k == num_2 && both_are_less && k != num_1  # d(a) = b, d(b) = a, a != b

    global sum_of_amicable_numbers += k + num_1

    # both numbers accounted for
    if k in vector && num_1 in vector
      continue
    end

    # one number unaccounted for
    if k in vector || num_1 in vector

      if k in vector
        push!(vector, num_1)
      end

      if num_1 in vector
        push!(vector, k)
      end

      continue

    end

    # neither number accounted for
    push!(vector, num_1)

    # incase the numbers are equal
    if k == num_1
      continue
    end

    push!(vector, k)

  end

end

println(vector)
println(sum(vector))
println(sum_of_amicable_numbers)


# Well, I tried : I
