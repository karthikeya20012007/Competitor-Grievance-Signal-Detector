import json

from signals.fetcher import (
    seeded_posts,
)

from signals.detector import (
    detect_signals
)

from signals.scorer import (
    calculate_signal_score
)

from signals.parser import (
    build_signal_record
)


def run_pipeline():

    all_signals = []

    posts = seeded_posts

    for post in posts:

        detection_result = (
            detect_signals(
                post["text"]
            )
        )

        signal_score = (
            calculate_signal_score(
                detection_result
            )
        )

        if signal_score < 40:

            continue

        signal_record = (
            build_signal_record(
                post,
                detection_result,
                signal_score,
            )
        )

        all_signals.append(
            signal_record
        )

    return all_signals


def detect_signals_handler(
    event,
    context,
):

    signals = run_pipeline()

    return {
        "statusCode": 200,

        "headers": {
            "Content-Type":
                "application/json"
        },

        "body": json.dumps(
            signals
        ),
    }


if __name__ == "__main__":

    results = run_pipeline()

    print(
        json.dumps(
            results,
            indent=4
        )
    )