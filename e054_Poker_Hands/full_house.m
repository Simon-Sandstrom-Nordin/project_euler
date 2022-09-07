function full_house_rank = full_house(hand)
card_values = values(hand);
unique_values = unique(card_values);
if length(unique_values) ~= 2
    full_house_rank = [0,0];  % no full house if it's not only two ranks.
    return
end
% note: we've already checked for four of a kind. This means that the only
% other hand were there are two and only two unique values would be a full
% house.

% Identify which value is the tiplet and which value is the pair.
first = sum(ismember(card_values, card_values(1)));
second = sum(ismember(card_values, card_values(2)));
third = sum(ismember(card_values, card_values(3)));

% This catches all cases, think about it. We're looking for triplets.
triplet_index = 0;
if first == 3
    triplet_index = 1;
elseif second == 3
    triplet_index = 2;
elseif third == 3
    triplet_index = 3;
end
triplet_value = card_values(triplet_index);

% next find pair
pair_index = 0;
if first == 2
    pair_index = 1;
elseif second == 2
    pair_index = 2;
elseif third == 2
    pair_index = 3;
elseif fourth == 2
    pair_index = 4
end
pair_value = card_values(pair_index); 

% note about the ranking of full houses: Triplet first, then pair.
full_house_rank = [triplet_value, pair_value];
end
