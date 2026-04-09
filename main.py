from experiments.run_experiments import run
from analysis.visualization import plot_results

if __name__ == "__main__":
    results=run()
    plot_results(results)