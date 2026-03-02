import csv

def analyze_dataset(file_path):
    """
    Reads the trash dataset and prints basic statistics.
    """

    total_items = 0
    total_depth = 0
    trash_type_counts = {}
    collected_count = 0

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_items += 1
            total_depth += int(row["depth_cm"])

            trash_type = row["trash_type"]
            trash_type_counts[trash_type] = trash_type_counts.get(trash_type, 0) + 1

            if row["collected"] == "yes":
                collected_count += 1

    average_depth = total_depth / total_items if total_items > 0 else 0

    print("\n DATASET STATISTICS")
    print("--------------------")
    print(f"Total trash items detected: {total_items}")
    print(f"Average depth (cm): {average_depth:.2f}")
    print(f"Items collected: {collected_count}")
    print("Trash type distribution:")

    for trash_type, count in trash_type_counts.items():
        print(f"  - {trash_type}: {count}")