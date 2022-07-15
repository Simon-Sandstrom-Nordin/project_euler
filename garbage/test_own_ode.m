clc, clear all, close all

[t, y] = ode45(@(t, y) cos(y), [0,20], (3/2)*pi + .1);
plot(t, y, 'b');
hold on
[t, y] = ode45(@(t, y) cos(y), [0,20], (3/2)*pi - .1);
plot(t, y, 'r')
