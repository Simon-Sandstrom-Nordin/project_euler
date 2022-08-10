function is_pandigital = e041_test(number)
number_string = num2str(number);
length_variable = length(number_string);

counter = 0;
if contains(number_string, '0')
    counter = counter + 1;
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
