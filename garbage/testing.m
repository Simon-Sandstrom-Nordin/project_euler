clc; close; clear; format long;

% testing, attention please:
p = @(x) x.^3 + x.^2 - 2*x - 2;
x = linspace(-2, 2);
%plot(x, p(x))

% newton's method! remember? We're looking for two roots...
x1_guess = -1.5;
x2_guess = -.9;

% scratch that, we're looking for three roots...
x3_guess = 1.5;

% tolerance
tol = 10^-4;
err = 1;

% derivative of polynomial
p_prime = @(x) 3.*x.^2 + 2*x - 2;

% while loops
x_old = x1_guess;
while err > tol
    % Newton iteration scheme
    x_new = x_old - p(x_old) / p_prime(x_old);
    err = abs(x_new - x_old);
    x_old = x_new;
end
disp(x_new)

err = 1;
x_old = x2_guess;
while err > tol
    % Newton iteration scheme
    x_new = x_old - p(x_old) / p_prime(x_old);
    err = abs(x_new - x_old);
    x_old = x_new;
end
disp(x_new)

err = 1;
x_old = x3_guess;
while err > tol
    % Newton iteration scheme
    x_new = x_old - p(x_old) / p_prime(x_old);
    err = abs(x_new - x_old);
    x_old = x_new;
end
disp(x_new)
