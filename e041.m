% pandigital prime
clc, clear; close; format;

% initial = 1023456789;
initial = 10^7;      % Took this from internet, but like
limit = 10^9;          % 8167543 is bigger...?

for k = initial:limit
    if isprime(k) && isPandigital(k)
        disp(k)
    end
end

%for k = initial:limit
%    if isprime(k)
%        if isPandigital(k)
%            disp(k)
%        end
%    end
%end

function is_pandigital = isPandigital(number)
number_string = num2str(number);
length_variable = length(number_string);

counter = 0;
if contains(number_string, '0')
    %counter = counter + 1;
    is_pandigital = false;
    return
end
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
if length_variable == counter
    is_pandigital = true;
else
    is_pandigital = false;
end
end
