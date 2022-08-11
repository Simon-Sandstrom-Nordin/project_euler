clc; clear; close;

syms x
syms y
syms z

disp("stuff 1")
expand((x-1)*(y-1)-2)
disp("stuff 2")
expand((z-1)*(y-1)-3)
disp("stuff 3")
expand((x-1)*(z-1) - 6)
