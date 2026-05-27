def calculate_signal_score(
    detection_result
):

    score = 0

    competitors = detection_result[
        "competitors"
    ]

    pain_categories = detection_result[
        "pain_categories"
    ]

    matched_keywords = detection_result[
        "matched_keywords"
    ]

    contextual_matches = detection_result[
        "contextual_matches"
    ]

    if competitors:

        score += 30

    score += (
        len(pain_categories) * 15
    )

    score += (
        contextual_matches * 15
    )

    score += (
        len(matched_keywords) * 3
    )

    if len(pain_categories) >= 2:

        score += 10

    if contextual_matches == 0:

        score -= 20

    if score < 0:

        score = 0

    if score > 100:

        score = 100

    return score