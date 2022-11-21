clc; clear; close all;

test_d = @(phi) b_f(phi) - 1.83;

d = fzero(test_d, 5*(2*pi/360))


%function x_f = test(d)
%
%
%x_end = b_f(d);
%
%x_f = x_end - 5;
%end