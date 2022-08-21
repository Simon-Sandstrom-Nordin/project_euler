% öÖö
% Sub-string divisibility

% This... I think 40 days was the estimate for the time this
% would take...? ehm... I got to like 20-ish percent
% then my computer shut off. I'll move on <3.

% note to self: probably works but is depressingly slow... :(
% ... I'll leave this going for a few moments / long moments

clc; clear all; close all; format;
list = [];

limit = 9999999999;
for k = 1234567890:limit
    if is_pandigital(k)
        list(end + 1) = k;
    end
    if mod(k, 1000000) == 0
        disp(((k - 1234567890)/(limit + 1 - 1234567890)) * 100 + " %")
    end
end
sum = sum(list);
disp("Sum is equal to: " + sum)

function isSpecialPandigital = is_pandigital(number)
string_number = string(number);
string_array = split(string_number, "");
string_array = string_array(2:end-1);

if length(string_array) ~= 10
    isSpecialPandigital = false;
    return
end

numbers = str2double(string_array);
isSpecialPandigital = false;
if ismember(0, numbers) == false
    return;
end
if ismember(1, numbers) == false
    return;
end
if ismember(2, numbers) == false
    return;
end
if ismember(3, numbers) == false
    return;
end
if ismember(4, numbers) == false
    return;
end
if ismember(5, numbers) == false
    return;
end
if ismember(6, numbers) == false
    return;
end
if ismember(7, numbers) == false
    return;
end
if ismember(8, numbers) == false
    return;
end
if ismember(9, numbers) == false
    return;
end

% Check sub-string divisibility
if mod(numbers(2)*100 + numbers(3)*10 + numbers(4), 2) ~= 0
    return
end
if mod(numbers(3)*100 + numbers(4)*10 + numbers(5), 3) ~= 0
    return
end
if mod(numbers(4)*100 + numbers(5)*10 + numbers(6), 5) ~= 0
    return
end
if mod(numbers(5)*100 + numbers(6)*10 + numbers(7), 7) ~= 0
    return
end
if mod(numbers(6)*100 + numbers(7)*10 + numbers(8), 11) ~= 0
    return
end
if mod(numbers(7)*100 + numbers(8)*10 + numbers(9), 13) ~= 0
    return
end
if mod(numbers(8)*100 + numbers(9)*10 + numbers(10), 17) ~= 0
    return
end

isSpecialPandigital = true;
end
