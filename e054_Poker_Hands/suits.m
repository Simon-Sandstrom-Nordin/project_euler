function suit_array = suits(hand)
suit_array = char();
for k = 1:5
    suit_array(end+1) = hand(k, 2);
end
end
