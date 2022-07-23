clc; close all; clear;

max_prime = 0;
product = 0;

for a = -999:999
    for b = -1000:1000
        prime_amount = e027_help(a, b);
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
