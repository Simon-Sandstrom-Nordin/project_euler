function isPandigital = e032_help(number_string)

% first things first: check if length is 9
if length(number_string) ~= 9
    isPandigital = false;
    return
end

% counter for counting which numbers are included
counter = 0;
if contains(number_string, '1')
    counter = counter + 1;
end
if contains(number_string, '2')
    counter = counter + 1;
end
if contains(number_string, '3')
    counter = counter + 1;
end
if contains(number_string, '4')
    counter = counter + 1;
end
if contains(number_string, '5')
    counter = counter + 1;
end
if contains(number_string, '6')
    counter = counter + 1;
end
if contains(number_string, '7')
    counter = counter + 1;
end
if contains(number_string, '8')
    counter = counter + 1;
end
if contains(number_string, '9')
    counter = counter + 1;
end
if counter == 9
    isPandigital = true;
else
    isPandigital = false;
end
end
