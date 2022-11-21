clc; clear; close all;

test_d = @(d) b_f(d) - 5;

d = fzero(test_d, .02)


%function x_f = test(d)
%
%
%x_end = b_f(d);
%
%x_f = x_end - 5;
%end

