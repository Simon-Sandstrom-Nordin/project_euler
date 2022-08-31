function value_array = values(hand)
value_array = [];
for k = 1:5
    value = hand(k, 1);
    integer_list = [2,3,4,5,6,7,8,9];
    % just to check that I did the indexing right. I did.
    %disp(value)
    
    % They're all characters. Even like '2'.
    %class(value)

    if ismember(str2num(value), integer_list)
        value_array(end + 1) = str2num(value); 
    else
        if value == 'T'
            value_array(end + 1) = 10;
        elseif value == 'J'
            value_array(end + 1) = 11;
        elseif value == 'Q'
            value_array(end + 1) = 12;
        elseif value == 'K'
            value_array(end + 1) = 13;
        elseif value == 'A'
            value_array(end + 1) = 14;
        end
    end
end
end
