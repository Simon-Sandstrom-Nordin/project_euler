clc; close all; clear; format short;
% The RSA algorith is an assymetric cryptography algorithm.
% A data structure is a particular way of organizing data
%   in a computer so that it can be used effectively.
% Assymetric cryptography:
%   1. A client ( e.g. a browser) sends its public key to the
%      server and requests for some data.
%   2. The server encrypts the data using client's public key
%      and sends the encrypted data.
%   3. Client recieves the data and decrypts it.
% Now, instead of just copying off of GeeksforGeeks...
% 1. Client yeets public key to server.
% 2. Server encrypts data with public key and returns to sender.
% 3. Client catches data and decryps with their private key.
% -> even if public key chosen by client is known,
%    only the client can decrypt the message.

% Step one: generate public key.
%   choose 2 different primes.
P = 41; Q = 71;
%   take the product.
n = P*Q;    % = 2911
%   choose small integer exponent e not a factor of n (!= P && != Q)
%       and also 1 < e < phi(n) = (P - 1)(Q - 1) # Eulers totient f.
e = 5; % forgot at first! e cannot divide n. nvm...
% 1 < 3 < 40*70 = 2800
%       note: phi(n) returns number of relatively prime numbers to n.
%             if n is prime, then phi(n) = |{1,2,...,n-1| = n-1.
%             here | denotes cardinality, not MATLAB logical OR operator.
% thus our public key is made of (n, e) = (2911, 3)

% Step two: generate private key.
%   calculate phi(n) = 2800 % note: eulerPhi(n) works in MATLAB.
%       wonder: if you have the public key, then you know this value?
%        ... so only the next component is chosen by the client.
%   calculate private key d (d for decryption?... probs.)
%       d = (k*phi(n) + 1) / e, where k is chosen as some integer.
k = 2; %?arbitrary... as long as the results are computable I suppose.
% d = (k*eulerPhi(n) + 1) / e;    % doesn't show as an integer...?!
% ... I can calculate the modular inverse of the encryption
% key modulo λ(n) = φ(n) by hand using the extended euclidian algorithm...
