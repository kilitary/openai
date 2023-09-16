import os
import asyncio
import chronological
from chronological import read_prompt, cleaned_completion
import pprint
from pprint import pprint as p

key = os.getenv('OPENAI_API_KEY')

# you can name this function anything you want, the name "logic" is arbitrary
async def logic():
    # you call the Chronology functions, awaiting the ones that are marked await
    prompt = read_prompt('example_prompt')
    completion = await cleaned_completion(prompt, max_tokens=100, engine="davinci", temperature=0.5, top_p=1, frequency_penalty=0.2, stop=["\n\n"])
    
    print('Completion Response: {0}'.format(completion))

async def main():
    await logic()

# invoke the Chronology main fn to run the async logic
# Create an event loop
loop = asyncio.get_event_loop()

# Schedule the main coroutine to run in the event loop
task = asyncio.ensure_future(logic())

loop.run_until_complete(task)

# Close the event loop
loop.close()
