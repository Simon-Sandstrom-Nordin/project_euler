% Champernowne's constant
clc; clear; close;

string_ = "";   % "0." removed
counter = 1;
while length(string_{1}) < 1000000
    string_ = string_ + num2str(counter);
    counter = counter + 1;
    if mod(counter, 1000) == 0
        disp("Progress: " + length(string_{1})/ 1000000)
    end
end
disp("Checkpoint 1")

expression = [];

expression(end + 1) = (str2num(string_{1}(1)));
expression(end + 1) = (str2num(string_{1}(10)));
expression(end + 1) = (str2num(string_{1}(100)));
expression(end + 1) = (str2num(string_{1}(1000)));
expression(end + 1) = (str2num(string_{1}(10000)));
expression(end + 1) = (str2num(string_{1}(100000)));
expression(end + 1) = (str2num(string_{1}(1000000)));


expression
prod(expression)

disp("Checkpoint 2")

