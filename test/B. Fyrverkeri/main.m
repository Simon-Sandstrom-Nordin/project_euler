% Samma sak här som i A, nog bättre att redan
% från början skriva en separat funktionsfil
% för att lösa systemen...
clc; clear; close all; format long;

% i princip kommer det här bli Euler framåt, för system, manuellt...
% load u vector
u = zeros(6,1);
u(1) = x_pos;
u(2) = y_pos;
u(3) = x_vel;
u(4) = y_vel;
u(5) = velocity;
u(6) = step_length;
