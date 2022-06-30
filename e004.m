clear all; close; clc;

counter = 0;
palendrome = [];
k_ = [];
j_ = [];

for k = 100:999
    for j = 100:999
        string_ = num2str(k*j);
        if string_(1) == string_(end)
            if string_(2) == string_(end-1)
                if string_(3) == string_(end-2)
                    palendrome(end+1) = str2num(string_);
                    k_(end+1) = k;
                    j_(end+1) = j;
                end
            end
        end
    end
end

disp(max(palendrome));
