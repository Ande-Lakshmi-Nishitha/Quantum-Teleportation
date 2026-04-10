import matplotlib
matplotlib.use('Agg')  # no GUI needed

import matplotlib.pyplot as plt


def plot_results(results):
    noise_levels = [r[0] for r in results]
    avg_fidelity = [r[1] for r in results]

    plt.figure()
    plt.plot(noise_levels, avg_fidelity, marker='o')

    plt.xlabel("Noise Probability (p)")
    plt.ylabel("Average Fidelity")
    plt.title("Quantum Teleportation: Fidelity vs Noise")

    plt.grid()

    plt.savefig("results_plot.png")
    print("Plot saved as results_plot.png")