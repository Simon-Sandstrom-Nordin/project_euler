% Square root conergents
clc; clear all; close all; format rat;

number = 1; list = [];
for k = 1:1000
    number = iteration(number);
    list(end + 1) = number;
end
disp(list')

function value = iteration(number)
value =  1 + 1 / (1 + number);
end

% Another problem in MATLAB: the format rat doesn't... it
% doesn't... it just uses the same quotient over and over.
