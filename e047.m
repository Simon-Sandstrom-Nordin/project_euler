% Distinct prime factors
clc; clear; close all;

counter = 1;
searching = true;
while searching
    counter_prime = counter + 1;
    counter_prime_1 = counter + 2;
    counter_prime_2 = counter + 3;

    % if either counter or counter prime is prime (haha) then this
    % is useless, since at least one will only have one prime factor.
    if isprime(counter) || isprime(counter_prime) ...
            || isprime(counter_prime_1) || isprime(counter_prime_2)
        counter = counter + 1;
        continue
    end

    % luckily, matlab has a built in function that returns the prime
    % factors of a number, in an array. factor(n)
    prime_factors_in_counter = unique(factor(counter));
    prime_factors_in_counter_prime = unique(factor(counter_prime));
    prime_factors_in_counter_prime_1 = unique(factor(counter_prime_1));
    prime_factors_in_counter_prime_2 = unique(factor(counter_prime_2));

    % finding number of distinct factors, using set theory here.
    intersection = intersect(prime_factors_in_counter, ...
        prime_factors_in_counter_prime);
    intersection = intersect(intersection, ...
        prime_factors_in_counter_prime_1);
    intersection = intersect(intersection, ...
        prime_factors_in_counter_prime_2);

    distinct_in_counter = setdiff(prime_factors_in_counter, intersection);
    distinct_in_counter_prime = setdiff(prime_factors_in_counter_prime, ...
        intersection);
    distinct_in_counter_prime_1 = ...
        setdiff(prime_factors_in_counter_prime_1, intersection);
    distinct_in_counter_prime_2 = ...
        setdiff(prime_factors_in_counter_prime_2, intersection);

    if length(distinct_in_counter) >= 4 && ...
            length(distinct_in_counter_prime) >= 4 && ...
            length(distinct_in_counter_prime_1) >= 4 && ...
            length(distinct_in_counter_prime_2) >= 4
        disp("First number is: " + counter)
        disp("Factors are: ")
        disp(prime_factors_in_counter)
        disp("Second number is: " + counter_prime)
        disp("Factors are: ")
        disp(prime_factors_in_counter_prime)
        disp("Third number is: " + counter_prime_1)
        disp("Factors are: ")
        disp(prime_factors_in_counter_prime_1)
        disp("Fourth number is: " + counter_prime_2)
        disp("Factors are: ")
        disp(prime_factors_in_counter_prime_2)
        searching = false;
    end

    counter = counter + 1;
end

% ez

%First number is: 134043
%Factors are: 
%     3     7    13   491
%
%Second number is: 134044
%Factors are: 
%     2    23    31    47
%
%Third number is: 134045
%Factors are: 
%     5    17    19    83
%
%Fourth number is: 134046
%Factors are: 
%     2     3    11   677