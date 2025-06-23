from google.adk.agent import Agent


root_agent = Agent(
    name="greeting_agent",
    description="A root agent that can handle all the requests",
    model="gemini-2.5-flash-exp",
    description="A greeting agent that can greet the user",
    instructions="You are a greeting agent that can greet the user",
)


root_agent.run("Hello, how are you?")

