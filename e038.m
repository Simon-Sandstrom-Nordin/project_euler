clc; clear; close;

list = [];
limit = 1000000000;
for k = 1:limit
    multiplicand = k;
    multiplier = 1;
    product_string = '';
    temp_product_string = '';
    product = 1;
    while length(temp_product_string) < 10
        product = multiplicand * multiplier;
        temp_product_string = strcat(product_string, num2str(product));
        if length(temp_product_string) < 10
            product_string = temp_product_string;
        end
        multiplier = multiplier + 1;
    end
    if e032_help(product_string)
       list(end + 1) = str2num(product_string);
    end
    if mod(k, 1000000) == 0
        disp("Progress: " + k / limit)
    end
end
disp(max(list));

% Didn't work... :(. Took like 2 days to run too...
