clc; clear all; close all;

counter = 0;

for k=1:1000
    %test lines
    %if k ~= 115
    %    continue
    %end
    ones = mod(k, 10);
    tens = mod(k, 100) - ones;
    hundreds = mod(k, 1000) - tens - ones;

    % 1000
    if k == 1000
       counter = counter + 3 + 8; % one thousand
    end

    % 100s
    if hundreds == 100
        counter = counter + 3 + 7; % one hundred
        if ones ~= 0 || tens ~= 0
            counter = counter + 3; % and
        end
    end

    if hundreds == 200
        counter = counter + 3 + 7; % two
        if ones ~= 0 || tens ~= 0
            counter = counter + 3; % and
        end
    end

    if hundreds == 300
        counter = counter + 5 + 7; % three
        if ones ~= 0 || tens ~= 0
            counter = counter + 3; % and
        end
    end

    if hundreds == 400
        counter = counter + 4 + 7; % four
        if ones ~= 0 || tens ~= 0
            counter = counter + 3; % and
        end
    end

    if hundreds == 500
        counter = counter + 4 + 7; % five
        if ones ~= 0 || tens ~= 0
            counter = counter + 3; % and
        end
    end

    if hundreds == 600
        counter = counter + 3 + 7; % six
        if ones ~= 0 || tens ~= 0
            counter = counter + 3; % and
        end
    end

    if hundreds == 700
        counter = counter + 5 + 7; % seven
        if ones ~= 0 || tens ~= 0
            counter = counter + 3; % and
        end
    end

    if hundreds == 800
        counter = counter + 5 + 7; % eight
        if ones ~= 0 || tens ~= 0
            counter = counter + 3; % and
        end
    end

    if hundreds == 900
        counter = counter + 4 + 7; % nine
        if ones ~= 0 || tens ~= 0
            counter = counter + 3; % and
        end
    end

    % "unique numbers": 10-19
    
    if tens == 10 && ones == 0
        counter = counter + 3;  % ten
        continue
    end

    if tens == 10 && ones == 1
        counter = counter + 6;  % eleven
        continue
    end

    if tens == 10 && ones == 2
        counter = counter + 6;  % twelve
        continue
    end
    
    if tens == 10 && ones == 3
        counter = counter + 8;  % thirteen
        continue
    end

    if tens == 10 && ones == 4
        counter = counter + 8;  % fourteen
        continue
    end

    if tens == 10 && ones == 5
        counter = counter + 7;  % fifteen
        continue
    end
    
    if tens == 10 && ones == 6
        counter = counter + 7;  % sixteen
        continue
    end

    if tens == 10 && ones == 7
        counter = counter + 9;  % seventeen
        continue
    end

    if tens == 10 && ones == 8
        counter = counter + 8;  % eighteen
        continue
    end

    if tens == 10 && ones == 9
        counter = counter + 8;  % nineteen
        continue
    end

    % 10s without the 10
    if tens == 20
        counter = counter + 6;  % twenty
    end

    if tens == 30
        counter = counter + 6;  % thirty
    end

    if tens == 40
        counter = counter + 5;  % forty
    end

    if tens == 50
        counter = counter + 5;  % fifty
    end

    if tens == 60
        counter = counter + 5;  % sixty
    end

    if tens == 70
        counter = counter + 7;  % seventy
    end

    if tens == 80
        counter = counter + 6;  % eighty
    end

    if tens == 90
        counter = counter + 6;  % ninety
    end

    if ones == 1
        counter = counter + 3;  % one
    end

    if ones == 2
        counter = counter + 3;  % two
    end

    if ones == 3
        counter = counter + 5;  % three
    end

    if ones == 4
        counter = counter + 4;  % four
    end

    if ones == 5
        counter = counter + 4;  % five
    end

    if ones == 6
        counter = counter + 3;  % six
    end

    if ones == 7
        counter = counter + 5;  % seven
    end

    if ones == 8
        counter = counter + 5;  % eight
    end

    if ones == 9
        counter = counter + 4;  % nine
    end

end

disp(counter)
