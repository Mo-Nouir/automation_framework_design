import subprocess
import sys
import os

# --- Config ---
FEATURE = "features/transfer_money.feature"  # path to your feature
PARALLEL = False                             # True for parallel
PROCESSES = 4                                # only used if parallel
REPORT_DIR = "reports/allure"

# make sure report dir exists
os.makedirs(REPORT_DIR, exist_ok=True)

# --- Build command ---
if PARALLEL:
    cmd = [
        "behave-parallel",
        "--processes", str(PROCESSES),
        "--format", "allure_behave.formatter:AllureFormatter",
        "--outfile", REPORT_DIR,
        FEATURE
    ]
else:
    cmd = [
        "behave",
        FEATURE,
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", REPORT_DIR
    ]

# --- Run tests ---
print("Running:", " ".join(cmd))
subprocess.run(cmd, check=True)

print(f"Tests finished! Allure results in {REPORT_DIR}")
print(f"Generate report with: allure serve {REPORT_DIR}")
