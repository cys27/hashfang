import hashlib
import os

import bcrypt


def encode_general(text, algorithm):
    if not text or not algorithm:
        return ""

    data = text.encode("utf-8")

    try:
        if hasattr(hashlib, algorithm):
            hash = getattr(hashlib, algorithm)(data)

        else:
            hash = hashlib.new(algorithm, data)

        return hash.hexdigest()

    except ValueError:
        return f"Error: '{algorithm}' not supported yet!"


def encode_bcrypt(text, rounds=12):
    data = text.encode("utf-8")
    salt = bcrypt.gensalt(rounds=rounds)
    hashed = bcrypt.hashpw(data, salt)
    return hashed.decode("utf-8")


def encode_pbkdf2(text, salt=None, iterations=260000):
    if salt is None:
        salt = os.urandom(16)

    dk = hashlib.pbkdf2_hmac("sha256", text.encode("utf-8"), salt, iterations)

    return f"pbkdf2:sha256:{iterations}${salt.hex()}${dk.hex()}"


def encode_scrypt(text, salt=None):
    if salt is None:
        salt = os.urandom(16)

    dk = hashlib.scrypt(text.encode("utf-8"), salt=salt, n=16384, r=8, p=1)

    return f"$s0$n=16384,r=8,p=1${salt.hex()}${dk.hex()}"
