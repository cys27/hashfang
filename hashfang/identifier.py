# simple hash identifier
# i could have used hashid
import re

# i used ai assistance to generate these regex patterns for identifying hashes.
HASH_PATTERNS = [
    (re.compile(r"^[a-fA-F0-9]{32}$"), ["MD5"]),
    (re.compile(r"^[a-fA-F0-9]{40}$"), ["SHA1"]),
    (re.compile(r"^[a-fA-F0-9]{56}$"), ["SHA224", "SHA3-224"]),
    (re.compile(r"^[a-fA-F0-9]{64}$"), ["SHA256", "SHA3-256", "BLAKE2s"]),
    (re.compile(r"^[a-fA-F0-9]{96}$"), ["SHA384", "SHA3-384"]),
    (re.compile(r"^[a-fA-F0-9]{128}$"), ["SHA512", "SHA3-512", "BLAKE2b"]),
    (re.compile(r"^\$2[aby]\$[0-9]{2}\$[A-Za-z0-9./]+$"), ["bcrypt"]),
    (re.compile(r"^\$s0\$.*"), ["scrypt"]),
    (re.compile(r"^pbkdf2:sha(1|224|256|384|512):[0-9]+\$.*"), ["PBKDF2-HMAC"]),
]


def identify(hash):
    if not hash:
        return []

    hash = hash.strip()
    matches = []

    for pattern, algorithms in HASH_PATTERNS:
        if pattern.fullmatch(hash):
            matches.extend(algorithms)

    return matches
