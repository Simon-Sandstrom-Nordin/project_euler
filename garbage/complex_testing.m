clc; clear all; close all;

%%
syms x
syms a
syms b
syms c


y = (x - a/3)^3 + a*(x - a/3)^2 + b*(x - a/3) + c;
expand(y)

%%
clc; clear all; close all;
p = @(x, y) 2.*(x.^2).*y.^2
q = @(x) x.^2.*2

p(2,1)
q(5)