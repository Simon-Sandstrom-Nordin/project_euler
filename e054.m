% IT WAS a bad idea to try to do all of this in one chunk of code. Note
% till next time: Use function files to subdivide tasks like this one. I'll
% have one function for checking rank, one for suit, maybe even seperate
% functions for checking the different win conditions. Now I'll leave the
% scene - *swhoosh-

% Poker hands! detemine who wins given two hands.
clc; clear all; close all;

% progress report (29/8): it checked for a straight flush, and it checked
% for for cards of the same suit, and now it should check for a four of
% a kind but it broke instead. ... well, I'll maybe use function files
% next time. Yep... this became very complicated very quickly and it became
% difficult to get an overview of the code since it's all chunked into one
% block of spagetti code. This is just how I would play factorio. No plan,
% and everything kept growing like a cancer on the screen. Also how I would
% live my life <3.

fileID = fopen('poker.txt', 'r');
string = fscanf(fileID, '%s');

% truncate string from the left to get cards!
player_one_wins = 0;
counter = 1;
while counter < 20000    % there are 1000 rows of 20 characters. Math this.

    % player one's hand
    player_1_card_1 = string(counter: counter + 1);
    player_1_card_2 = string(counter + 2: counter + 3);
    player_1_card_3 = string(counter + 4: counter + 5);
    player_1_card_4 = string(counter + 6 : counter + 7);
    player_1_card_5 = string(counter + 8: counter + 9);
    first_hand_char_array = [player_1_card_1; player_1_card_2; ...
        player_1_card_3; player_1_card_4; player_1_card_5];

    % player two's hand
    player_2_card_1 = string(counter + 10: counter + 11);
    player_2_card_2 = string(counter + 12: counter + 13);
    player_2_card_3 = string(counter + 14: counter + 15);
    player_2_card_4 = string(counter + 16: counter + 17);
    player_2_card_5 = string(counter + 18: counter + 19);
    second_hand_char_array = [player_2_card_1; player_2_card_2; ...
        player_2_card_3; player_2_card_4; player_2_card_5];
    % ... you got that character array at second hand? :P

    % increment counter by 10 cards, for next round.
    counter = counter + 20;

    % Check win conditions
    player_1_won = false;   % for now, let's check if they won.

    % Does anyone have a Royal flush?
    flush_clubs = ['TC'; 'JC'; 'QC'; 'KC'; 'AC'];
    flush_hearts = ['TH'; 'JH'; 'QH'; 'KH'; 'AH'];
    flush_spades = ['TS'; 'JS'; 'QS'; 'KS'; 'AS'];
    flush_diamonds = ['TD'; 'JD'; 'QD'; 'KD'; 'AD'];
    if first_hand_char_array == flush_clubs
        player_1_won = true;
    elseif first_hand_char_array == flush_hearts
        player_1_won = true;
    elseif first_hand_char_array == flush_spades
        player_1_won = true;
    elseif first_hand_char_array == flush_diamonds
        player_1_won = true;
    elseif second_hand_char_array == flush_clubs
        continue
    elseif second_hand_char_array == flush_hearts
        continue
    elseif second_hand_char_array == flush_spades
        continue
    elseif second_hand_char_array == flush_diamonds
        continue
    end

    if player_1_won %not that it matters, p1 here has no win by royal flush.
        player_one_wins = player_one_wins + 1;    % give 'em points
        continue
    end

    % "continue" brings the code lens to the next iteration of the while
    % loop, and skips whatever code would have been left to be excecuted
    % (in the loop). I already incremented the counter, so it won't become
    % an endless loop. Here it just signals that player two won.

    % -------------------------- space for checking straight flushes.

    % Does anyone have four of a kind?
    player_1_has_4_of_a_kind = false; p1_4_of_a_kind_rank = "";
    player_2_has_4_of_a_kind = false; p2_4_of_a_kind_rank = "";
    % ... placeholders, we'll check and see-

    % first, let's pick out the values of each card:
    p1_value_1 = first_hand_char_array(1,1);
    p1_value_2 = first_hand_char_array(2,1);
    p1_value_3 = first_hand_char_array(3,1);
    p1_value_4 = first_hand_char_array(4,1);
    p1_value_5 = first_hand_char_array(5,1);
    p1_twos = 0; p1_threes = 0; p1_fours = 0; p1_fives = 0;
    p1_sixes = 0; p1_sevens = 0; p1_eights = 0; p1_nines = 0;
    p1_tens = 0; p1_jacks = 0; p1_queens = 0; p1_kings = 0; p1_aces = 0;
    p1_value_list = ...
        {p1_value_1, p1_value_2, p1_value_3, p1_value_4, p1_value_5};
    % I made the lists as cell arrays since letters are involved.
    p2_value_1 = first_hand_char_array(1,1);
    p2_value_2 = first_hand_char_array(2,1);
    p2_value_3 = first_hand_char_array(3,1);
    p2_value_4 = first_hand_char_array(4,1);
    p2_value_5 = first_hand_char_array(5,1);
    p2_twos = 0; p2_threes = 0; p2_fours = 0; p2_fives = 0;
    p2_sixes = 0; p2_sevens = 0; p2_eights = 0; p2_nines = 0;
    p2_tens = 0; p2_jacks = 0; p2_queens = 0; p2_kings = 0; p2_aces = 0;
    p2_value_list = ...
        {p2_value_1, p2_value_2, p2_value_3, p2_value_4, p2_value_5};

    % Mondai: lettered ranks are difficult to compare. Convert to integers.
    for k = 1:5
        value = char(p1_value_list(k));
        if value == 'T'
            p1_value_list(k) = {'10'};
        elseif value == 'J'
            p1_value_list(k) = {'11'};
        elseif value == 'Q'
            p1_value_list(k) = {'12'};
        elseif value == 'K'
            p1_value_list(k) = {'13'};
        elseif value == 'A'
            p1_value_list(k) = {'14'};
        end
        % do it for the other player while you're at it
        value = char(p2_value_list(k));
        if value == 'T'
            p2_value_list(k) = {'10'};
        elseif value == 'J'
            p2_value_list(k) = {'11'};
        elseif value == 'Q'
            p2_value_list(k) = {'12'};
        elseif value == 'K'
            p2_value_list(k) = {'13'};
        elseif value == 'A'
            p2_value_list(k) = {'14'};
        end
    end

    % just to check that the cell arrays now only contain numbers:
    % disp(p1_value_list);

    for k = 1:5     % length(p1_suit_list) = 5, i.e. one hand is five cards
        value = char(p1_value_list(k));
        if value == '2'
            p1_twos = p1_twos + 1;
        elseif value == '3'
            p1_threes = p1_threes + 1;
        elseif value == '4'
            p1_fours = p1_fours + 1;
        elseif value == '5'
            p1_fives = p1_fives + 1;
        elseif value == '6'
            p1_sixes = p1_sixes + 1;
        elseif value == '7'
            p1_sevens = p1_sevens + 1;
        elseif value == '8'
            p1_eights = p1_eights + 1;
        elseif value == '9'
            p1_nines = p1_nines + 1;        
        elseif value == '10'
            p1_tens = p1_tens + 1;
        elseif value == '11'
            p1_jacks = p1_jacks + 1;
        elseif value == '12'
            p1_queens = p1_queens + 1;
        elseif value == '13'
            p1_kings = p1_kings + 1;
        elseif value == '14'
            p1_aces = p1_aces + 1;
        end
    end
    if (p1_twos >= 4) || (p1_threes >= 4) || (p1_fours >= 4) || ...
       (p1_fives >= 4) || (p1_sixes >= 4) || (p1_sevens >= 4) || ...
       (p1_eights >= 4) || (p1_nines >= 4) || (p1_tens >= 4) || ...
       (p1_jacks >= 4) || (p1_queens >= 4) || (p1_kings >= 4) || ...
       (p1_aces >= 4)
        player_1_has_4_of_a_kind = true;

        % also check rank of four of a kind... it'll be enough to check 3.
        if p1_value_1 == p1_value_2
            p1_4_of_a_kind_rank = p1_value_2;
        else
            p1_4_of_a_kind_rank = p1_value_3;
        end
    end

    % Now, let's check if player 2 has four of a kind...

    for k = 1:5     % length(p1_suit_list) = 5, i.e. one hand is five cards
        value = char(p2_value_list(k));
        if value == '2'
            p2_twos = p2_twos + 1;
        elseif value == '3'
            p2_threes = p2_threes + 1;
        elseif value == '4'
            p2_fours = p2_fours + 1;
        elseif value == '5'
            p2_fives = p2_fives + 1;
        elseif value == '6'
            p2_sixes = p2_sixes + 1;
        elseif value == '7'
            p2_sevens = p2_sevens + 1;
        elseif value == '8'
            p2_eights = p2_eights + 1;
        elseif value == '9'
            p2_nines = p2_nines + 1;        
        elseif value == '10'
            p2_tens = p2_tens + 1;
        elseif value == '11'
            p2_jacks = p2_jacks + 1;
        elseif value == '12'
            p2_queens = p2_queens + 1;
        elseif value == '13'
            p2_kings = p2_kings + 1;
        elseif value == '14'
            p2_aces = p2_aces + 1;
        end
    end
    if (p2_twos >= 4) || (p2_threes >= 4) || (p2_fours >= 4) || ...
       (p2_fives >= 4) || (p2_sixes >= 4) || (p2_sevens >= 4) || ...
       (p2_eights >= 4) || (p2_nines >= 4) || (p2_tens >= 4) || ...
       (p2_jacks >= 4) || (p2_queens >= 4) || (p2_kings >= 4) || ...
       (p2_aces >= 4)
        player_2_has_4_of_a_kind = true;

        % also check rank of four of a kind... it'll be enough to check 3.
        if p2_value_1 == p2_value_2
            p2_4_of_a_kind_rank = p2_value_2;
        else
            p2_4_of_a_kind_rank = p2_value_3;
        end
    end

    % now let's compare their hands...
    if player_1_has_4_of_a_kind && (player_1_has_4_of_a_kind == false)
        player_1_won = true;
    elseif (player_1_has_4_of_a_kind == false) && player_1_has_4_of_a_kind
        continue    % player 2 won
    elseif player_1_has_4_of_a_kind && player_2_has_4_of_a_kind
        if (p1_4_of_a_kind_rank > p2_4_of_a_kind_rank)
            player_1_won = true;
        elseif (p1_4_of_a_kind_rank < p2_4_of_a_kind_rank)
            continue    % player 2 won
        else    % they have the same rank...
            % check highest valued remaining card. If those are of the same
            % rank, then ...? noone wins?
            % No, there's a clear winner according to instructions.
            
            % find remaining card for each player
            remaining_card_p1 = ""; remaining_card_p2 = "";
            
            for k = 1:5
                if first_hand_char_array(k, 1) ~= p1_4_of_a_kind_rank
                    remaining_card_p1 = first_hand_char_array(k);
                end
            end

            for k = 1:5
                if second_hand_char_array(k, 1) ~= p2_4_of_a_kind_rank
                    remaining_card_p2 = second_hand_char_array(k);
                end
            end

            if remaining_card_p1(1,1) > remaining_card_p1(1,2)
                player_1_won = true;
            end

            if remaining_card_p2(1,1) < remaining_card_p2(1,2)
                continue    % player 2 won
            end

        end
    end


    










    if player_1_won
        player_one_wins = player_one_wins + 1;    % give 'em points
    end

