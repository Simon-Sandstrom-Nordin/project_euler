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

  if k == num_2 && (k < 10000-1 || num_1 < 10000-1)

    global sum_of_amicable_numbers += k + num_1

    # both numbers accounted for
    if k in vector && num_1 in vector
      continue
    end

    # one number unaccounted for
    if k in vector || num_1 in vector

      if k in vector && k < 10000 - 1
        push!(vector, num_1)
      end

      if num_1 in vector && num_1 < 10000 - 1
        push!(vector, k)
      end

      continue

    end

    # neither number accounted for
    if num_1 < 10000 - 1
      push!(vector, num_1)
    end

    # incase the numbers are equal
    if k == num_1
      continue
    end

    if k < 10000 - 1
      push!(vector, k)
    end

  end

end

println(vector)
println(sum(vector))
println(sum_of_amicable_numbers)


# Well, I tried : I
