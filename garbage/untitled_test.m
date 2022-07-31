% Truncatable primes
X = [1,2,3,4,5,6,7,8,9];
var(X);
mean(X);
std(X);
% Ignore these, they're part of Nomi Mino's MATLAB adventure
% ... also useful while procrastinating real work.

f = @(x) 4.^x; g = @(x) 8;
x = linspace(0,2);
plot(x, f(x)); hold on; plot(x, g(x));

