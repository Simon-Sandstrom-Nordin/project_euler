% öÖö
% Sub-string divisibility
clc; clear all; close all; format long;
list = [];

limit = 9999999999;
for k = 1234567890:limit
    if is_pandigital(k)
        list(end + 1) = k;
    end
end


function isPandigital = is_pandigital(number)
string_number = string(number);
string_array = split(string_number, "");
string_array = string_array(2:end-1);

if length(string_array) ~= 10
    isPandigital = false;
    return
end

counter = 0;
if ismember("0", string_array)
    counter = counter + 1;
end
if ismember("1", string_array)
    counter = counter + 1;
end
if ismember("2", string_array)
    counter = counter + 1;
end
if ismember("3", string_array)
    counter = counter + 1;
end
if ismember("4", string_array)
    counter = counter + 1;
end
if ismember("5", string_array)
    counter = counter + 1;
end
if ismember("6", string_array)
    counter = counter + 1;
end
if ismember("7", string_array)
    counter = counter + 1;
end
if ismember("8", string_array)
    counter = counter + 1;
end
if ismember("9", string_array)
    counter = counter + 1;
end

if counter == 10
    isPandigital = true;
    return
end
isPandigital = false;
end
