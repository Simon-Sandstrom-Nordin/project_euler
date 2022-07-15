clear all; clc, close all;

fileID = fopen('e022_names.txt');
file = fgetl(fileID);
file = convertCharsToStrings(file);
file_array = split(file, ",");
file_array = strip(file_array, "both", '"');
file_array = file_array.sort;

sum = 0;

for i = 1:length(file_array)    % name
   name = file_array(i);
   name = convertStringsToChars(name);
   score = 0;
   for k = 1:length(name)       % letters in name
       letter = name(k);
       score = score + e022_letter2num(letter);
   end
   sum = sum + score * i;
end

disp(sum)
