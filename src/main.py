from simulation.generate_dataset import generate_dataset
from logic.collection_rules import analyze_dataset
from logic.visualize_data import visualize_dataset
from logic.report_generator import generate_report

def main():
    print("Starting Subsurface Trash Collector Simulation...\n")

    dataset_path = generate_dataset()
    analyze_dataset(dataset_path)
    visualize_dataset(dataset_path)
    generate_report(dataset_path)

    print("\nSimulation finished successfully.")

if __name__ == "__main__":
    main()