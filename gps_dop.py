import matplotlib.pyplot as plt
import numpy as np

# *DOP = f(digree)

digree = np.linspace(0, 90, 300)
GDOP = np.zeros(len(digree))
PDOP = np.zeros(len(digree))
HDOP = np.zeros(len(digree))
ZDOP = np.zeros(len(digree))
TDOP = np.zeros(len(digree))


for i in range(len(digree)):
    rad = digree[i] * 2 * np.pi / 360

    A = np.array(
        [
            [np.cos(rad), 0, np.sin(rad), 1],
            [1 / np.sqrt(2), 0, 1 / np.sqrt(2), 1],
            [-1 / 2 * np.sqrt(2), np.sqrt(3 / 2) / 2, 1 / np.sqrt(2), 1],
            [-1 / 2 * np.sqrt(2), -np.sqrt(3 / 2) / 2, 1 / np.sqrt(2), 1],
        ]
    )
    AT = A.T
    M_inverse = np.dot(AT, A)
    M = np.linalg.inv(M_inverse)

    xx = M[0][0]
    yy = M[1][1]
    zz = M[2][2]
    tt = M[3][3]

    GDOP[i] = np.sqrt(xx + yy + zz + tt)
    PDOP[i] = np.sqrt(xx + yy + zz)
    HDOP[i] = np.sqrt(xx + yy)
    ZDOP[i] = np.sqrt(zz)
    TDOP[i] = np.sqrt(tt)

    if int(digree[i]) == 0:
        print("GDOP(0)={}".format(GDOP[i]))
        print("PDOP(0)={}".format(PDOP[i]))
        print("HDOP(0)={}".format(HDOP[i]))
        print("ZDOP(0)={}".format(ZDOP[i]))
        print("TDOP(0)={}".format(TDOP[i]))

    if int(digree[i]) == 75:
        print("GDOP(75)={}".format(GDOP[i]))
        print("PDOP(75)={}".format(PDOP[i]))
        print("HDOP(75)={}".format(HDOP[i]))
        print("ZDOP(75)={}".format(ZDOP[i]))
        print("TDOP(75)={}".format(TDOP[i]))

    if int(digree[i]) == 90:
        print("GDOP(90)={}".format(GDOP[i]))
        print("PDOP(90)={}".format(PDOP[i]))
        print("HDOP(90)={}".format(HDOP[i]))
        print("ZDOP(90)={}".format(ZDOP[i]))
        print("TDOP(90)={}".format(TDOP[i]))


# plt.plot(digree, GDOP, label = "GDOP")
# plt.plot(digree, PDOP, label = "PDOP")
# plt.plot(digree, HDOP, label = "HDOP")
# plt.plot(digree, ZDOP, label = "ZDOP")
plt.plot(digree, TDOP, label="TDOP")
plt.xlabel = "degree"
plt.legend()

plt.show()
# plt.savefig("all.png",format='png',dpi=300)
