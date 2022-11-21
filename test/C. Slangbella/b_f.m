function x_end = b_f(d)
%B_F Summary of this function goes here
%   Detailed explanation goes here

% constants
z_pos = d;     % d i uppgiften
z_vel = 0;  % no initial velocity
L0 = 10;    % cm
B = 12;     % cm
k = 950;    % N/m

% step length is special
step_length = 0.00001;

% Liknande funktionsfil för i B? Det är en väldigt lik uppgift...
% Mycket kod går nog att modifiera för att passa här.

% z_solver(u)
% load u vector
u = zeros(3,1);
u(1) = z_pos;
u(2) = z_vel;
u(3) = step_length;

% d seems to be chosen by us...
disp("finding exit velocity")
original_u = u;
%figure(1)
tol = 1e-7; err = 1; maxiter = 12; iter = 1;
while err > tol && iter < maxiter
    u = original_u;
    step_length = step_length * .1;
    u(3) = step_length;
    z_pos_vec = []; z_pos_vec(end+1) = u(1); z_vel_vec = []; z_vel_vec(end+1) = u(2);
    while u(1) > 0
        [z_pos, z_vel] = z_solver(u);
    
        % fill lists
        z_pos_vec(end+1) = z_pos;
        z_vel_vec(end+1) = z_vel;

        % reload
        u(1) = z_pos;
        u(2) = z_vel;
    end
    % linear interpolation
    %line = @(t) z_pos_vec(end-1) + ...
    %    ((z_vel_vec(end)-z_vel_vec(end-1))/step_length) * ...
    %    (t - z_pos_vec(end-1));
    %t = linspace(-.001, .001);
    %plot(t, line(t), 'r'); hold on;
    %plot(z_pos_vec, z_vel_vec, 'b');
    %hold on
    %original_u(3) = step_length;
    
    %new_z = line(0)
    new_z = z_vel_vec(end);
    if iter ~= 1    % first iteration we only have one value for z
        err = abs(new_z - old_z);
    end
    old_z = new_z;
    iter = iter + 1
end
v0 = new_z; % found exit velocity

% a)

m = 50*.001;
phi = 45*(2*pi/360);    % radians, converted from degrees
% declare initial conditions
x_pos = 0;
y_pos = 1.65;
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
tol = 1e-7; err = 1; maxiter = 7; iter = 1;
while err > tol && iter < maxiter
    u = original_u;
    step_length = step_length * .1;
    u(6) = step_length;
    x_vec = []; y_vec = []; x_vec(end+1) = u(1); y_vec(end+1) = u(2);
    while u(2) > 0
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
    % x as function of y
    line = @(t) x_vec(end-1) + ...
        ((x_vec(end)-x_vec(end-1))/(y_vec(end)-y_vec(end-1))) * ...
        (t - y_vec(end-1));
    t = linspace(y_vec(end) - .1, y_vec(end) + .1);
    plot(line(t), t, 'r'); hold on;
    plot(x_vec, y_vec, 'b'); % xlim([0,2.37]); ylim([0, 2])
    hold on
    original_u(6) = step_length;
    
    new_x = line(0);
    if iter ~= 1    % first iteration we only have one value for y
        err = abs(new_x - old_x);
    end
    old_x = new_x;
    iter = iter + 1
end
x_end = new_x
end

