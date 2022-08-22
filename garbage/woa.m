clc; clear; close;

%A = [-1 0 1; 1 1 1]
%b = [1 2 4]'
%A' * A

yp = @(y) -.5*y;
h = 4;

t = 0;
t_list = [];
t_list(end + 1) = t;
y = 1;
y_list = [];
y_list(end+1) = y;

while t < 48
    y = euler(y_list(end), h);
    t = t + h;
    t_list(end + 1) = t;
    y_list(end + 1) = y;
end
    
plot(t_list, y_list)

function y_1 = euler(y, h)
    yp = @(y) -.5*y;
    y_1 = y + h*yp(y);
end

% facit tycker att h = 4 är stabil. Den är begränsad antar jag, men...?