clc; clear all; close all;

% Panigital products
product_array = [];

max_multiplicand = 10000;
max_multiplier = max_multiplicand;
for multiplicand = 1:max_multiplicand
    for multiplier = 1:max_multiplier
        product = multiplicand * multiplier;
        number_string = strcat(num2str(product), num2str(multiplicand), num2str(multiplier));
        if e032_help(number_string)
            if ismember(product, product_array) == false
                product_array(end+1) = product;
            end
        end
    end
    if mod(multiplicand, 100) == 0
        disp("Progress report: " + multiplicand + " / "+ max_multiplicand)
    end
end

disp("Sum of product array is " + sum(product_array))

% answer: 45228
