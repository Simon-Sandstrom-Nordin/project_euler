clc; close all; clear;

max_prime = 0;
product = 0;

for a = -999:999
    for b = -1000:1000
        prime_amount = e027_test_function(a, b);
        if prime_amount > max_prime
           max_prime = prime_amount; 
           product = a*b;
        end
    end
    
    if mod(a, 100) == 0
        disp(a)
    end
end

disp("maximum prime is " + max_prime)
disp("product is " + product)

function [primes] = e027_test_function(a, b)

f = @(n) n^2 + a*n + b;
searching = true;
counter = -1;   % since I want to increment first thing I do...
primes = 0;

while searching
    counter = counter + 1;

    if f(counter) < 0   % this means it's not a prime... but
        break           % isprime() doesn't take negative inputs.
    end

    if isprime(f(counter)) == false
        break
    end

end

primes = counter;
end
