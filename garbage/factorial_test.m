clc; clear; close;

factorial(5)

function output = factorial(input)
if input == 1
    output = 1;
    return
end
output = input * factorial(input-1);
end
