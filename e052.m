% Permutated mutiples
clc; clear; close;

searching = true;
counter = 1;
while searching

   % all of these are numbers!
   x = counter;
   x2 = 2*counter;
   x3 = 3*counter;
   x4 = 4*counter;
   x5 = 5*counter;
   x6 = 6*counter;

   % parse to strings
   string_x = num2str(x);
   string_x2 = num2str(x2);
   string_x3 = num2str(x3);
   string_x4 = num2str(x4);
   string_x5 = num2str(x5);
   string_x6 = num2str(x6);

   % split into cells
   cell_x = split(string_x, '');
   cell_x2 = split(string_x2, '');
   cell_x3 = split(string_x3, '');
   cell_x4 = split(string_x4, '');
   cell_x5 = split(string_x5, '');
   cell_x6 = split(string_x6, '');

    % cells to character arrays
    array_x = cell2mat(cell_x);
    array_x2 = cell2mat(cell_x2);
    array_x3 = cell2mat(cell_x3);
    array_x4 = cell2mat(cell_x4);
    array_x5 = cell2mat(cell_x5);
    array_x6 = cell2mat(cell_x6);

    % used for comparisons
    comp = intersect(array_x, array_x);

    % intesect them all!
    i1 = intersect(array_x, array_x2);
    i2 = intersect(array_x2, array_x3);
    i3 = intersect(array_x3, array_x4);
    i4 = intersect(array_x4, array_x5);
    i5 = intersect(array_x5, array_x6)


    try
        if (i1 == i2) & (i2 == i3) &  (i3 == i4) & (i4 == i5) & (i5 == comp)
            disp(x)
            searching = false;
        end
        counter = counter + 1;
    catch
        counter = counter + 1;
    end
end
