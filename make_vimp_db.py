import os
import re
import subprocess
from pathlib import Path
from itertools import chain

trivy_path = Path("trivy")
snyk_path = Path("snyk")
grype_path = Path("grype")

report_paths = chain(trivy_path.glob("*.json"), snyk_path.glob("*.json"), grype_path.glob("*.json"))

cve_regex = re.compile("CVE-\d+-\d+")

all_images = set()
image_vuln_with_scanners = {}
for report_path in report_paths:
    scanner_name = report_path.parent.name
    image_name = report_path.name.split("/", 1)[-1].split(".")[0].split("-", 1)[-1]
    all_images.add(image_name)
    with open(report_path) as f:
        report = f.read()
        cves = set(cve_regex.findall(report))

        for cve in cves:
            key = (image_name, cve)
            if key not in image_vuln_with_scanners:
                image_vuln_with_scanners[key] = [scanner_name]
            else:
                image_vuln_with_scanners[key].append(scanner_name)


with open("final_output.csv", "w") as f:
    f.write("image_name,cve,scanners\n")
    for image_vuln, scanners in image_vuln_with_scanners.copy().items():
        scanners = "+".join(sorted(scanners))
        f.write(f"{image_vuln[0]},{image_vuln[1]},{scanners}\n")

