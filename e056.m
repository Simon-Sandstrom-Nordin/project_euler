% Powerful digit sum
clc; clear all; close all;

number = 10^23;
n = 0;  % number of digits
while (number/10^n) >= 1
    n = n + 1;
end
list_of_digits = zeros(n, 1);   % zeros to allocate memory
for i = 1:n
    k = number - floor(number/10^i)*10^i;   % number sin digit
    number = number - k;    % remove wanted digit
    list_of_digits(i) = k/10^(i-1); % add wanted digit to the list
end
sum_of_digits = sum(list_of_digits)
% see? MATLAB screws up when it comes to (really) big numbers (like
% about above 10^20-ish it seems.)
% Good to know.

% next time: Square root convergents! This is an interesting fact
% I've seen whenever mathematicians want to seem weird.
% Square roots can be expressed as infinite continued fractions.
% eg. sqrt(2) =~ 1 + 1/2 = 1.5
% sqrt(2) =~ 1 + 1/(2 + 1/2) = 1.4
% sqrt(2) =~ 1 + 1/(2 + 1/(2 + 1/2))
% ... and so on. It looks cramped as hell in notation.
