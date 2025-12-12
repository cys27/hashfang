import sys

import bcrypt

from hashfang.cli import get_args
from hashfang.encoders import encode_general, encode_pbkdf2, encode_scrypt
from hashfang.identifier import identify


def read_wordlist(wordlist):
    if not wordlist:
        return []

    entries = []

    try:
        with open(wordlist, "r") as file:
            for line in file:
                word = line.strip()

                if word == "":
                    continue

                if word not in entries:
                    entries.append(word)

    except FileNotFoundError:
        print(f"Error: The file {wordlist} was not found!")

        sys.exit(1)

    except IOError as err:
        print(f"IO error occurred: {err}")

        sys.exit(1)

    return entries


def cracker():
    args = get_args()

    hash = args.hash
    # is_detect_enabled = args.detect
    is_crack_enabled = args.crack
    algorithm = args.algorithm
    wordlist = args.wordlist

    possible_algorithms = []

    if not algorithm == "unknown":
        possible_algorithms.append(algorithm)

    else:
        possible_algorithms = identify(hash)

    if not is_crack_enabled:
        print("[*] Possible algorithm(s):")

        for algo in possible_algorithms:
            print(f"- {algo}")

    else:
        entries = read_wordlist(wordlist)

        if len(entries) == 0:
            print(f"The {wordlist} file is empty!")

            sys.exit(1)

        print(f"\n[*] The attack is starting... ({len(entries)} words)")
        print(f"[*] Possible algorithms: {' / '.join(possible_algorithms)}")

        found = False

        for algo in possible_algorithms:
            print(f"[*] The program is trying the {algo} algorithm")

            for word in entries:
                # the ai wrote the code inside the if statement.
                if algo == "bcrypt":
                    try:
                        if bcrypt.checkpw(word.encode("utf-8"), hash.encode("utf-8")):
                            print(f"\n[+] Password was found: {word}")
                            found = True
                            break

                    except ValueError:
                        continue

                # the ai wrote the code inside the elif statement.
                elif algo == "pbkdf2-hmac":
                    try:
                        header, salt_hex, _ = hash.split("$")
                        _, _, iterations = header.split(":")

                        salt_bytes = bytes.fromhex(salt_hex)
                        iter_int = int(iterations)

                        check_hash = encode_pbkdf2(
                            word, salt=salt_bytes, iterations=iter_int
                        )

                        if check_hash == hash:
                            print(f"\n[+] Password was found: {word}")
                            found = True
                            break

                    except ValueError:
                        continue
                # the ai wrote the code inside the elif statement.
                elif algo == "scrypt":
                    try:
                        parts = hash.split("$")
                        params = parts[2]
                        salt_hex = parts[3]

                        n_val = int(params.split(",")[0].split("=")[1])
                        r_val = int(params.split(",")[1].split("=")[1])
                        p_val = int(params.split(",")[2].split("=")[1])
                        salt_bytes = bytes.fromhex(salt_hex)

                        check_hash = encode_scrypt(
                            word, salt=salt_bytes, n=n_val, r=r_val, p=p_val
                        )

                        if check_hash == hash:
                            print(f"\n[!!!] ŞİFRE BULUNDU: {word}")
                            found = True
                            break
                    except Exception:
                        continue
                else:
                    check_hash = encode_general(word, algo)
                    if check_hash == hash:
                        print(f"\n[+] Password was found: {word}")
                        found = True
                        break

            if found:
                break

        if not found:
            print("\n[-] Password was not found in the wordlist.")
