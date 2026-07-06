import sys
from converters.engine import convert


def main():
    if len(sys.argv) < 2:
        print("❌ Usage: python main.py <file_path>")
        return

    file_path = sys.argv[1]

    try:
        output = convert(file_path)
        print(f"\n✅ Done!\nPDF saved at:\n{output}")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()