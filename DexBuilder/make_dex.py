import seribii_main, combine


def main():
    # Process raw text
    seribii_main.compile_raw()

    # Add all other information
    combine.add_all()
    return


if __name__ == "__main__":
    main()