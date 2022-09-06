function full_house_rank = full_house(hand)
card_values = values(hand);
unique_values = unique(card_values);
if length(unique_values) ~= 2
    full_house_rank = [0,0];  % no full house if it's not only two ranks.
    return
end


% note about the ranking of full houses: Triplet first, then pair.
full_house_rank = [triplet_value, pair_value];
end
