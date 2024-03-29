clc; clear; close;

number = 1234;
list_of_truncatable_primes = [];

primes_found = 0;
counter = 11;
while primes_found < 11 % didn't stop before since it was on <=
    bool = isTruncatablePrime(counter);
    if bool
        primes_found = primes_found + 1;
        list_of_truncatable_primes(end + 1) = counter;
    end
    if mod(counter, 1000) == 0
        disp(counter)
    end
    counter = counter + 1;
end
disp("Sum of all eleven both left- and right-truncatable primes is:")
sum(list_of_truncatable_primes)  

% doesn't end for some reason... oh well -\_(^-)_/-
% sum of that list is 748317
% insight: first of all, they're finite.
%          second, the last one is way the hell bigger than the rest, like
%                  a thousand times bigger than the second to last.

function isTruncatablePrimeBoolean = isTruncatablePrime(number)

list = [number];
for i = 1: length(num2str(number))
    if length(num2str(list(end))) == 1
        continue
    end
    list(end+1) = truncate_right(list(end));
end

% list
for i = 1: length(num2str(number))
    if i == 1
        list(end+1) = truncate_left(list(1));
        continue
    end
    if length(num2str(list(end))) == 1
        continue
    end
    list(end+1) = truncate_left(list(end));
end

% list

prime_counter = 0;
for i = 1: length(list)
    if isprime(list(i))
        prime_counter = prime_counter + 1;
    end
end
if prime_counter == length(list)
    isTruncatablePrimeBoolean = true;
else
    isTruncatablePrimeBoolean = false;
end
end

function truncated_number = truncate_right(number)
number_string = num2str(number);
number_cell_array = cell(1, numel(number_string) - 1);

for i = 1:numel(number_cell_array)
number_cell_array{i} = number_string(i);
end

truncated_string = '';
for i = 1:numel(number_cell_array)
truncated_string(end+1) =  number_cell_array{i};
end

truncated_number = str2num(truncated_string);
end

function truncated_number = truncate_left(number)
number_string = num2str(number);
number_cell_array = cell(1, numel(number_string) - 1);

for i = 1:numel(number_cell_array)
% + 2 since + 1 is due to MATLAB using [1] as (access index 1), and 1 more
% since number cell array was created with length (# elements)-1.
number_cell_array{i} = number_string(i + 1);
end

truncated_string = '';
for i = 1:numel(number_cell_array)
truncated_string(end+1) =  number_cell_array{i};
end

truncated_number = str2num(truncated_string);
end

% note to self... appending a string to an integer array
% appends the ascii value of that string, even if the
% string is the string of a number. ascii('1') = 49 != 1.

% more notes: cell array {}. From documentation:
% "A cell array is a data type with indexed data containers called cells,
% where each cell can contain any type of data. Cell arrays commonly
% contain either lists of text, combinations of text and numbers, or
% numeric arrays of different sizes. Refer to sets of cells by enclosing
% indices in smooth parentheses, (). Access the contents of cells by
% indexing with curly braces, {}."
% summary: arrays holding any type of data, not just numbers and shit.
