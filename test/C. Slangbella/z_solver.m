function [z_pos, z_vel] = z_solver(u)
% system_solver: Solves equations of motions and a velocity function
% see "variables" to see what vector u contains. t is current time.

% constants
m = 50*.001;
L0 = 10*.01;
B = 12*.01;
k = 950;

% variables
z_pos = u(1);
z_vel = u(2);
step_length = u(3);

% find L
L = 2*sqrt(z_pos^2 + (B/2)^2);

% calc. accelerations
z_acc = (k/m)*(L-L0);

% assign new values
z_pos = z_pos - step_length*z_vel;
z_vel = z_vel + step_length*z_acc;
end
