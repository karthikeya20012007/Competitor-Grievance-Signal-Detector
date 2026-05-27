from utils.keywords import (
    COMPETITORS,
    NEGATIVE_KEYWORDS,
)


WINDOW_SIZE = 6


def detect_signals(text):

    lowered_text = text.lower()

    words = lowered_text.split()

    detected_competitors = []

    detected_categories = []

    matched_keywords = []

    contextual_matches = 0

    for competitor in COMPETITORS:

        competitor_lower = (
            competitor.lower()
        )

        for index, word in enumerate(words):

            if competitor_lower in word:

                detected_competitors.append(
                    competitor
                )

                matched_keywords.append(
                    competitor
                )

                start = max(
                    0,
                    index - WINDOW_SIZE
                )

                end = min(
                    len(words),
                    index + WINDOW_SIZE
                )

                nearby_words = words[start:end]

                for (
                    category,
                    keywords
                ) in NEGATIVE_KEYWORDS.items():

                    for keyword in keywords:

                        keyword_lower = (
                            keyword.lower()
                        )

                        if keyword_lower in (
                            " ".join(
                                nearby_words
                            )
                        ):

                            detected_categories.append(
                                category
                            )

                            matched_keywords.append(
                                keyword
                            )

                            contextual_matches += 1

    return {

        "competitors": list(
            set(detected_competitors)
        ),

        "pain_categories": list(
            set(detected_categories)
        ),

        "matched_keywords": list(
            set(matched_keywords)
        ),

        "contextual_matches":
            contextual_matches,
    }