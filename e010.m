format long

prime_array = [];
for k = 1:2000000 - 1
    if isprime(k)
        prime_array(end+1) = k;
    end
end
disp(sum(prime_array))
