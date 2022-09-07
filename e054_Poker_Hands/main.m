% Poker hands main program
clc; clear; close all;

fileID = fopen("poker.txt", 'r');
char_array = fscanf(fileID, '%s');
% note: since like everything is an array in MATLAB,
% this "string" is a 1*20000 characher array.
% scratch that: according to stackoverflow and lehigh
% EVERYTHING in matlab is an array /is assumed to be.
% according to some answer on stackoverflow,
% matlab is like "I got a list" in python for all.
% I wonder if there are exceptions. I wonder if
% a try-catch structure is an exception. Continue!

p1_win_counter = 0; % This is what we want to know.
index = 1;   % This'll keep track of where we are.

while index < 2*10^4

    player_1_hand = cards(index, char_array);
    index = index + 10; % increment index.
    player_2_hand = cards(index, char_array);
    index = index + 10; % increment again for next round.

    % Royal flush
    p1_royal = royal_flush(player_1_hand);
    p2_royal = royal_flush(player_2_hand);
    if p1_royal
        p1_win_counter = p1_win_counter + 1;
        continue
    elseif p2_royal
        continue
    end

    % Straight flush
    p1_straight = flush(player_1_hand);
    p2_straight = flush(player_2_hand);
    if p1_straight > p2_straight
        p1_win_counter = p1_win_counter + 1;
        continue
    elseif p1_straight < p2_straight
        continue
    end

    % Four of a Kind
    p1_four_rank = four_of_a_kind(player_1_hand);
    p2_four_rank = four_of_a_kind(player_2_hand);
    if p1_four_rank > p2_four_rank
        p1_win_counter = p1_win_counter + 1;
        continue
    elseif p1_four_rank < p2_four_rank
        continue
    end

    % Full house % on form [triplet_value, pair_value]
    p1_full_house_rank = full_house(player_1_hand);
    p2_full_house_rank = full_house(player_2_hand);
    if p1_full_house_rank(1) > p2_full_house_rank(1)
        p1_win_counter = p1_win_counter + 1;
        continue
    elseif p1_full_house_rank(1) < p2_full_house_rank(1)
        continue
    elseif p1_full_house_rank(2) > p2_full_house_rank(2)
        p1_win_counter = p1_win_counter + 1;
        continue
    elseif p1_full_house_rank(2) < p2_full_house_rank(2)
        continue
    end


    disp(p1_win_counter);   % it never gets to this...

end

disp(p1_win_counter);

% Note 6:th of September 2022
%   Well, now the win counter doesn't increment at all.
%   For some reason, either the functions don't return
%   anything but zeros, or something like it.
%   On the plus side: I've tripped on the fact that you can pause
%   exeution on lines by clicking the line numbers on the left.
%   It also says something about "save file to synchronize breakpoints".
%   Interesting.

% Note 7:th of September 2022
%   It still doesn't increment the counter. Although I've found out that
%   with the "pause at line" thing I can also go one step at a time through
%   the code-lens and even enter functions and shit. And step out. Yep.
