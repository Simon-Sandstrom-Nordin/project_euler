function four_rank = four_of_a_kind(hand)
card_values = values(hand);
unique_values = unique(card_values);
if length(unique_values) > 2
    four_rank = 0;  % no four of a kind if three unique cards exist.
else    % four of a kind ga aru.
    % identify impostor card.
    if card_values(1) == card_values(2)
        four_rank = card_values(1);
    elseif card_values(1) == card_values(3)
        four_rank = card_values(1);
    elseif card_values(1) == card_values(4)
        four_rank = card_values(1);
    elseif card_values(1) == card_values(5)
        four_rank = card_values(1);
    else    % if we get this far then the first card was the IMPOSTOR CARD.
        four_rank = card_values(2);
    end
end

end
