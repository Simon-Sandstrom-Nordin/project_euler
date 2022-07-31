clc; clear; close all;

list = [];

sum = 0;
for k=3:1000000
    sum = 0;
    k_string = num2str(k);
    for m = 1: length(k_string)
        sum = sum + factorial(str2double(k_string(m)));
    end
    if sum == k
        list(end + 1) = k;
    end
    if mod(k, 10000) == 0
        disp("counter is at:" +  k)
    end
end

disp(list)
