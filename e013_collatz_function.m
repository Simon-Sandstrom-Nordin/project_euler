function [collatz] = e013_collatz_function(number)
if mod(number, 2) == 0
    collatz = number / 2;
    return
end
collatz = 3 * number + 1;
end
