clc; clear; close;

f = @(z) log(z);

x = linspace(-2*pi, 2*pi);
y = linspace(-2*pi, 2*pi);
z = complex(x, y);

plot(f(z))
