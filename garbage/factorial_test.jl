function factorial(x)

if x == 1
  return 1
end

return x * factorial(x-1)

end

x = 5
res = factorial(5)
println(res)
