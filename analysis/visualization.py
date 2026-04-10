import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt


def plot_results(results_dict):
    plt.figure()

    for noise_type, results in results_dict.items():
        noise_levels = [r[0] for r in results]
        avg_fidelity = [r[1] for r in results]

        plt.plot(noise_levels, avg_fidelity, marker='o', label=noise_type)

    plt.xlabel("Noise Probability (p)")
    plt.ylabel("Average Fidelity")
    plt.title("Quantum Teleportation: Fidelity vs Noise")

    plt.legend()
    plt.grid()

    plt.savefig("results_plot.png")
    print("Plot saved as results_plot.png")