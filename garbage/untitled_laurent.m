clc; clear; close;

z = complex(1,1);
plot(z*z, 'ro'); axis equal; xlim([-3,3]); ylim([-3,3]);

hold on;
w = complex(-.5, .5); plot(w*w, 'ob')
plot(z*z+w*w, 'og'); plot((z-w)^2, 'yo'); plot(-2*z*w, 'om')
plot(z*z-2*z*w-w*w, 'ro')
% lesson learned... ?

syms x
syms y
expand((x-y)^2)
