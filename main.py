from bot import QABot

# -------------------------------
# Run Chatbot
# -------------------------------
if __name__ == "__main__":
    bot = QABot()
    print("🤖 Q&A Bot ready! Type 'exit' to quit.\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break
        answer = bot.ask(query)
        print("Bot:", answer)
        print()