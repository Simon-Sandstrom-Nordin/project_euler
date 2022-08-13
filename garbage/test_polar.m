clc; close; clear;
z1 = complex(-4, 0);
z2 = complex(2, - 2*sqrt(3));
z3 = complex(2, + 2*sqrt(3));
plot(z1, 'ro'); hold on; plot(z2, 'go'); plot(z3, 'bo');
disp(abs(z1)); disp(abs(z2)); disp(abs(z3));
