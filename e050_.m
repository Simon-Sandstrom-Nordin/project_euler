clc; clear; close all;

%... I'll just assume is't wrong? Here's my justification:

%list = [];

%counter = 2;    % 2 is the first prime number
%while length(list) < 24
%    if isprime(counter)
%        list(end + 1) = counter;
%    end
%    counter = counter + 1;
%end

%disp(list')
%disp(sum(list))

% It has to be a sequence that doesn't necessarily begin with 2 でしょ?
%　ええ、平仮名はここにいいです。
% そう、平仮名はここで働いています。<- Hatarai? is translate messing with me?
% Is this more like "Hiragana is working here" rather than "Hiragana works
% here? ... ok, back to MATLAB:

% So it has to be a sequence that can start on something other than 2.
% Because then it works, since 963 = 953 - 2 - 3 - 5, meaning that the
% first three primes are excluded from the sequence. Then my 24 term
% sequence becomes a 21 term sequence and things are good.

% generate list of primes:
list = [];
counter = 2;
while length(list) < 100    % I want one hundred primes please.
    if isprime(counter)
        list(end+1) = counter;
    end
end

max_prime = 0;
max_terms = 0;
for start = 1 : length(list)
    for cut = start : length(list)
        for end_point = cut : length(list)
            sum_of_terms = list(cut:end_point);
            if length(list(cut:end_point)) > max_terms && isprime(sum_of_terms)
                max_terms = length(list(cut:end_point));
                max_prime = sum_of_terms;
            end
        end
    end
end
