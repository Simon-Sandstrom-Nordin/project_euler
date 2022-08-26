% Prime digit replacement
clc; clear; close all;

alter(12)

% objective: find first prime to have an eight digit prime value family.

% reasonably, that prime ain't singe digit. Since only [2,3,5,7] are prime.
% COULD IT BE double-digit? No, primes aint that dense below 100.

% img = imread("image_prime.jpg");
% image(img);

% We're looking for a row or a column with 8 primes. And in this game of
% bingo prime, there's no such thing :(. Most is 7... do the one digit
% numbers count? ... probably not, right? So note: if you're replacing
% the first digit, then you cannot enter a zero. Probs.

% could it be three digits? ... this feels false, but could be Idk.
% note: no need to worry about replacing "all" digits. Such a family would
% contain one "original" with all ones and 8 multples of that.

% wait, according to instructions, the first number to be part of a seven
% value prime family is 56''3, so the first to be part of an eight value
% prime family should be at least 5 digit. Good to know.


%
function eight_value_prime = alter(number)
% list of alterations
list_of_replacements = [0,1,2,3,4,5,6,7,8,9];
temp_replacement = {'X'};  % It needs to be a cell array... since
                                % split(string, splitter) returns a cell
                                % array.

% break integer down into array with everydigit. Or cell array.
cell_array = split(num2str(number), '');
cell_array = cell_array(2:end-1);   % remove leading and trailing ''
% disp(cell_array)

cell_array_prime_with_strings_attatched = {}

% create temporary list with o
altered_numbers = [];




end

% Note: string arrays are a thing! B = [1,2], string(B) = ["1", "2"]

% well, it doesn't work, but it was informative.