end

disp(player_one_wins)

% note: player one never wins by straigh flush? Does he/she lose to it? 

% more notes: instructions say there's a clear winner for every hand. No
% need to deal with draws.

% notes on the rules of 'Poker':
% High Card < One Pair < Two pairs < Three of a Kind < Straight <
% Flush < Full House < Four of a Kind < Straight flush < Royal Flush



%% Trash Code: (faulty ideas and broken algorithms)    
%    p1_value_counter = 0;  % now count the # of same value cards
%    if p1_value_1 == p1_value_2
%        p1_value_counter = p1_value_counter + 1;
%    end
%    if p1_value_2 == p1_value_2
%        p1_value_counter = p1_value_counter + 1;
%    end
%    if p1_value_1 == p1_value_2
%        p1_value_counter = p1_value_counter + 1;
%    end
%    if p1_value_1 == p1_value_2
%        p1_value_counter = p1_value_counter + 1;
%    end
%    
%    p2_value_1 = first_hand_char_array(1,1);
%    p2_value_3 = first_hand_char_array(3,1);
%    p2_value_4 = first_hand_char_array(4,1);
%    p2_value_5 = first_hand_char_array(5,1);
%   
    % now check four of a kind... just copy code, and change the index
%    p1_value_1 = first_hand_char_array(1,1);
%    p1_value_2 = first_hand_char_array(2,1);
%    p1_value_3 = first_hand_char_array(3,1);
%    p1_value_4 = first_hand_char_array(4,1);
%    p1_value_5 = first_hand_char_array(5,1);

