clc; clear all; close all;
%%
f = @(x) x.^3 - 6.*x.^2 + 11.*x - 6;

x = [1, 2, 3, 6, -1, -2, -3, -6];

f(x)

syms x
y = (x - 1)*(x - 2)*(x - 3)
expand(y)
expand((x - 1)*(x - 2)*(x - 3))
%%
clc; clear all; close all;
g = @(x) 8.*x.^5 + 2.*x + 6;
x = [1, 2, 3, 6, -1, -2, -3, -6, 1/2, 3/2, -1/2, -3/2, 1/8, 1/4, 3/8, 3/4, -1/8, -1/4, -3/8, -3/4];
g(x)

%%
clc; clear all; close all;
syms x
y = (x + 1)*(x + 1j)*(x - 1j);
expand(y)