function [x_pos, x_vel, y_pos, y_vel, velocity] = system_solver(u)
% system_solver: Solves equations of motions and a velocity function
% see "variables" to see what vector u contains. t is current time.

% constants
Kx = .001;
Ky = .01;
g = 9.82; 

% variables
x_pos = u(1);
y_pos = u(2);
x_vel = u(3);
y_vel = u(4);
velocity = u(5);
step_length = u(6);
m = u(7);   % mass, remember to insert in kg

% calc. accelerations
y_acc = -g - Ky*y_vel*velocity / m;
x_acc = -Kx*x_vel*velocity / m;

% assign new values
x_pos = x_pos + step_length*x_vel;
y_pos = y_pos + step_length*y_vel;
x_vel = x_vel + step_length*x_acc;
y_vel = y_vel + step_length*y_acc;
velocity = sqrt(x_vel^2 + y_vel^2);
end
