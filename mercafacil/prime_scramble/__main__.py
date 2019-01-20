# pragma: no cover
import sys

from . import main


source = ' '.join(sys.argv[1:])
main(source)
