from graph.graph import app

if __name__ == '__main__':
    print(app.invoke(input={"question" : "What is your name?"}))