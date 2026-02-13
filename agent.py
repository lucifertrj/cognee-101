import asyncio,os
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from cognee_integration_google_adk import add_tool, search_tool

from dotenv import load_dotenv
load_dotenv()

os.environ['LLM_PROVIDER'] = "openai"

MY_PREFERENCE = """
- I like to visit places near the beach where I can find the best spots. 
- I need locations that are rare to find on blogs but are goldmine places for your eyes
- I prefer Vegetarian meals. Use this when I ask for restaurants recommendation
- I am a Jain so plan accordingly. Garlic and Onions works. But No eggs and Mushrooms. 
- For hotel recommendations if I ask: I prefer private bathrooms and minimum 8+ reviews on booking.com and more than 4+ ratings on Google Maps 
- My hobbies that might also help in planning Itineraries: I love Anime, F1 and Cricket.
- About me: I am Tarun Jain, AI & Founding Engineer with a YouTube channel: AI with Tarun
"""

INSTRUCTIONS = """
You are a travel planning agent. When the user asks for recommendations:
1. Search memory for relevant user preferences
2. Extract and apply those preferences to filter all results
3. When retrieving cached recommendations from memory, re-validate against preferences
4. Present only options that match ALL preference criteria
5. If preferences conflict with available options, explain why and suggest alternatives
"""

async def main():
    agent = Agent(
        model="gemini-2.5-flash",
        name="executive_assistant",
        description="You are a Personal Executive Assistant who remembers my preference to plan my itinerary accordingly",
        instruction=INSTRUCTIONS,
        tools=[add_tool, search_tool],
    )

    runner = InMemoryRunner(agent=agent)

    await runner.run_debug(f"Remember: {MY_PREFERENCE}")
    query = "plan 3 days Itinerary for Rome along with restaurants to try food."
    events = await runner.run_debug(query)

    for event in events:
        if event.is_final_response() and event.content:
            for part in event.content.parts:
                if part.text:
                    print(part.text)

if __name__ == "__main__":
    asyncio.run(main())