import webview

class Display:
    """Set up a live display"""
    def __init__(self, cluster):
        self.cluster = cluster

    def start(self):
        webview.create_window('UI', 'https://example.com/')
        webview.start()
        print("Not implemented")

    def update(self, bodies):
        print("Not implemented")