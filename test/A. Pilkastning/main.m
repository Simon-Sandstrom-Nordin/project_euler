% Skriv om diffekvationerna som system
% att lösas numeriskt
clc; clear; close all; format long;

% Constants
Kx = .001;
Ky = .01;
g = 9.82;
h = 185; % height
% mass, speed, and angle varies by questions
m = 26;
v0 = 13;
phi = 5;    % degrees, not radians

% System of Ode:s
up_x = @(t, u) [u(2); -g-Ky/m * u(2)];
up_y = @(t, u) [u(2); -Kx / m * u(2)];
% Velocity function
V = @(xp, yp) sqrt(xp^2 + yp^2);

% a)
t = linspace(0, 2);

% initial conditions
u0_x = [0; cos(v0)]; u0_y = [h; sin(v0)];

[t_v, U_x] = ode45(up_x, t, u);

%% notes (8/11):
% bättre att skriva en separat funktionsfil
% för lösningen av systemen... de är
% coupled, eller de beror på varandra.
