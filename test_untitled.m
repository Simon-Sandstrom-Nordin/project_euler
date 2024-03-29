% för att testa

% Permutated mutiples
clc; clear; close;

searching = true;
counter = 1;
while searching

    % all of these are numbers!
    x = counter;
    x2 = 2*counter;

    % parse to strings
    string_x = num2str(x);
    string_x2 = num2str(x2);

     % split into cells
    cell_x = split(string_x, '');
    cell_x2 = split(string_x2, '');

    % cells to character arrays
    array_x = cell2mat(cell_x);
    array_x2 = cell2mat(cell_x2);

    % used for comparisons
    comp = intersect(array_x, array_x);

    % intesect them all!
    i1 = union(array_x, array_x2);
    i1 = intersect(1i, 1i);

    try
        if (i1 == comp)
            disp(x)
            searching = false;
        end
        counter = counter + 1;
    catch
        counter = counter + 1;
    end
end

% --- doesn't work but lesson learnt: in MATLAB, (a == b) && (b == c)
% is a == b == c, which is a transitive relation.
