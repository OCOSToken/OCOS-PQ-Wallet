"""
pq_wallet
=========

A secure post-quantum wallet module for OCOS ecosystem,
powered by NIST-approved CRYSTALS-Dilithium3 lattice-based signature algorithm.

This module provides:
- Quantum-resistant keypair generation
- Public key-based OCOS address derivation
- Secure export interfaces

Usage Example:
--------------
from pq_wallet import generate_wallet

wallet = generate_wallet()
print(wallet["address"])

"""

from .generator import generate_wallet, verify_address, get_public_key_hash

__all__ = [
    "generate_wallet",
    "verify_address",
    "get_public_key_hash"
]
