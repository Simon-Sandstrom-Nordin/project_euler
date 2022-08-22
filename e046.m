% Goldbach's other conjecture
clc; close; clear;

list = [];

searching = true;
current_number = 4; % Four is the first composite number,
                    % (composite: not prime).
while searching

    % check parity
    if mod(current_number, 2) == 0
        current_number = current_number + 1;
        continue
    end

    % check primality
    if isprime(current_number)
       current_number = current_number + 1;
       continue     % proceed to next iteration of while loop.
    end

    conjecture_holds_here = false;
    % check if it can be written as a sum of a prme and twice a square
    for current_prime = 1: current_number
        if isprime(current_prime)  % check primality
            for square = 1: current_number % overkill, but works
                if current_number == current_prime + 2*square^2
                   conjecture_holds_here = true; 
                end
            end
        end
    end
    disp(current_number)
    if conjecture_holds_here == false
        list(end + 1) = current_number;
        searching = false;
        break
    end
    current_number = current_number + 1;
end


disp(list)

% lesson learnt:  5777 is the smallest odd composite number that
%                 cannot be written as the sum of a prime and twice
%                 a square. Goldbach's other conjecture is false.
% (The conjecture {förmodan, opinion based on incomplete information},
% was that there was no such number).
