"""Audit shared-folder permissions from a CSV for risky grants.

Usage: python3 main.py shares.csv
CSV columns: share,path,principal,access (Read/Change/Full Control)
Flags: HIGH for Everyone Full Control, MEDIUM for Everyone Change or
Authenticated Users Full Control, INFO for any other Full Control grant.
"""
import argparse, csv, sys


def audit_row(row):
    principal, access = row["principal"].strip(), row["access"].strip()
    if principal == "Everyone" and access == "Full Control":
        return "HIGH"
    if (principal == "Everyone" and access == "Change") or \
       (principal == "Authenticated Users" and access == "Full Control"):
        return "MEDIUM"
    if access == "Full Control":
        return "INFO"
    return "OK"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    high = 0
    with open(args.path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            verdict = audit_row(row)
            if verdict == "HIGH":
                high += 1
            print(f"{row['share']} ({row['principal']} {row['access']}): {verdict}")
    print(f"{high} HIGH issue(s).")
    return 1 if high else 0


if __name__ == "__main__":
    sys.exit(main())
