function win_boolean = royal_flush(hand)
    flush_clubs = ['TC'; 'JC'; 'QC'; 'KC'; 'AC'];
    flush_hearts = ['TH'; 'JH'; 'QH'; 'KH'; 'AH'];
    flush_spades = ['TS'; 'JS'; 'QS'; 'KS'; 'AS'];
    flush_diamonds = ['TD'; 'JD'; 'QD'; 'KD'; 'AD'];
    
    % The type of sort doesn't really matter. In this case
    % (I think) it sorts alphabetically based on the first
    % character of each element of the array. Which is nice.
    % But as long as I know the sorting is consistent, it'll
    % be fine.
    sorted_hand = sort(hand);
    sorted_clubs = sort(flush_clubs);
    sorted_hearts = sort(flush_hearts);
    sorted_spades = sort(flush_spades);
    sorted_diamonds = sort(flush_diamonds);

    if sorted_hand == sorted_clubs
        win_boolean = true;
    elseif sorted_hand == sorted_hearts
        win_boolean = true;
    elseif sorted_hand == sorted_spades
        win_boolean = true;
    elseif sorted_hand == sorted_diamonds
        win_boolean = true;
    else
        win_boolean = false;
    end

end
