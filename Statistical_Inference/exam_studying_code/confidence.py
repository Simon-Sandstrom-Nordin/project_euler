import numpy as np

X = [-1.379, -4.004, 3.8, -1.797, .341]

m = np.mean(X)
n = len(X)

print([m - 2/np.sqrt(n) * 1.96, m + 2/np.sqrt(n) * 1.96])
# slarver :D !!!!! Skriv av rätt nästa gång <3
print([-np.inf, m + 4/np.sqrt(n) * 1.65])
print([m - 4/np.sqrt(n) * 1.65, np.inf])
# ... det är inte så lätt som att byta ut z-värdena för ensidiga
# intervall :(((
# Jo fast facit använder variancen istället för standardavvikelsen...
# av nån anledning. misstag eller missförstånd hos mig?

# nya
X = [-.34, .62, -.37, -.07, -.7,
     .07, -2.49, .7, -1.52, -.27]

m = np.mean(X)
n = len(X)

print([m - 2/np.sqrt(n) * 1.29, m + 2/np.sqrt(n) * 1.29])
#... they take some t-test, or with a t_{n-1, alpha} dist...
