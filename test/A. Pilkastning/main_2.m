% Skriv om diffekvationerna som system
% att lösas numeriskt
clc; clear; close all; format long;

% Constants
Kx = .001;
Ky = .01;
g = 9.82;
h = 185*.01; % height in meters
% mass, speed, and angle varies by questions
m = 26*.001; % mass in kg
v0 = 13;
phi = 5*(2*pi/360);    % radians, converted from degrees

% declare initial conditions
x_pos = 0;
y_pos = h;
x_vel = v0*cos(phi);
y_vel = v0*sin(phi);
velocity = v0;

% step length is special
step_length = .001;

% load u vector
u = zeros(7,1);
u(1) = x_pos;
u(2) = y_pos;
u(3) = x_vel;
u(4) = y_vel;
u(5) = velocity;
u(6) = step_length;
u(7) = m;
original_u = u;
figure(1)
tol = 1e-7; err = 1; maxiter = 7; iter = 1;
while err > tol && iter < maxiter
    u = original_u;
    step_length = step_length * .1;
    u(6) = step_length;
    x_vec = []; y_vec = []; x_vec(end+1) = u(1); y_vec(end+1) = u(2);
    while u(1) < 237*.01
        [x_pos, x_vel, y_pos, y_vel, velocity] = system_solver(u);
    
        % fill lists
        x_vec(end+1) = x_pos; y_vec(end+1) = y_pos;
    
        % reload
        u(1) = x_pos;
        u(2) = y_pos;
        u(3) = x_vel;
        u(4) = y_vel;
        u(5) = velocity;
    end
    % linear interpolation
    line = @(t) y_vec(end-1) + ...
        ((y_vec(end)-y_vec(end-1))/(x_vec(end)-x_vec(end-1))) * ...
        (t - x_vec(end-1));
    t = linspace(2.37 - .1, 2.37 + .1);
    plot(t, line(t), 'r'); hold on;
    plot(x_vec, y_vec, 'b'); % xlim([0,2.37]); ylim([0, 2])
    hold on
    original_u(6) = step_length;
    
    new_y = line(2.37)
    if iter ~= 1    % first iteration we only have one value for y
        err = abs(new_y - old_y)
    end
    old_y = new_y;
    iter = iter + 1
end

% so the a task is done.


