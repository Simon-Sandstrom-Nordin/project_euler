% Code triangle numbers
clc; clear; close;

triangle_numbers = [];
for k = 1: 10000000
    triangle_numbers(end + 1) = generator(k);
end

% disp(triangle_numbers)

%m = coding("SKY");
%disp(length(triangle_numbers))

%for a = 1: length(triangle_numbers)
%    if m == triangle_numbers(a)
%        disp(triangle_numbers(a) + "hi")
%    end
%end

fileID = fopen("p042_words.txt", 'r');
A = fscanf(fileID, '%s %s', [1 inf]);
B = split(A, ",");

triangle_counter = 0;
for k = 1: size(B)
    code_number = coding(B{k,1});
    for a = 1: length(triangle_numbers)
        if code_number == triangle_numbers(a)
            triangle_counter = triangle_counter + 1;
        end
    end
end
disp(triangle_counter)

function triangle_number = generator(index)
    triangle_number = index * (index + 1) / 2;
end

function word_value = coding(word)
   list = split(word, "");
   list = list(2:end-1);    % remove empty strings leading and trailing
   sum = 0;
   for k = 1: length(list)
        number = letter_checker(list(k));
        sum = sum + number;
   end
   word_value = sum;
end

function number = letter_checker(letter)
number = 0;
if letter == "A"
    number = 1;
elseif letter == "B"
    number = 2;
elseif letter == "C"
    number = 3;
elseif letter == "D"
    number = 4;
elseif letter == "E"
    number = 5;
elseif letter == "F"
    number = 6;
elseif letter == "G"
    number = 7;
elseif letter == "H"
    number = 8;
elseif letter == "I"
    number = 9;
elseif letter == "J"
    number = 10;
elseif letter == "K"
    number = 11;
elseif letter == "L"
    number = 12;
elseif letter == "M"
    number = 13;
elseif letter == "N"
    number = 14;
elseif letter == "O"
    number = 15;
elseif letter == "P"
    number = 16;
elseif letter == "Q"
    number = 17;
elseif letter == "R"
    number = 18;
elseif letter == "S"
    number = 19;
elseif letter == "T"
    number = 20;
elseif letter == "U"
    number = 21;
elseif letter == "V"
    number = 22;
elseif letter == "W"
    number = 23;
elseif letter == "X"
    number = 24;
elseif letter == "Y"
    number = 25;
elseif letter == "Z"
    number = 26;
end
end
