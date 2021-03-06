clc; clear all;

f = @(x) x.^3 + 3.*x.^2 - x;
g = @(x) -x.^3 - 5.*x.^2 + 5*x - 9;

fp = @(x) 3.*x.^2 + 6.*x - 1;
gp = @(x) -3.*x.^2 - 10.*x + 5;

x = linspace(-10, 10);
plot(x, fp(x))
hold on;
plot(x, gp(x));

yin = intersect(fp(x), gp(x));
