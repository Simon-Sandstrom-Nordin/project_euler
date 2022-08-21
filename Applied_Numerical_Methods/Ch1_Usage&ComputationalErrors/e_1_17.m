vector = zeros(10001, 1);

counter = 0;
while counter < length(vector)
    vector(counter+1) = f(counter);
    counter = counter + 1;
    disp(counter)
end

disp(vector(end))

disp(sum(vector))
disp(sum(vector) - pi^2 / 8)

function term = f(n)
    term = 1 / (2*n + 1)^2;
end
