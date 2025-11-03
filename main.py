from graph.graph import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    print(app.invoke(input={"question" : "What is prompt engineering?"}))