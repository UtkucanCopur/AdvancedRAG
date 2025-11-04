from graph.graph import app
from dotenv import load_dotenv


"""---TO RUN THIS SCRIPT---"""


load_dotenv()

if __name__ == '__main__':
    print(app.invoke(input={"question": "how can i make hamburgers?"}))