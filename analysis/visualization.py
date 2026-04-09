import matplotlib.pyplot as plt

def plot_results(results):
    noise_levels=[r[0] for r in results]
    fidelity=[r[1] for r in results]

    plt.figure()
    plt.plot(noise_levels,fidelity,marker='o')

    plt.xlabel("Noise probability (p)")
    plt.ylabel("Average fidelity")

    plt.title("Quantum Teleportation: Fidelity vs Noise")

    plt.grid()
    plt.savefig("results_plot.png")
    plt.show()
    