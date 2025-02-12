from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Load environment variables
load_dotenv()

# Initialize chat model with GPT-4-0-mini
chat = ChatOpenAI(
    model_name="gpt-4o-mini",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0
)

# Generate response
response = chat.invoke([HumanMessage(content="Write me a song about sparkling water.")])
print(response)