%    if (p1_suit_1 == p1_suit_2) && (p1_suit_2 == p1_suit_3) && ...
%            (p1_suit_3 == p1_suit_4) && (p1_suit_4 == p1_suit_5)
%        player_1_won = true;
%    end

%    if (p2_suit_1 == p2_suit_2) && (p2_suit_2 == p2_suit_3) && ...
%            (p2_suit_3 == p2_suit_4) && (p2_suit_4 == p2_suit_5)
        % continue
%    end
    


    % ... let's pick out our suits:
%    p1_suit_1 = first_hand_char_array(1,2);
%    p1_suit_2 = first_hand_char_array(2,2);
%    p1_suit_3 = first_hand_char_array(3,2);
%    p1_suit_4 = first_hand_char_array(4,2);
%    p1_suit_5 = first_hand_char_array(5,2);
%    p1_clubs = 0; p1_hearts = 0; p1_spades = 0; p1_diamonds = 0;
%    p1_suit_list = [p1_suit_1, p1_suit_2, p1_suit_3, p1_suit_4, p1_suit_5];
%    for k = 1:5     % length(p1_suit_list) = 5, i.e. one hand is five cards
%        suit = p1_suit_list(k);
%        if suit == 'C'
%            p1_clubs = p1_clubs + 1;
%        elseif suit == 'H'
%            p1_hearts = p1_hearts + 1;
%        elseif suit == 'S'
%            p1_spades = p1_spades + 1;
%        else
%            p1_diamonds = p1_diamonds + 1;
%        end
%    end
%    if (p1_clubs >= 4) || (p1_hearts >= 4) || (p1_spades >= 4) || (p1_diamonds >= 4)
%        player_1_won = true;
%    end
%    p2_suit_1 = second_hand_char_array(1, 2);
%    p2_suit_2 = second_hand_char_array(2, 2);
%    p2_suit_3 = second_hand_char_array(3, 2);
%    p2_suit_4 = second_hand_char_array(4, 2);
%    p2_suit_5 = second_hand_char_array(5, 2);
%    p2_clubs = 0; p2_hearts = 0; p2_spades = 0; p2_diamonds = 0;
%    p2_suit_list = [p2_suit_1, p2_suit_2, p2_suit_3, p2_suit_4, p2_suit_5];
%    for k = 1:5     % length(p1_suit_list) = 5, i.e. one hand is five cards
%        suit = p2_suit_list(k);
%        if suit == 'C'
%            p2_clubs = p2_clubs + 1;
%        elseif suit == 'H'
%            p2_hearts = p2_hearts + 1;
%        elseif suit == 'S'
%            p2_spades = p2_spades + 1;
%        else
%            p2_diamonds = p2_diamonds + 1;
%        end
%    end
%     if (p2_clubs >= 4) || (p2_hearts >= 4) || (p2_spades >= 4) || (p2_diamonds >= 4)
%        continue    % player 2 won
%    end