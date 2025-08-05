class TextReply:
    def respond(self):
        return "Text: Hello"

class ImageReply:
    def respond(self):
        return "Image: 📷"

messages = [TextReply(), ImageReply()]

for m in messages:
    print(m.respond())
