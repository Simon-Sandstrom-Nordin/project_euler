% complex plotting :)
clc; clear; close all;

f = @(z) abs(z - 1 + 1j);
x = linspace(0, 2*pi);
y = linspace(0, 2*pi);

z = complex(x, y);
plot(f(z))

%%
clc; clear; close all;

c = @(z) exp(z) + 1j - 1;

x = linspace(log(2),log(2));
y = linspace(0,2*pi);
z = complex(x, y);

plot(c(z)); axis equal; axis([-4,4,-4,4])


%%
clc; close; clear;
co = @(z) z^2 + 5*z + 6;

co(-2)
co(-3)

%%
clc; close; clear;
g = @(t) cos(t).*abs(cos(t)) + 1j*sin(t).*abs(sin(t));
t = linspace(0, 2*pi);
plot(g(t)); axis equal;