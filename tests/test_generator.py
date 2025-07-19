"""
tests/test_generator.py

Unit tests for the OCOS Post-Quantum Wallet Generator module.
Verifies correctness, integrity, and address consistency.

Run with:
    pytest tests/
"""

import re
from pq_wallet.generator import generate_wallet, verify_address, get_public_key_hash


def test_wallet_structure():
    """Test that generated wallet includes expected keys and formats."""
    wallet = generate_wallet()

    # Check required keys exist
    assert "private_key" in wallet
    assert "public_key" in wallet
    assert "address" in wallet

    # Private key format: hex string, >= 5000 characters (Dilithium3)
    assert isinstance(wallet["private_key"], str)
    assert len(wallet["private_key"]) >= 5000

    # Public key format: hex string, >= 2000 characters
    assert isinstance(wallet["public_key"], str)
    assert len(wallet["public_key"]) >= 2000

    # Address format: starts with 'QOS' and Base58Check string
    assert wallet["address"].startswith("QOS")
    assert re.fullmatch(r'QOS[1-9A-HJ-NP-Za-km-z]{20,}', wallet["address"])


def test_public_key_hash_consistency():
    """Ensure get_public_key_hash() is stable and deterministic."""
    wallet = generate_wallet()
    pubkey_bytes = bytes.fromhex(wallet["public_key"])

    hash1 = get_public_key_hash(pubkey_bytes)
    hash2 = get_public_key_hash(pubkey_bytes)

    assert hash1 == hash2
    assert isinstance(hash1, str)
    assert len(hash1) == 64  # SHA3-256 in hex


def test_address_verification():
    """Verify that address matches public key."""
    wallet = generate_wallet()
    pubkey_bytes = bytes.fromhex(wallet["public_key"])
    address = wallet["address"]

    assert verify_address(pubkey_bytes, address) is True

    # Tampered address should not pass
    tampered = address[:-1] + ("Z" if address[-1] != "Z" else "Y")
    assert verify_address(pubkey_bytes, tampered) is False
