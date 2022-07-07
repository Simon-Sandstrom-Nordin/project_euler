f = @(x) abs(x + 1) + 2.*x - x.^2;

x = linspace(-6, 2)

plot(x, f(x))

disp("max: " + max(f(x)))
disp("min: "+ min(f(x)))