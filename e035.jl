function is_prime(number)

  for k= 2:number-1
    if number % k == 0
      return false
    end
  end

  return true

end

function check_circular_prime(number)

  string_digit_vector = []
  number_string = string(number)
  for k = length(number_string):-1:1
    push!(string_digit_vector, string(number_string[k]))
  end

  # fill in with zeros...
  for k = 1:9 - length(string_digit_vector)
    push!(string_digit_vector, "-")
  end

  permutation_vector = []
  for a = 1:9
    reserved = [a]
    for b = 1:9
    reserved = [a]
      if b in reserved
        continue
      end
      reserved = [a, b]
      for c = 1:9
        reserved = [a, b]
        if c in reserved
          continue
        end
        reserved = [a, b, c]
        for d = 1:9
        reserved = [a, b, c]
          if d in reserved
            continue
          end
          reserved = [a, b, c, d]
          for e = 1:9
            reserved = [a, b, c, d]
            if e in reserved
              continue
            end
            reserved = [a, b, c, d, e]
            for f = 1:9
              reserved = [a, b, c, d, e]
              if f in reserved
                continue
              end
              reserved = [a, b, c, d, e, f]
              for g = 1:9
                reserved = [a, b, c, d, e, f]
                if g in reserved
                  continue
                end
                reserved = [a, b, c, d, e, f, g]
                for h = 1:9
                  reserved = [a, b, c, d, e, f, g]
                  if h in reserved
                    continue
                  end
                  reserved = [a, b, c, d, e, f, g, h]
                  for j = 1:9
                    if j in reserved
                      continue
                    end
                    temp_vector = []
                    push!(temp_vector, string(string_digit_vector[a]))
                    push!(temp_vector, string(string_digit_vector[b]))
                    push!(temp_vector, string(string_digit_vector[c]))
                    push!(temp_vector, string(string_digit_vector[d]))
                    push!(temp_vector, string(string_digit_vector[e]))
                    push!(temp_vector, string(string_digit_vector[f]))
                    push!(temp_vector, string(string_digit_vector[g]))
                    push!(temp_vector, string(string_digit_vector[h]))
                    push!(temp_vector, string(string_digit_vector[j]))
                    push!(permutation_vector, temp_vector)
                  end
                end
              end
            end
          end
        end
      end
    end
  end
  for k = 1: length(permutation_vector)
    deleteat!(permutation_vector[k], findall(x->x=="-", permutation_vector[k]))
  end
  counter_prime = 0
  for k = 1: length(permutation_vector)
    if is_prime(parse(Int64, join(permutation_vector[k])))
      counter_prime += 1
    end
  end
  return length(permutation_vector) == counter_prime
end

# println(is_prime(197))
# println(is_prime(179))
# println(is_prime(719))
# println(is_prime(791))
# println(is_prime(917))
# println(is_prime(971))
println(check_circular_prime(22))


# Note to self: read instructions properly. The question asks about rotations,
# not all permutations. That being said... I did learn a lot from this..

# question asks ex. 197, 971, 719.
# my program checks 197, 179, 719, 791, 917, 971.
# ... i.e. it looks at all permutations of a given number, instead of rotations.
# Circular primes do sound like they have to do with rotations,
# rather than with permutations... :l.


# Why does this work? HIER IS KEIN WARUM
