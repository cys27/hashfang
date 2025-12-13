import argparse

from hashfang.utils import Colors


def get_args():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Hashfang is a lightweight hash identifier and cracker"
    )

    # Define command-line arguments

    ## Target hash
    parser.add_argument("-H", "--hash", help="Target hash value")

    ## Detect type
    parser.add_argument("-d", "--detect", action="store_true", help="Detect hash type")

    ## Crack mode
    parser.add_argument("-c", "--crack", action="store_true", help="Start cracking")

    ## List algorithms
    parser.add_argument(
        "-l", "--list", action="store_true", help="List supported algorithms"
    )

    ## Algorithm name
    parser.add_argument(
        "-a", "--algorithm", default="unknown", help="Hash algorithm name"
    )

    ## Wordlist path
    parser.add_argument("-w", "--wordlist", help="Wordlist file path")

    # Parse the arguments
    args = parser.parse_args()

    # If --list is used, no other argument should be present
    if args.list:
        other_args = any(
            [
                args.hash,
                args.detect,
                args.crack,
                args.algorithm != "unknown",
                args.wordlist,
            ]
        )

        if other_args:
            parser.error(
                f"{Colors.RED}The --list (-l) option must be used alone.{Colors.ENDC}"
            )

        return args

    if not args.hash:
        parser.error(f"{Colors.RED}You must provide a hash value!{Colors.ENDC}")

    if not args.detect and not args.crack:
        parser.error(f"{Colors.RED}No action specified.{Colors.ENDC}")

    if args.detect and args.algorithm != "unknown":
        parser.error(
            f"{Colors.RED}The --detect and --algorithm options cannot be used together.{Colors.ENDC}"
        )

    if args.crack and not args.wordlist:
        parser.error(
            f"{Colors.RED}Cracking requires a wordlist file (-w).{Colors.ENDC}"
        )

    if args.crack and args.algorithm == "unknown" and not args.detect:
        parser.error(
            f"{Colors.RED}Cracking requires a known algorithm. Use --algorithm or --detect.{Colors.ENDC}"
        )

    return args
