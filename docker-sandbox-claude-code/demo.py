import asyncio
import os
import sys
from pathlib import Path

import cognee

DATASET = "agent_sessions"

SAMPLE_PREFERENCES = """\
User travel preferences:
- Likes to visit places near the beach where they can find the best spots.
- Wants locations that are rare to find on blogs — goldmine, off-the-beaten-path places.
- Prefers vegetarian meals; use this for any restaurant recommendation.
- Hobbies that help with itinerary planning: Anime, F1, and Cricket.
"""

ITINERARY_QUERY = "Plan a one-day itinerary for Rome, including restaurants to try."


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


async def connect() -> None:
    await cognee.serve(
        url=os.environ["COGNEE_BASE_URL"],
        api_key=os.environ["COGNEE_API_KEY"],
    )


async def remember() -> None:
    await cognee.remember(SAMPLE_PREFERENCES, dataset_name=DATASET)
    print("Stored sample preferences in Cognee Cloud.")


async def recall(query: str) -> None:
    results = await cognee.recall(query, datasets=[DATASET])
    for result in results:
        print(result)


async def main(mode: str, query: str) -> None:
    await connect()
    if mode in ("remember", "both"):
        await remember()
    if mode in ("recall", "both"):
        await recall(query)
    await cognee.disconnect()


if __name__ == "__main__":
    load_dotenv(Path(__file__).parent / ".env")
    for var in ("COGNEE_BASE_URL", "COGNEE_API_KEY"):
        if not os.environ.get(var):
            sys.exit(f"Missing required environment variable: {var}")

    mode = sys.argv[1] if len(sys.argv) > 1 else "both"
    if mode not in ("remember", "recall", "both"):
        sys.exit("Usage: python demo.py [remember|recall|both] [\"query\"]")
    query = sys.argv[2] if len(sys.argv) > 2 else ITINERARY_QUERY
    asyncio.run(main(mode, query))
