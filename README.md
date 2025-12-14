# Hashfang

Hashfang is a lightweight hash identifier and cracker written in Python. It is designed to be fast, simple to use, and effective for detecting hash types and performing dictionary attacks.

![Hashfang Demo](images/hashfang_demo.gif)

## Features

- **Hash Identification**: Automatically detect the type of a given hash using pattern matching.
- **Hash Cracking**: Perform dictionary attacks against various hash algorithms.
- **Multiple Algorithm Support**: Supports MD5, SHA family, SHA3 family, BLAKE2, bcrypt, scrypt, and PBKDF2.
- **Simple CLI**: Easy-to-use command-line interface with clear options.

## Installation

### Prerequisites

- Python 3.x

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/cys27/hashfang.git
   cd hashfang
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the setup script to create a global command:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```
   
   This script will:
   - Check for Python 3.
   - Make the script executable.
   - Install dependencies from `requirements.txt`.
   - Create a symbolic link so you can run `hashfang` from anywhere.

### Uninstall

To remove the global `hashfang` command from your system:
```bash
chmod +x uninstall.sh
./uninstall.sh
```

## Usage

```bash
hashfang --help
```

### Arguments

| Argument      | Short | Description                                         | Default                     |
| ------------- | ----- | --------------------------------------------------- | --------------------------- |
| `--hash`      | `-H`  | Target hash value to identify or crack.             | **Required**                |
| `--detect`    | `-d`  | Detect the hash type.                               | `False`                     |
| `--crack`     | `-c`  | Start cracking the hash.                            | `False`                     |
| `--algorithm` | `-a`  | Specify the hash algorithm name.                    | `unknown`                   |
| `--wordlist`  | `-w`  | Wordlist file path for cracking.                    | **Required** (for cracking) |
| `--list`      | `-l`  | List all supported algorithms (must be used alone). | `False`                     |

## Examples

**Detect Hash Type:**
```bash
hashfang -H "5d41402abc4b2a76b9719d911017c592" -d
```

**Crack MD5 Hash with Wordlist:**
```bash
hashfang -H "5d41402abc4b2a76b9719d911017c592" -c -a md5 -w wordlist.txt
```

**Auto-detect and Crack:**
```bash
hashfang -H "5d41402abc4b2a76b9719d911017c592" -d -c -w wordlist.txt
```

**List Supported Algorithms:**
```bash
hashfang -l
```

## Supported Algorithms

| Algorithm   | Type      |
| ----------- | --------- |
| MD5         | Fast hash |
| SHA1        | Fast hash |
| SHA224      | Fast hash |
| SHA256      | Fast hash |
| SHA384      | Fast hash |
| SHA512      | Fast hash |
| SHA3-224    | Fast hash |
| SHA3-256    | Fast hash |
| SHA3-384    | Fast hash |
| SHA3-512    | Fast hash |
| BLAKE2s     | Fast hash |
| BLAKE2b     | Fast hash |
| bcrypt      | Slow hash |
| scrypt      | Slow hash |
| PBKDF2-HMAC | Slow hash |

## Limitations & Roadmap

- **Single-threaded**: Currently, Hashfang performs dictionary attacks sequentially. Multi-threading support is planned for future releases.
- **Memory Usage with Large Wordlists**: Very large wordlists can consume significant amounts of RAM as the file is loaded into memory. Future versions will implement optimized methods such as streaming/chunked file reading to handle large wordlists more efficiently.
- **Limited Hash Patterns**: Hash identification relies on regex patterns and may not detect all hash variants.
- **No Salt Extraction**: For salted hashes (bcrypt, scrypt, PBKDF2), the salt must be embedded in the hash string format.

## License

This project is licensed under the GNU General Public License v3.0 (GPLv3). See the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for authorized password auditing and educational purposes only. Unauthorized use is prohibited. The author is not responsible for any misuse.

---
