class HTML:
    def __init__(self, tag, content):
        self.tag = tag
        self.content = content

    def make_web_page(self):
        return f"<{self.tag}>{self.content}</{self.tag}>"
    
class CSS:
    def __init__(self, content):
        self.css_content = content

    def style_format(self):
        return f"<style>{self.css_content}</style>"

class full_website(HTML, CSS):
    def __init__(self, tag, content, css_content):
        self.tag = tag
        self.content = content
        self.css_content = css_content

    def make_full_website(self):
        return f"{self.make_web_page()}\n{self.style_format()}"
    
class js(full_website):
    def __init__(self, tag, content, css_content, js_content):
        full_website.__init__(self, tag, content, css_content)
        self.js_content = js_content

    def make_full_website(self):
        return f"{super().make_full_website()}\n<script>{self.js_content}</script>"

js_instance = js("h1", "Hello World", "body {background-color: lightblue;}", "console.log('Hello World');")
print(js_instance.make_full_website())