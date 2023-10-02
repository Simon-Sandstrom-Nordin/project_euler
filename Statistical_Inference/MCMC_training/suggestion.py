import numpy as np
from scipy.special import gamma
from scipy import stats
from matplotlib import pyplot as plt


# acceptance-rejection method
# unnormalized pdf
# def pdf(x, alpha, beta, t):
#    if x == 0:
#        return ((1-t)+t*x**(alpha-1)*(1-x)**(beta-1)*gamma(alpha+beta)/(gamma(alpha)*gamma(beta)))/(np.sqrt(t*(1-t)))
#    else:
#        return t * gamma(alpha + beta) / (gamma(alpha) * gamma(beta)) / (np.sqrt(t * (1 - t)))


#a = -3
#b = 3
#n = 10000
#x_lin = np.linspace(a, b)
#plt.figure(1)
#plt.plot(x_lin, pdf(x_lin))
plt.show()

# prior_t = stats.uniform(loc=0, scale=1)  # Uniform prior for t
prior_t = stats.beta(a=.5, b=.5)  # Uniform prior for t
# prior_alpha = stats.norm(loc=mean_alpha, scale=std_alpha)  # Normal prior for alpha
# prior_beta = stats.gamma(a=shape, scale=scale)  # Gamma prior for beta
# prior_x = stats.norm(loc=mean_x, scale=std_x)  # Normal prior for x
prior_x = stats.beta(a=.5, b=.5)  # Normal prior for x


#def likelihood(t, alpha, beta, x):
#    if x == 0:
#        return ((1-t)+t*x**(alpha-1)*(1-x)**(beta-1)*gamma(alpha+beta)/(gamma(alpha)*gamma(beta)))/(np.sqrt(t*(1-t)))
#    else:
#        return t * gamma(alpha + beta) / (gamma(alpha) * gamma(beta)) / (np.sqrt(t * (1 - t)))
def likelihood(x, alpha, beta, t):
    print("Like")
    print(alpha)
    print(beta)
    print(t)
    alpha = alpha[0]
    beta = beta[0]
    t = t[0]
    all_terms = 1
    for x_el in x:
#        print(np.sqrt(t * (1 - t)))
#        if np.isnan(np.sqrt(t * (1 - t))):
#            print("isnan")
#            print(t)
        if x_el == 0:
            term = ((1-t)+t*x_el**(alpha-1)*(1-x_el)**(beta-1)*gamma(alpha+beta)/(gamma(alpha)*gamma(beta)))/(np.sqrt(t*(1-t)))
        else:
            term = t * gamma(alpha + beta) / (gamma(alpha) * gamma(beta)) / (np.sqrt(t * (1 - t)))
        all_terms = all_terms*term
    return all_terms
    #if np.any(x == 0):
    #    term_1 = ((1 - t) + t * x**(alpha - 1) * (1 - x)**(beta - 1) * gamma(alpha + beta) / (gamma(alpha) * gamma(beta))) / (np.sqrt(t * (1 - t)))
    #      term_1[x != 0] = 0  # Set the values where x != 0 to 0
    #else:
    #    term_1 = 0

    #term_2 = t * gamma(alpha + beta) / (gamma(alpha) * gamma(beta)) / (np.sqrt(t * (1 - t)))
    #return term_1 + term_2


# posterior = lambda t, alpha, beta, x: prior_t.pdf(t) * prior_alpha.pdf(alpha) * prior_beta.pdf(beta) * prior_x.pdf(x) * likelihood(t, alpha, beta, x)
posterior = lambda t, alpha, beta, x: prior_t.pdf(t) * prior_x.pdf(x) * likelihood(t, alpha, beta, x)

# Markov Chain Monte Carlo (MCMC)
X0 = stats.uniform.rvs(size=1)
alpha0 = stats.uniform.rvs(size=1)
beta0 = stats.uniform.rvs(size=1)
t0 = stats.uniform.rvs(size=1)

plt.figure(2)

n = 1000
samples = [[alpha0, beta0, t0]]
x = [7.8,0.0,0.0,0.0,8.6,0.0,7.8,0.0,8.7,0.0,9.3,0.0,0.0,0.0,0.0,8.6,7.1,0.0]
for i in range(n):
    plt.clf()

    # is this how you'd generalize to higher dimensions?
    # x_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)
    alpha_guess = stats.norm.rvs(loc=samples[-1][0], scale=1, size=1)
    beta_guess = stats.norm.rvs(loc=samples[-1][1], scale=1, size=1)
    t_guess = stats.norm.rvs(loc=samples[-1][2], scale=1, size=1)

    # Reject proposed samples if t is out of bounds
    if t_guess <= 0 or t_guess >= 1:
        samples.append(samples[-1])
        print("t out of bounds")
    else:
        R = posterior(x, alpha_guess, beta_guess, t_guess) / posterior(x, samples[-1][0],
                                                                             samples[-1][1], samples[-1][2])
        print("R")
        print(R)
        u = stats.uniform.rvs(size=1)
        if u < min(R, 1):
            samples.append([alpha_guess, beta_guess, t_guess])
        else:
            samples.append(samples[-1])
        # plt.plot(x_lin, pdf(x_lin))
        # plt.title("MCMC method for N(0,1) with X0 =" + str(X0) + ", n = " + str(n))
        # plt.hist(samples, stacked=True, density=True)
        # plt.pause(.001)
# plt.show()
