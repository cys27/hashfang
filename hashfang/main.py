from hashfang import banner
from hashfang.cli import get_args
from hashfang.cracker import cracker
from hashfang.identifier import identify
from hashfang.utils import Colors

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
        print(f"{Colors.BLUE}[*] Supported algorithms:{Colors.ENDC}")
        for algo in SUPPORTED_ALGORITHMS:
            print(f"  - {Colors.YELLOW}{algo}{Colors.ENDC}")
        return

    detected_algos = []

    if args.detect:
        possible = identify(args.hash)
        if possible:
            print(f"{Colors.BLUE}[*] Possible algorithm(s):{Colors.ENDC}")
            for algo in possible:
                print(f"  - {Colors.YELLOW}{algo}{Colors.ENDC}")
            detected_algos = possible
        else:
            print(f"{Colors.RED}[-] Could not identify the hash type.{Colors.ENDC}")
            return

    if args.crack:
        if args.algorithm != "unknown":
            algos = [args.algorithm]
        elif detected_algos:
            algos = detected_algos
        else:
            print(
                f"{Colors.RED}[-] No algorithm specified. Use -a or -d to detect.{Colors.ENDC}"
            )
            return
        cracker(args.hash, args.wordlist, algos)


if __name__ == "__main__":
    main()
