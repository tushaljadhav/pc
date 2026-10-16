"""
Data Science Practicals Runner
Executes all 10 practicals sequentially and reports status.
"""

import os
import sys
import subprocess

tasks = [
    ("Practical 1", "CSV to HORUS Format", "practical_1.py"),
    ("Practical 2", "JSON to HORUS Format", "practical_2.py"),
    ("Practical 3", "XML to HORUS Format", "practical_3.py"),
    ("Practical 4", "Fixers Utilities", "practical_4.py"),
    ("Practical 5", "Averaging of Data", "practical_5.py"),
    ("Practical 6", "Create Sample Dataset", "practical_6.py"),
    ("Practical 7", "Retrieve Attributes of Data", "practical_7.py"),
    ("Practical 8", "Identify and Fix Problematic Column Names", "practical_8.py"),
    ("Practical 9", "Network Routing Diagram", "practical_9.py"),
    ("Practical 10", "Error Management with Pandas", "practical_10.py"),
]

def main():
    print("=" * 65)
    print("  RUNNING ALL DATA SCIENCE PRACTICALS (1 to 10)")
    print("=" * 65)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    env = os.environ.copy()
    env["NO_SHOW"] = "1"

    success_count = 0

    for pid, title, filename in tasks:
        filepath = os.path.join(base_dir, filename)
        print(f"\n>>> Running {pid}: {title} ({filename})...")
        try:
            res = subprocess.run(
                [sys.executable, filepath],
                cwd=base_dir,
                env=env,
                capture_output=True,
                text=True,
                check=True
            )
            print(f"[SUCCESS] {pid} executed cleanly.")
            lines = res.stdout.strip().splitlines()
            for line in lines[:5]:
                print(f"    {line}")
            if len(lines) > 5:
                print(f"    ... [{len(lines) - 5} more lines of output]")
            success_count += 1
        except subprocess.CalledProcessError as e:
            print(f"[FAILED] Error running {filename}:")
            print(e.stderr)

    print("\n" + "=" * 65)
    print(f"  RESULT: {success_count}/{len(tasks)} practicals executed successfully!")
    print("=" * 65)

if __name__ == "__main__":
    main()
