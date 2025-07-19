#!/usr/bin/env python3
"""
generate_wallet.py
===================

Command-line tool to generate a quantum-safe OCOS wallet using Dilithium3.

Generates:
- Private Key (hex)
- Public Key  (hex)
- OCOS PQ Address (QOS-prefixed, Base58Check)

Author: OCOSToken Team
License: MIT
"""

import argparse
import json
import os
from pq_wallet import generate_wallet


def main():
    parser = argparse.ArgumentParser(
        description="OCOS Post-Quantum Wallet Generator (CRYSTALS-Dilithium3)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Save output to JSON file (wallet.json)",
        default=None
    )
    args = parser.parse_args()

    print("\n🔐  Generating quantum-safe OCOS wallet...\n")
    wallet = generate_wallet()

    print("📬  OCOS PQ Address     : ", wallet["address"])
    print("🔓  Public Key (hex)    : ", wallet["public_key"][:64] + "...")
    print("🔐  Private Key (hex)   : ", wallet["private_key"][:64] + "...\n")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(wallet, f, indent=4)
        print(f"✅  Wallet saved to {os.path.abspath(args.output)}\n")
    else:
        print("ℹ️  Use -o wallet.json to save output to file.\n")


if __name__ == "__main__":
    main()
