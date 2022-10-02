% Spiral primes
clc; clear all; close all; format long;

% first: try to construct a 7x7 matrix like the first ex
size = input("Enter size: ");
%A = zeros(size,size);
%A(ceil(size/2),ceil(size/2)) = 1;
% leave this out for now.
%disp(A) % This is a good start...
value = 1;
%while value <= size^2
    %disp(value)
    value = value + 1;
%end

% C code declares integers statically. Not needed here, but let's.
i = 0; j = 0; ascendingNumbers = 0; leftAndTop = 0; rightAndBottom = 0;
% ... and we already did size.

% Assign values. We could have done this just now...
leftAndTop = 1;     % leftAndTop = 0; 
rightAndBottom = size;    % rightAndBottom = size-1;
ascendingNumbers = size^2;
% roight, this was since Matlab indexing starts at 1.

% The next step is "filling the array". In my case the matrix.
%... I can't really do their 
% for (i = 1; i <= size/2; i++, leftAndTop++, rightAndBottom--)
%.... but i could translate it into a while loop and increment/decrement
% counters instead.5
A = [];
counter_prime = 0;
i = 1;  % they call the following loop /*filling the array*/
quotient = 1;   % for now.
while quotient > .1
    i = 1;  % they call the following loop /*filling the array*/
    quotient = 1;   % for now.
    leftAndTop = 1;
    rightAndBottom = size;    % rightAndBottom = size-1;
    ascendingNumbers = size^2;
    A = [];
    while i <= size / 2
        if isprime(ascendingNumbers)
            counter_prime = counter_prime + 1;
        end
        % /*right to left*/
        j = rightAndBottom;
        while j > leftAndTop    % do strict: Matlab uses 1 as beginning.
            A(rightAndBottom, j) = ascendingNumbers;
            j = j - 1; ascendingNumbers = ascendingNumbers - 1;
        end
        if isprime(ascendingNumbers)
            counter_prime = counter_prime + 1;
        end
    
        % /*bottom to top*/
        j = rightAndBottom;
        while j > leftAndTop    % do strict: Matlab uses 1 as beginning.
            A(j, leftAndTop) = ascendingNumbers;
            j = j - 1; ascendingNumbers = ascendingNumbers - 1;
        end
        if isprime(ascendingNumbers)
            counter_prime = counter_prime + 1;
        end
    
        % /*left to right*/
        j = leftAndTop;
        while j < rightAndBottom    % do strict: Matlab uses 1 as beginning.
            A(leftAndTop, j) = ascendingNumbers;
            j = j + 1; ascendingNumbers = ascendingNumbers - 1;
        end
        if isprime(ascendingNumbers)
            counter_prime = counter_prime + 1;
        end
    
        % /*top to bottom*/
        j = leftAndTop; % let it start at the same time as before
        while j < rightAndBottom
            A(j, rightAndBottom) = ascendingNumbers;
            j = j + 1; ascendingNumbers = ascendingNumbers - 1;
        end
        if isprime(ascendingNumbers)
            counter_prime = counter_prime + 1;
        end
    
        i = i + 1;
        leftAndTop = leftAndTop + 1;
        rightAndBottom = rightAndBottom - 1;
    end
    
    % They fill the center.
    % /*fill center for odd size*/
    if mod(size, 2) == 1    % right? Equal to one should mean odd.
        A(leftAndTop, j-1) = ascendingNumbers;
    end
    size = size + 1;

    % I need to check if we're done.
    quotient = counter_prime / (2*(size - 1))
% Right now this places it off center by like 3, we'll fix that.
% I've got other shit now though <3.
disp(A)
end

disp(A)
disp(counter_prime)
disp(size)
disp(quotient)
% ... this is essentially their shit right? Continue...
% In Matlab, array indexing starts at 1. C seems to start at 0. ... .

% Inspiration written i C of code creating the spiral pattern
% https://stackoverflow.com/questions/53325542/how-to-write-a-code-that-prints-an-specific-numerical-spiral-pattern-in-c-using
% That code fills it top left to center in ascending order, HOWEVER,
% I should be able to modify it.
