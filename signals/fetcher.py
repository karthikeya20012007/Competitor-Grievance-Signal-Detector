import requests

REDDIT_URLS = [

    "https://www.reddit.com/r/recruiting/new.json?limit=3",

    "https://www.reddit.com/r/cscareerquestions/new.json?limit=3",

    "https://www.reddit.com/r/humanresources/new.json?limit=3",
]


HEADERS = {

    "User-Agent":
        "CompetitorSignalDetector/1.0"
}


def fetch_reddit_posts():

    posts = []

    for url in REDDIT_URLS:

        try:

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=10,
            )

            if response.status_code != 200:

                continue

            data = response.json()

            children = data["data"][
                "children"
            ]

            for child in children:

                post_data = child["data"]

                text = (

                    post_data.get(
                        "title",
                        ""
                    )

                    + " "

                    + post_data.get(
                        "selftext",
                        ""
                    )
                )

                posts.append({

                    "source": "Reddit",

                    "url":
                        "https://reddit.com"
                        + post_data.get(
                            "permalink",
                            ""
                        ),

                    "text": text,
                })


        except Exception as e:

            print(
                f"Fetch error: {e}"
            )

    return posts

seeded_posts = [

    {
        "source": "Reddit",

        "url":
            "https://reddit.com/example1",

        "text":
            (
                "HackerRank has become "
                "extremely slow and candidates "
                "keep complaining about the "
                "experience."
            ),
    },

    {
        "source": "Trustpilot",

        "url":
            "https://trustpilot.com/example2",

        "text":
            (
                "HireVue interviews feel "
                "biased and unreliable "
                "for technical hiring."
            ),
    },

    {
        "source": "Reddit",

        "url":
            "https://reddit.com/example3",

        "text":
            (
                "Codility pricing is too "
                "expensive for small "
                "recruiting teams."
            ),
    },
]