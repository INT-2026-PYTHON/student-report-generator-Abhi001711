"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
from .stats import average_per_student, subjects_offered, top_scorer, passing_students

def format_report(records: list[dict]) -> str:
    if not records:
        return "Gradebook Report\nNo records to report."

    total_records = len(records)
    subjects_list = sorted(subjects_offered(records))
    subjects_str = ", ".join(subjects_list)

    averages = average_per_student(records)
    top_name, top_avg = top_scorer(records)
    passers = passing_students(records, threshold=60.0)

    passers_str = ", ".join(passers)

    report = " Gradebook Report: \n"
    report += f"Total records: {total_records}\n"
    report += f"Subjects offered: {subjects_str}\n\n"
    report += "Averages:\n"

    for name in averages.keys():
        report += f"  {name:<7} : {averages[name]}\n"

    report += f"\nTop scorer: {top_name} ({top_avg})\n"
    report += f"Passing students (>= 60.0): {passers_str}"

    return report
