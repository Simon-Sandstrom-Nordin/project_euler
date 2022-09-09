function flush_rank = flush(hand)
suit_v = suits(hand);
% This is just if we have one at all.
if (suit_v(1) == suit_v(2)) && (suit_v(2) == suit_v(3)) && ...
        (suit_v(3) == suit_v(4)) && (suit_v(4) == suit_v(5))
    % leaving it blanc in MATLAB is the equivalent of doNothing
    ;   % if I want I can put a semi colon. As comfort.
else
    flush_rank = 0;
    return
end

% If the computer (compiler?) has started reading at this point,
% We know we have a flush. Question now is... which rank?
% Use poker rule in main.m

value_v = values(hand);
unique_value_v = unique(value_v);
sorted_unique_v = sort(unique_value_v);
flush_rank = sorted_unique_v;

% This'll pop out a vector of varying length... we'll deal with that.
end
