function [t_new, y_new] = euler_forwards(t, y, h, function_handle)
    % function_handle is derivative of y, of t and y
    y_new = y + h*function_handle(t, y);
    t_new = t + h;  % h is step length.
end
