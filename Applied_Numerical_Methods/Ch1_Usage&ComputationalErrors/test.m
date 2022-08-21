clc; clear; close;
p(2,3)
q(3)
m(1)

% anonomous vector-valued functions are possible, think in matrices:
f = @(x) [x; 0; 2*x];   % This notation seems way more compact...
f(2)

% functions are defined at the end of the script.
function u = p(x,y)
u = x + y;
end

function vector = q(x)
vector = zeros(1,2);    % not neccessary? 
vector(1) = x;
vector(2) = x.^2;
end

function h = m(x)
h(1) = x;
h(3) = 2*x; % this seems to create h(2) = 0... to fill blancs?
end

% comments seem ok to leave after function definitions... not read? .
