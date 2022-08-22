% Intervallhalvering.
clc; clear; close;

% 1
f = @(x) (x - 2.5) .* exp(-0.5 * (x - 2).^2);

x = linspace(1, 5);
plot(x, f(x)); axis equal;

a = 2; b = 3;   % initial guesses, on on each side of the x-axis

if f(a)*f(b) < 0
    disp("f(a)*f(b) < 0")
end

m = (a + b) / 2;    % point in the middle

if f(m) == 0
    disp("We've found our x-intersect: " + m)
end

if f(a) * f(m) < 0
    disp("middle point is to the right of the intersect.")  % we want this.
    % it means that we've caught the line between our two points.
    b = m;  % new interval is (here) [2, 2.5].
else
    disp("middle point is to the left of the intersect.")   % could be used
    % it means the other interval contains the line.
    a = m;
end

if f(a)*f(b) < 0
    disp("f(a)*f(b) < 0")
end

if f(a)*f(b) > 0
    disp("f(a)*f(b) > 0")
end

% remember, this is useful! Altough there are methods that converge faster.
% ... but this is intuitive and easy to implement. Also doesn't require
% any knowledge of the derivative of the function, or such.
