% Consecutive prime sum
clc; clear; close all;

bound = 100;
limit = 10^4;
list_primary = zeros(limit, 1);  % Fix list size to speed performance.
for k = 2:1:limit
    if isprime(k)
        list_primary(k) = k;
    end
end

list_prime = nonzeros(list_primary);    % Zeros are not primes.

max_prime = 0;
max_terms = 0;

searching = true;
for cut_off = 1: length(list_prime)
    for end_point = cut_off : length(list_prime)
        sum_of_terms = sum(list_prime(cut_off:end_point));
        if valid(sum_of_terms, bound)
            if length(list_prime(cut_off:end_point)) > max_terms
                max_prime = sum_of_terms;
            end
        end
    end
    % break if done
    if searching == false
        break
    end
    % break if done
    if searching == false
        break
    end
end

disp(max_prime)

% note: misinterpreted instructions? The sequence of primes does not
%       necessarily start at 2?

function validity = valid(potential_prime, bound)
primality = isprime(potential_prime);
bounded = potential_prime < bound;
if primality && bounded
    validity = true;
else
    validity = false;
end
end

% or maybe I didn't misinterpret the rules... 97 seems to be the one 
% beneath 100 with my interpretation, where the starting term doesn't
% have to be 2.
