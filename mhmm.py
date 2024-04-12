from prettytable import PrettyTable
import numpy as np

#-------------------------------------------------------------------------------------------------------------------------------
def forward(A, pi, B, observations):
    M = len(observations)
    N = pi.shape[0]

    alpha = np.zeros((M, N))

    # Initialization
    alpha[0, :] = pi * B[:, observations[0]]

    # Induction
    for t in range(1, M):
        for j in range(N):
            alpha[t, j] = np.sum(alpha[t-1] * A[:, j] * B[j, observations[t]])

    return alpha,np.sum(alpha[M-1,:])

#-------------------------------------------------------------------------------------------------------------------------------
def viterbi(A, pi, B, observations):
    M = len(observations)
    N = pi.shape[0]
    delta = np.zeros((M, N))
    psi = np.zeros((M, N), dtype=int)

    # Initialization
    delta[0] = pi * B[:, observations[0]]
    # Recursion
    for t in range(1, M):
        for j in range(N):
            trans_prob = delta[t - 1] * A[:, j]
            max_trans_prob = np.max(trans_prob)
            psi[t,j] = np.argmax(trans_prob)
            delta[t,j] = max_trans_prob * B[j, observations[t]]

    # Termination
    best_path_prob = np.max(delta[M - 1])
    # Backtrack
    best_path= np.zeros(M,dtype=int)
    best_path[M-1]=np.argmax(delta[M-1])
    for t in range(M-2,-1,-1):
        best_path[t]=psi[t+1,best_path[t+1]]

    return delta,best_path,best_path_prob

#-------------------------------------------------------------------------------------------------------------------------------
def main():
    states = (0, 1)
    observations = [2, 2, 1, 0]

    # Transition Probabilities
    A = np.array([[0.5 ,0.5], [0.4 ,0.6]])
    # Initial Probabilities
    pi = np.array([0.5 ,0.5])
    # Emission Probabilities
    B = np.array([[0.2 ,0.3 ,0.3 ,0.2], [0.3 ,0.2 ,0.2 ,0.3]])
    tab,prob = forward(A, pi, B, observations)
    two_d_list = tab.tolist()
    table = PrettyTable()
    table.field_names = ["Step", "First Value", "Second Value"]
    for i, row in enumerate(two_d_list):
        table.add_row([i+1] + row)
    print('\n---------------------------------------------------------------------------------------')
    print("\t\t\t\tForward Approach ")
    print('---------------------------------------------------------------------------------------')
    print("\n\tProbability table: \n\n", table)
    print("\n\tProbability of observing sequence is: ", prob)
    print('\n---------------------------------------------------------------------------------------')

    #---------------------------------------------------------
    #       If input in log form  just apply np.exp()
    #---------------------------------------------------------
    observations = [2, 2, 1, 0, 1, 3, 2, 0, 0]
    # Transition Probabilities
    A = np.array([[-1,-1], [-1.322 ,-0.737]])
    # Initial Probabilities
    pi = np.array([-1 ,-1])
    # Emission Probabilities
    B = np.array([[-2.322 ,-1.737 ,-1.737 ,-2.322], [-1.737 ,-2.322 ,-2.322 ,-1.737]])
    A = np.exp2(A)
    pi = np.exp2(pi)
    B = np.exp2(B)
    tab,best_path, best_path_prob = viterbi(A, pi, B, observations)
    two_d_list = tab.tolist()
    table = PrettyTable()
    table.field_names = ["Step", "First Value", "Second Value"]
    for i, row in enumerate(two_d_list):
        table.add_row([i+1] + row)
    print('\n---------------------------------------------------------------------------------------')
    print("\t\t\t\tViterbi Method")
    print('---------------------------------------------------------------------------------------')
    print("\n\tProbability Table : \n\n",table)
    print("\n\tThe most probable path is: ", best_path)
    print("\tThe probability of the most probable path is: ", best_path_prob)
    print('\n---------------------------------------------------------------------------------------')


#-------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
