import asyncio
from constant import MY_PREFERENCE
import cognee
from cognee.api.v1.visualize.visualize import visualize_graph

from dotenv import load_dotenv
load_dotenv()

async def main():
    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)

    await cognee.add(MY_PREFERENCE) # Used for grouping related data points in the knowledge graph.
    # await cognee.add(MY_PREFERENCE,node_set="personal_tarun")
    # await cognee.add("- In Food I usually prefer Thali and Indian Vegetarian food places",node_set=["food"])

    await cognee.cognify()
    await visualize_graph("./graph_after_cognify.html")
    await cognee.memify() # enhance the knowledge graph with memory consolidation for improved connections
    
    results = await cognee.search("plan 3 days Itinerary for Hong Kong",query_type=cognee.SearchType.GRAPH_COMPLETION,)
    for result in results:
        print(result) 

if __name__ == '__main__':
    asyncio.run(main())