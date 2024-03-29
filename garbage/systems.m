% numerically solving linear system of ordinary differential equations
clc; clear all; close all;

% [up vp] = @(u, v) [0 1; -1 0] * [u v]'
% don't worry so much about this anonomous function over here. Nothing 2see

u_0 = 1; v_0 = 1; t_0 = 0;   % initial conditions
h = .01;  % step length

t_vector = [t_0];
u_vector = [u_0];
v_vector = [v_0];

max_iterations = 1000; iter = 1; % puts bounds on my while loop
while iter < max_iterations
    [u_n_next, v_n_next] = my_euler(u_vector(end), v_vector(end), h);
    u_vector(end + 1) = u_n_next;
    v_vector(end + 1) = v_n_next;
    t_vector(end + 1) = t_vector(end) + h;
    iter = iter + 1;
end
disp([u_vector' v_vector']);
plot(t_vector, u_vector, 'b')   % numeric approximation
hold on
% plot(t_vector, v_vector, 'r') % This would have been the derivative
hold on
plot(t_vector, cos(t_vector) + sin(t_vector), 'k')  % analytic solution
legend('approximation', ' analytic solution');

function [u_n_next, v_n_next] = my_euler(u_n, v_n, h)
v_n_prime = @(u_n) -u_n;

u_n_next = u_n + h .* v_n;           % u_n prime = v_n 
v_n_next = v_n + h .* v_n_prime(u_n);
end
