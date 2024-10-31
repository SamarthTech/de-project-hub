class MarkdownConverter:
    def convert(self, markdown):
        html = markdown.replace("**", "<b>").replace("__", "<b>")
        html = html.replace("*", "<i>").replace("_", "<i>")
        return html.replace("\n", "<br>")

def main():
    converter = MarkdownConverter()
    print("Enter Markdown text (type 'quit' to exit):")
    while True:
        markdown = input()
        if markdown.lower() == "quit":
            break
        html = converter.convert(markdown)
        print("Converted HTML:\n", html)

if __name__ == "__main__":
    main()
