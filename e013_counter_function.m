function [counter] = e013_counter_function(number)
counter = 1;
searching = true;
while searching
    counter = counter + 1;
    number = e013_collatz_function(number);
    if number == 1
        searching = false;
    end
end
end
