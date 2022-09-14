% Lynchrel numbers
clc; clear; close;

% checking that it works
% palindrome(121) returns logical [1]
% palindrome(123) returns logical [2]
% both of these results are what what I wanted.

%start_number = input("Enter starting number: ");
% input was for testing

% abandon this for now, let's do an actual thing in the next session!
start_numer = 1; limit = 10000;
list = [start_number];
searching = true;
while searching
    next_number = add_reverse(list(end));
    list(end + 1) = next_number;
    if palindrome(list(end))
        searching = false;
    end
end
disp(list); disp("Number of iterations: " + (length(list) - 1));

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

% note: might not work in matlab as the integers become
% to large.