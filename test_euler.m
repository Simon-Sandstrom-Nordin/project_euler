% stuff
clc; clear all; close all;

% function handle
f = @(t,y) exp(t);

% parameters
t_0 = 0;
y_0 = 1;
max_iter = 50;
h = 0.1;  % step length

% vectors
t_v = [t_0];
y_v = [y_0];

% while loop
iter = 1; t_new = 0; y_new = 0;
while iter < max_iter
    [t_new, y_new] = euler_forwards(t_v(end), y_v(end), h, f);

    % push vectors
    t_v(end + 1) = t_new;
    y_v(end + 1) = y_new;
    iter = iter + 1;
end

plot(t_v, y_v, 'ro'); hold on; plot(t_v, exp(t_v), 'b')
