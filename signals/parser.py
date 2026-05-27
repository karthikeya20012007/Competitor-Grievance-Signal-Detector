from datetime import datetime


def build_signal_record(
    post,
    detection_result,
    signal_score,
):

    competitors = detection_result[
    "competitors"
]

    categories = detection_result[
        "pain_categories"
    ]

    reason = (
        f"Detected complaints related to "
        f"{', '.join(competitors)} "
        f"with pain points in "
        f"{', '.join(categories)}."
    )

    return {

        "company": (
            detection_result[
                "competitors"
            ][0]

            if detection_result[
                "competitors"
            ]

            else "Unknown"
        ),

        "signal_type":
            "competitor_grievance",

        "source_url":
            post["url"],

        "matched_keywords":
            detection_result[
                "matched_keywords"
            ],

        "pain_categories":
            detection_result[
                "pain_categories"
            ],

        "signal_score":
            signal_score,

        "detected_at":
            datetime.utcnow().isoformat(),

        "reason":
            reason,
    }