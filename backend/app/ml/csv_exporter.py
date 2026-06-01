import csv


def export_dataset(
    rows: list[dict],
    output_file: str,
) -> None:

    if not rows:
        return

    fieldnames = list(
        rows[0].keys()
    )

    with open(
        output_file,
        "w",
        newline="",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()

        writer.writerows(rows)
