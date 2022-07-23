function length = e026_help(number)

% convert number to string
number_string = string(number);

% convert string into character array
number_character = number_string{1};

% strip integer part and dot
number_character = number_character(3:end);

% initialize cycle length variable
length = 0;

last_character = number_character(1);
% iterate through string character array
for i = 1:length(number_character)

    % if number is repeted, check next occurence
    % (if we're not at the last character.)
    if number_character(i) == last_character && ...
                            i ~= number_character(length(number_character))
        for k = i+1:length(number_character)



        end
    end

end
length = length + 1;
end

% ... I don't quite know... : (
% but we learned about brace indexing!
% "string"{1} = 'string', meaning it converts it from the
% string data type to the charachter (class?... are dt's classes here?)

% I abandoned my dreams of completing this in MATLAB,
% since number to string doesn't preserve all digits.
% ... onward to Java?
% NO! Never give up! let's do this manually by listing all the numbers
% and counting them by eye... ... ... 