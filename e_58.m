% Spiral primes
clc; clear all; close all;

% first: try to construct a 7x7 matrix like the first ex
size = 7;
A = zeros(size,size);
A(ceil(size/2),ceil(size/2)) = 1;
disp(A) % This is a good start...
value = 1;
while value <= size^2
    %disp(value)
    value = value + 1;
end

% Inspiration written i C of code creating the spiral pattern
% https://stackoverflow.com/questions/53325542/how-to-write-a-code-that-prints-an-specific-numerical-spiral-pattern-in-c-using
% That code fills it top left to center in ascending order, HOWEVER,
% I should be able to modify it.
