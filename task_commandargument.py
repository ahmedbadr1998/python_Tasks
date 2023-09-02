
import sys

# Get the list of command-line arguments (excluding the script name)
arguments = sys.argv[1:]

# Print the command-line arguments
print("Command-line arguments:")
if len(arguments) > 1:
    kin = arguments[0]
    if kin == "100":
        print("pop")
    v = arguments[2]
    if v == "40":
        print("koko")
    k = arguments[3]
    if k == "40":
        print("nono")
