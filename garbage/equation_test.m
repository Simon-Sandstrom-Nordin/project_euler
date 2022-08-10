% test for fun and games

y1 = @(x) 4*x - 5;
y2 = @(x) x/2 + 7/2;
y3 = @(x) (5/3)*x + 2/3;


x = linspace(-10, 10);
plot(x, y1(x)); hold on; plot(x, y2(x));
hold on; plot(x,  y2(x)); hold on; plot(x, y3(x));
