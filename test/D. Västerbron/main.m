%
clc; clear; close all;

% parameters
a = 26; % segelfri höjd

% constants
y0 = 0; yL = 0; t_L_half = a; L = 204; K = 2*10^(-4);

% Second order ODE to system
y_system = @(x, u) [u(2);- K .* u(1) .* (1 + u(2).^2) .^ (3/2)];

% båglängdsberäkning genom linjär approximation och pythagoras sats.
t = linspace(L/2, L);
ode45(y_system, t, [a, 0]); axis equal;

%... det fungerar typ med ett minus i andra elementet. Varifrån det
% kommer är dock ett mysterium. Fel i lydelsen?
