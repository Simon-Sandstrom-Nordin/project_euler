function [primes] = e027_help(a, b)

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
