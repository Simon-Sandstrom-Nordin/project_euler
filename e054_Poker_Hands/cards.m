function hand = cards(index, char_array)
card_1 = char_array(index: index + 1);
card_2 = char_array(index + 2: index + 3);
card_3 = char_array(index + 4: index + 5);
card_4 = char_array(index + 6 : index + 7);
card_5 = char_array(index + 8: index + 9);
hand = [card_1; card_2; card_3; card_4; card_5];
end
