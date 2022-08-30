% combinatoric selections
clc; clear; close;

% check to see that my own function is correct. It was correct :).
% nchoosek(15,13)
% nCr(15,13)

counter = 0;
for n = 1:100
    for k = 1:n
        combinations = nCr(n,k);
        if combinations > 10^6
            counter = counter + 1;
        end
    end
end
disp(counter)

function combinations = nCr(n,r)
n_factorial = factorial(n);
r_factorial = factorial(r);
n_minus_r_factorial = factorial(n-r);
combinations = n_factorial/(r_factorial*n_minus_r_factorial);
end
