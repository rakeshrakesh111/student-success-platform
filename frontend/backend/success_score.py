def calculate_success_score(
    academic,
    attendance,
    assignments,
    placement
):
    """Calculate a weighted Student Success Score out of 100."""

    indicators = [academic, attendance, assignments, placement]

    if any(not isinstance(x, (int, float)) or isinstance(x, bool)
           or not 0 <= x <= 100 for x in indicators):
        raise ValueError("All indicator scores must be between 0 and 100.")

    score = (
        academic * 0.35
        + attendance * 0.25
        + assignments * 0.15
        + placement * 0.25
    )

    return round(score, 2)


def get_success_category(score):
    """Return an initial category for the score."""

    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 80:
        return "Strong indicators"
    elif score >= 60:
        return "Needs monitoring"
    else:
        return "Priority for review"


if __name__ == "__main__":
    score = calculate_success_score(
        academic=80,
        attendance=65,
        assignments=70,
        placement=45
    )

    print("Student Success Score:", score)
    print("Category:", get_success_category(score))