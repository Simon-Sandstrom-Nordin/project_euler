a = 1
b = 1
c = 1

searching = true
limit = 1000
while searching

  while a < limit
    global b = 1
    global c = 1

    while b < limit

      global c = 1
      while c < limit


        if (a^2 + b^2 == c^2)

          if (a + b + c == 1000)

            global searching = false
            println("--FOUND--")
            println("a:", a)
            println("b:", b)
            println("c:", c)

          end

        end

      if (searching == false)
      break
      end

      global c += 1
      end

    if (searching == false)
    break
    end

    global b += 1
    end

  if (searching == false)
  break
  end

  println("counter is ", a, " out of ", limit)
  global a += 1
  end


end

product = a*b*c
println("Answer: product abc is ", product)
