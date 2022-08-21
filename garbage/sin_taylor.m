clc; clear; close; format long;
f = @(x) x - x.^3 / 6 + x.^5 / 120;
x = linspace (-1.2*pi, 1.2*pi);

% plot this
figure(1);
plot(x, f(x), 'ro'); hold on; plot(x, sin(x));

% root finding by Newton's method. We have three roots in this interval.

x_1 = -3; x_2 = 1; x_3 = 3; % guesses.

% parameters
tolerance = 10^(-10);
max_iter = 100;

x_list = [x_2];
% newton's method for root 2
iter = 0; error = 100;
while iter < max_iter && error > tolerance
    x_new = x_2 - sin(x_2) / cos(x_2);
    x_list(end + 1) = x_new;
    error = abs(x_new - x_2);
    x_2 = x_new;
    iter = iter + 1;
end

disp(x_list')
