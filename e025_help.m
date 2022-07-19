number = 1
for k = 1:100
    number = number * 10;
end

disp(number)

% MATLAB can't deal with 1000-digit numbers either...
% Double

realmax("double")
% max here is 308 digit number... close but not close enough
