def analyze_student(
    academic,
    attendance,
    assignments,
    placement
):
    """Identify possible concerns using transparent example rules."""

    values = [academic, attendance, assignments, placement]

    if any(
        not isinstance(x, (int, float))
        or isinstance(x, bool)
        or not 0 <= x <= 100
        for x in values
    ):
        raise ValueError("All indicators must be between 0 and 100.")

    academic_reasons = []
    placement_reasons = []

    if academic < 60:
        academic_reasons.append("Academic score is below 60")

    if attendance < 75:
        academic_reasons.append("Attendance is below 75%")

    if assignments < 60:
        academic_reasons.append("Assignment completion score is below 60")

    if placement < 50:
        placement_reasons.append("Placement readiness score is below 50")

    if academic_reasons:
        academic_status = "Review recommended"
    else:
        academic_status = "No rule-based academic flag"

    if placement_reasons:
        placement_status = "Placement support recommended"
    else:
        placement_status = "No rule-based placement flag"

    return {
        "academic_status": academic_status,
        "academic_reasons": academic_reasons,
        "placement_status": placement_status,
        "placement_reasons": placement_reasons,
    }


if __name__ == "__main__":
    result = analyze_student(
        academic=80,
        attendance=65,
        assignments=70,
        placement=45
    )

    print(result)