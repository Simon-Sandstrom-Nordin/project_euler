%%%
%f = @(t) cos(pi*t) + 1j * sin(pi*t);
%t = linspace(-2*pi, 2*pi);
%plot(f(t)); axis equal;
%
clear; clc; close all;
counter = 0;
syms x
sum = 0;
y = exp(x);    % target function
a0 = 1 / pi * int(y, x, -pi, pi);
for n = 1:10
    an = (1/pi) * int(y*cos(n*x), x, pi, pi);
    bn = (1/pi) * int(y*sin(n*x), x, -pi, pi);
    sum = sum + (an*cos(n*x) + bn*sin(n*x));
    counter = counter + 1;
    if mod(counter, 100) == 0
        disp(counter)
    end
end

int(y, x, [0, pi])
interval = [-pi, pi];

ezplot(x,y, interval)
grid on; hold on;
ezplot(x, (sum + a0/2), interval)
