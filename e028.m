clc; clear; close all;

size = 1001^2;

sum = 0;
counter = 0;
decrement = 1001 - 1;
while size > 1
    sum = sum + size;
    size = size - decrement;
    counter = counter + 1;
    if mod(counter, 4) == 0
        decrement = decrement - 2;  % side of inner square decreases by 2
    end
end
sum = sum + 1;   % add middle number which is one.

disp(sum)
disp(size)

% Worked! answer is 669171001
