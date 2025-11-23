import argparse
from .core import Category
from .chart import create_spend_chart


def main():
    parser = argparse.ArgumentParser(
        description="Budget App — Manage categories and generate spend charts."
    )

    parser.add_argument(
        "--chart",
        nargs="+",
        help="Generate a spend chart for given categories (comma-separated)",
    )

    args = parser.parse_args()

    # Example CLI usage:
    if args.chart:
        names = args.chart
        categories = [Category(name) for name in names]
        print(create_spend_chart(categories))


if __name__ == "__main__":
    main()
