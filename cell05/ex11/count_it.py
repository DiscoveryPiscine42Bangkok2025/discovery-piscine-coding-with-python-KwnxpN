import sys

def main():
    """Count arguments and each argument length."""
    if len(sys.argv) < 2:
        print("None.")
        return
    print("parameters:", len(sys.argv) - 1)
    for arg in sys.argv[1:]:
        print(f"{arg}:", len(arg))
main()
