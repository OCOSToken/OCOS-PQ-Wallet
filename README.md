# OCOS Post-Quantum Wallet Generator

**A quantum-safe wallet, keypair, and address generator for OCOS, based on the NIST-approved CRYSTALS-Dilithium3 post-quantum digital signature scheme.**

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Security Considerations](#security-considerations)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)
- [Disclaimer](#disclaimer)

---

## Introduction

The **OCOS Post-Quantum Wallet Generator** is an open-source Python toolkit for generating **quantum-resistant cryptographic wallets, keys, and addresses** for the OCOS ecosystem. It uses the NIST-standardized [CRYSTALS-Dilithium3](https://csrc.nist.gov/projects/post-quantum-cryptography/selected-algorithms-2022) digital signature algorithm, providing industry-grade security against both classical and quantum attacks.

This project aims to prepare OCOS and its users for the quantum era, ensuring the long-term safety and integrity of digital assets.

---

## Features

- **Quantum-Safe Cryptography:** Uses CRYSTALS-Dilithium3 (lattice-based, NIST PQC standard).
- **Keypair Generation:** Creates strong, quantum-resistant private and public keys.
- **OCOS Address Derivation:** Generates a unique, collision-resistant address (QOS-prefixed, SHA3-256, Base58Check).
- **Modular Codebase:** Easy integration into OCOS services or other blockchain projects.
- **Open Source:** Fully auditable and MIT-licensed.
- **Test Coverage:** Includes minimal test suite for validation.

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OCOSToken/OCOS-PQ-Wallet.git
   cd OCOS-PQ-Wallet
   ```

2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** Requires Python 3.7 or higher.

---

## Usage

To generate a new OCOS quantum-safe wallet, run:

```bash
python scripts/generate_wallet.py
```

Example output:

```
OCOS PQ Private Key:  <long hex string>
OCOS PQ Public Key :  <long hex string>
OCOS PQ Address    :  QOS3ur98jqwl... (Base58Check)
```

- **Keep your private key safe and offline!**
- **Your address (QOS...) is your public identifier.**

---

## How It Works

- The core module uses **Dilithium3** to generate a secure keypair.
- The public key is hashed using **SHA3-256** and encoded as a 20-byte address with Base58Check (same as BTC/ETH style).
- The resulting OCOS address starts with the **QOS** prefix, ensuring uniqueness for the OCOS post-quantum standard.

#### Code Example

```python
from pq_wallet.generator import generate_wallet

wallet = generate_wallet()
print(wallet["private_key"])
print(wallet["public_key"])
print(wallet["address"])
```

---

## Security Considerations

- **Private keys are sensitive!** Never share, upload, or expose your private key.
- **Backup:** Store the private key in multiple, secure offline locations.
- **This tool performs all cryptography locally; no keys are sent over the internet.**
- Consider using hardware security modules (HSMs) or air-gapped devices for real-world deployments.

---

## Project Structure

```
OCOS-PQ-Wallet/
├── README.md
├── LICENSE
├── requirements.txt
├── pq_wallet/
│   ├── __init__.py
│   └── generator.py
├── scripts/
│   └── generate_wallet.py
└── tests/
    └── test_generator.py
```

- **pq_wallet/** – Core cryptographic logic (wallet generator).
- **scripts/** – Example CLI tools.
- **tests/** – Minimal automated tests.

---

## Contributing

Contributions, bug reports, and suggestions are welcome! Please open an issue or submit a pull request.

1. Fork the repo and create your branch.
2. Write clear commit messages and document all changes.
3. Run tests before submitting a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## References

- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [CRYSTALS-Dilithium](https://pq-crystals.org/dilithium/)
- [pqcrypto Python Library](https://github.com/sourcehold/pqcrypto)
- [Base58Check Encoding](https://en.bitcoin.it/wiki/Base58Check_encoding)

---

## Disclaimer

This software is provided **as-is** for research, development, and professional infrastructure integration.  
No warranty is given. Always perform independent code and security audits before using in production or storing significant assets.

---
