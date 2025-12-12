# simple hash identifier
# i could have used hashid
import re

# i used ai assistance to generate these regex patterns for identifying hashes.
HASH_PATTERNS = [
    (re.compile(r"^[a-fA-F0-9]{32}$"), ["md5"]),
    (re.compile(r"^[a-fA-F0-9]{40}$"), ["sha1"]),
    (re.compile(r"^[a-fA-F0-9]{56}$"), ["sha224", "sha3-224"]),
    (re.compile(r"^[a-fA-F0-9]{64}$"), ["sha256", "sha3-256", "blake2s"]),
    (re.compile(r"^[a-fA-F0-9]{96}$"), ["sha384", "sha3-384"]),
    (re.compile(r"^[a-fA-F0-9]{128}$"), ["sha512", "sha3-512", "blake2b"]),
    (re.compile(r"^\$2[aby]\$[0-9]{2}\$[A-Za-z0-9./]+$"), ["bcrypt"]),
    (re.compile(r"^\$s0\$.*"), ["scrypt"]),
    (re.compile(r"^pbkdf2:sha(1|224|256|384|512):[0-9]+\$.*"), ["pbkdf2-hmac"]),
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
