% same as with e_55.m, but now instead of a list I got a counter(s)
clc; clear all; close all;

lynchrel_counter = 0; iteration_counter = 1;
searching_for_lynchrels = true;
while searching_for_lynchrels
    iterations_till_palindrome_counter = 0;

    % also stolen but modified (no list, we're doing counters now.)
    old_number = iteration_counter;
    searching_for_palindrome = true;
    while searching_for_palindrome
        next_number = add_reverse(old_number);
        if palindrome(next_number)
            lynchrel_counter = lynchrel_counter + 1;
            searching_for_palindrome = false;
            % don't break here, we have counters to increment down below.
        end
        iterations_till_palindrome_counter = ...
            iterations_till_palindrome_counter + 1;
        old_number = next_number;
        if old_number > 10e+15  % limit around 10^16 in Matlab? ... dunno.
                                % something is messing with me here though.
            disp(old_number)
        end

        % break conditions!
        if iterations_till_palindrome_counter == 50 % <=comforting but unn.
            searching_for_palindrome = false;
        end
    end
    iteration_counter = iteration_counter + 1;
    if iteration_counter == 10000   % should be 10000, increments above.
        searching_for_lynchrels = false;
    end
end
disp(lynchrel_counter)

% Stolen from e_55.m, but it's not plagerism as this is my own intellectual
% property. If anything, I'm referencing my previous work.
function palindrome_boolean = palindrome(number)
    number_string = num2str(number);
    reverse_string = reverse(number_string);
    logical_array = number_string == reverse_string;
    if logical_array
        palindrome_boolean = true;
    else
        palindrome_boolean = false;
    end
end

function sum = add_reverse(number)
    number_string = num2str(number);
    reverse_string = reverse(number_string);
    number = str2num(number_string);
    reverse_number = str2num(reverse_string);
    sum = number + reverse_number;
end

% lesson learnt: 10^(15+1) = 10e+15
% the "e+" thing seems to add 15 zeros. Exponentiation of 10 by 15 adds 14.
% 10^(15) = 1e+15 = 10e+14
