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
    elseif p2_royal
        continue
    end

    % Straight flush
    % In preparation, pick out the suits and values.
    p1_suits = 0;
    p1_values = 0;
    p2_suits = 0;
    p2_values = 0;

end
