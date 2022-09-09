function straight_rank = straight_flush(hand)

    % clubs
    flush_clubs_1 = sort(['2C'; '3C'; '4C'; '5C'; '6C']);
    flush_clubs_2 = sort(['3C'; '4C'; '5C'; '6C'; '7C']);
    flush_clubs_3 = sort(['4C'; '5C'; '6C'; '7C'; '8C']);
    flush_clubs_4 = sort(['5C'; '6C'; '7C'; '8C'; '9C']);
    flush_clubs_5 = sort(['6C'; '7C'; '8C'; '9C'; 'TC']);
    flush_clubs_6 = sort(['7C'; '8C'; '9C'; 'TC'; 'JC']);
    flush_clubs_7 = sort(['8C'; '9C'; 'TC'; 'JC'; 'QC']);
    flush_clubs_8 = sort(['9C'; 'TC'; 'JC'; 'QC'; 'KC']);

    % hearts
    flush_hearts_1 = sort(['2H'; '3H'; '4H'; '5H'; '6H']);
    flush_hearts_2 = sort(['3H'; '4H'; '5H'; '6H'; '7H']);
    flush_hearts_3 = sort(['4H'; '5H'; '6H'; '7H'; '8H']);
    flush_hearts_4 = sort(['5H'; '6H'; '7H'; '8H'; '9H']);
    flush_hearts_5 = sort(['6H'; '7H'; '8H'; '9H'; 'TH']);
    flush_hearts_6 = sort(['7H'; '8H'; '9H'; 'TH'; 'JH']);
    flush_hearts_7 = sort(['8H'; '9H'; 'TH'; 'JH'; 'QH']);
    flush_hearts_8 = sort(['9H'; 'TH'; 'JH'; 'QH'; 'KH']);

    % spades
    flush_spades_1 = sort(['2S'; '3S'; '4S'; '5S'; '6S']);
    flush_spades_2 = sort(['3S'; '4S'; '5S'; '6S'; '7S']);
    flush_spades_3 = sort(['4S'; '5S'; '6S'; '7S'; '8S']);
    flush_spades_4 = sort(['5S'; '6S'; '7S'; '8S'; '9S']);
    flush_spades_5 = sort(['6S'; '7S'; '8S'; '9S'; 'TS']);
    flush_spades_6 = sort(['7S'; '8S'; '9S'; 'TS'; 'JS']);
    flush_spades_7 = sort(['8S'; '9S'; 'TS'; 'JS'; 'QS']);
    flush_spades_8 = sort(['9S'; 'TS'; 'JS'; 'QS'; 'KS']);

    % diamonds
    flush_diamonds_1 = sort(['2D'; '3D'; '4D'; '5D'; '6D']);
    flush_diamonds_2 = sort(['3D'; '4D'; '5D'; '6D'; '7D']);
    flush_diamonds_3 = sort(['4D'; '5D'; '6D'; '7D'; '8D']);
    flush_diamonds_4 = sort(['5D'; '6D'; '7D'; '8D'; '9D']);
    flush_diamonds_5 = sort(['6D'; '7D'; '8D'; '9D'; 'TD']);
    flush_diamonds_6 = sort(['7D'; '8D'; '9D'; 'TD'; 'JD']);
    flush_diamonds_7 = sort(['8D'; '9D'; 'TD'; 'JD'; 'QD']);
    flush_diamonds_8 = sort(['9D'; 'TD'; 'JD'; 'QD'; 'KD']);
    
    %   The sorting is important, since when comparing matrices the
    %   comparison is elememt-wise.
    %   ['1' '2' '3'] == ['2' '1' '3'] gives [0 0 1].
    %   an if-statement with a logical array as a condition needs all
    %   elements of the logical array to be ones, in order for the
    %   condition to be rendered as true.
    sorted_hand = sort(hand);
    if sorted_hand == flush_clubs_1 % rank 1
        straight_rank = 1;
    elseif sorted_hand == flush_hearts_1
        straight_rank = 1;
    elseif sorted_hand == flush_spades_1
        straight_rank = 1;
    elseif sorted_hand == flush_diamonds_1
        straight_rank = 1;
    elseif sorted_hand == flush_clubs_2 % rank 2
        straight_rank = 2;
    elseif sorted_hand == flush_hearts_2
        straight_rank = 2;
    elseif sorted_hand == flush_spades_2
        straight_rank = 2;
    elseif sorted_hand == flush_diamonds_2
        straight_rank = 2;
    elseif sorted_hand == flush_clubs_3 % rank 3
        straight_rank = 3;
    elseif sorted_hand == flush_hearts_3
        straight_rank = 3;
    elseif sorted_hand == flush_spades_3
        straight_rank = 3;
    elseif sorted_hand == flush_diamonds_3
        straight_rank = 3;
    elseif sorted_hand == flush_clubs_4 % rank 4
        straight_rank = 4;
    elseif sorted_hand == flush_hearts_4
        straight_rank = 4;
    elseif sorted_hand == flush_spades_4
        straight_rank = 4;
    elseif sorted_hand == flush_diamonds_4
        straight_rank = 4;
    elseif sorted_hand == flush_clubs_5 % rank 5
        straight_rank = 5;
    elseif sorted_hand == flush_hearts_5
        straight_rank = 5;
    elseif sorted_hand == flush_spades_5
        straight_rank = 5;
    elseif sorted_hand == flush_diamonds_5
        straight_rank = 5;
    elseif sorted_hand == flush_clubs_6 % rank 6
        straight_rank = 6;
    elseif sorted_hand == flush_hearts_6
        straight_rank = 6;
    elseif sorted_hand == flush_spades_6
        straight_rank = 6;
    elseif sorted_hand == flush_diamonds_6
        straight_rank = 6;
    elseif sorted_hand == flush_clubs_7 % rank 7
        straight_rank = 7;
    elseif sorted_hand == flush_hearts_7
        straight_rank = 7;
    elseif sorted_hand == flush_spades_7
        straight_rank = 7;
    elseif sorted_hand == flush_diamonds_7
        straight_rank = 7;
    elseif sorted_hand == flush_clubs_8 % rank 8
        straight_rank = 8;
    elseif sorted_hand == flush_hearts_8
        straight_rank = 8;
    elseif sorted_hand == flush_spades_8
        straight_rank = 8;
    elseif sorted_hand == flush_diamonds_8
        straight_rank = 8;
    else
        straight_rank = 0;
    end

end
