close; clc; clear;

% line
re = linspace(-pi, pi, 10);
im = linspace(-pi, pi, 10);
c = complex(re, im);

figure(1)
plot(c, 'bo')

% möbius transformation
m = @(z) 1./z;

figure(2)
plot(real(m(c)), imag(m(c)), 'ro')

% circle
angle = linspace(0, 2*pi);
circle_generator = @(phi) 2*exp(1j*phi);
circle = circle_generator(angle);

figure(3)
plot(circle); axis equal;

% möbius transformation
m2 = @(z) z;

figure(4)
plot(m(circle)); axis equal;