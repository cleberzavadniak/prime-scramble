import sys
import os.path

from .decrypt import decrypt


def main(source=None):
    if not source:
        basename = os.path.basename(sys.argv[0])
        print(f"Usage: {basename} <string to be decrypted>")
        sys.exit(1)

    print(decrypt(source))
