import csv
import os

OUTPUT_DIR = "data/processed"
REPORT_FILE = "summary_report.txt"

def generate_report(file_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total_items = 0
    total_depth = 0
    collected = 0

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_items += 1
            total_depth += int(row["depth_cm"])
            if row["collected"] == "yes":
                collected += 1

    avg_depth = total_depth / total_items if total_items else 0
    collection_rate = (collected / total_items) * 100 if total_items else 0

    report_path = os.path.join(OUTPUT_DIR, REPORT_FILE)

    with open(report_path, "w") as report:
        report.write("SUBSURFACE TRASH COLLECTOR REPORT\n")
        report.write("--------------------------------\n")
        report.write(f"Total trash items: {total_items}\n")
        report.write(f"Average depth (cm): {avg_depth:.2f}\n")
        report.write(f"Collected items: {collected}\n")
        report.write(f"Collection rate: {collection_rate:.2f}%\n\n")
        report.write("Generated files:\n")
        report.write("- trash_type_distribution.png\n")
        report.write("- trash_depth_distribution.png\n")

    print("\n📝 Summary report generated.")