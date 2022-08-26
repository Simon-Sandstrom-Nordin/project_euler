% Prime permutations.
clc; clear all; close;

increment = 3330;

for c =  1000:1:10000-1 - 2*increment
    term_1 = c;
    term_2 = c + increment;
    term_3 = c + 2*increment;

    % check primality
    if isprime(term_1) && isprime(term_2) && isprime(term_3)
        cell_1 = split(num2str(term_1), "");
        cell_1 = cell_1(2:end-1);   % remove leading and trailing ""
        cell_2 = split(num2str(term_2), "");
        cell_2 = cell_2(2:end-1);   % remove leading and trailing ""
        cell_3 = split(num2str(term_3), "");
        cell_3 = cell_3(2:end-1);    % remove leading and trailing ""

        % my idea: sort the cell arrays then check equality.
        
        % first sort
        cell_1_sorted = sort(cell_1);
        cell_2_sorted = sort(cell_2);
        cell_3_sorted = sort(cell_3);

        % second things second check equality:
        % ... before that though, cell arrays cannot be checked for equaliy
        % in MATLAB, so... I suppose convert to strings first

        string_1 = "";
        string_2 = "";
        string_3 = "";

        for k = 1:1:4
            string_1 = string_1 + cell_1_sorted(k);
            string_2 = string_2 + cell_2_sorted(k);
            string_3 = string_3 + cell_3_sorted(k);
        end

        if string_1 == string_2 && string_2 == string_3
            disp(term_1 + ":" + term_2 + ":" + term_3)
        end

    end
end

% output:
% 1487:4817:8147
% 2969:6299:9629

% arithmetic sequence! arithmetic progression of (finite?) terms...?
