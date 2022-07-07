clear all; clc;

number = 0;
record = 0;
for i = 1: 1000000
    if mod(i, 100)
        disp(i)
    end
    score = e013_counter_function_test(i);
    if score > record
        number = i;
        record = score;
    end
end

disp("Number is " + number)
disp("Record is " + record)

function [counter] = e013_counter_function_test(number)
counter = 1;
searching = true;
while searching
    counter = counter + 1;
    number = e013_collatz_function_test(number);
    if number == 1
        searching = false;
    end
end
end

function [collatz] = e013_collatz_function_test(number)
if mod(number, 2) == 0
    collatz = number / 2;
    return
end
collatz = 3 * number + 1;
end
