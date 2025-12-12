from hashfang import banner
from hashfang.cli import get_args
from hashfang.cracker import cracker
from hashfang.identifier import identify

# Supported algorithms list
SUPPORTED_ALGORITHMS = [
    "md5",
    "sha1",
    "sha224",
    "sha256",
    "sha384",
    "sha512",
    "sha3-224",
    "sha3-256",
    "sha3-384",
    "sha3-512",
    "blake2s",
    "blake2b",
    "bcrypt",
    "scrypt",
    "pbkdf2-hmac",
]


def main():
    print(banner)

    args = get_args()

    # list supported algorithms
    if args.list:
        print("[*] Supported algorithms:")
        for algo in SUPPORTED_ALGORITHMS:
            print(f"  - {algo}")
        return

    if args.detect:
        possible = identify(args.hash)
        if possible:
            print("[*] Possible algorithm(s):")
            for algo in possible:
                print(f"  - {algo}")
        else:
            print("[-] Could not identify the hash type.")
        return

    if args.crack:
        cracker()


if __name__ == "__main__":
    main()