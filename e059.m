% problem 59: XOR decryption

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
length(alphabet)

for first = 1:26
    for second = 1:26
        for third = 1:26
            string = alphabet(first) + alphabet(second) + alphabet(third);
        end
    end
end

% ciphers.
