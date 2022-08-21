% Pentagon numbers. Not that Pentagon.
clc; clear; close;
% ... doesn't work

p = @(n) n*(3*n - 1) / 2;   % anonymous function for generating 
                            % pentagonal numbers
limit = 1000;                            

list = zeros(limit, 1);   % prepare list so that size is constant
for k = 1:1:limit     % generate list of pentagonal numbers
list(k) = p(k);
end

min_distance = limit;
pair_part_1 = 0;
pair_part_2 = 0;
% look for numbers ...
for a = 1:1:limit
    for b = 1:1:limit
        if a == b
            continue
        end
        p_sum = ismember(list(a) + list(b), list);
        p_diff = ismember(abs(list(a) - list(b)), list);
        if (abs(list(a) - list(b)) < min_distance) && p_sum && p_diff
            pair_part_1 = list(a);
            pair_part_2 = list(b);
            min_distance = abs(list(a) - list(b));
        end
    end
end

disp(pair_part_1); disp(pair_part_2); disp(min_distance)
