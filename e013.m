clear all; clc;

number = 0;
record = 0;
for i = 1: 1000000
    if mod(i, 100)
        disp(i)
    end
    score = e013_counter_function(i);
    if score > record
        number = i;
        record = score;
    end
end

disp("Number is " + number)
disp("Record is " + record)
