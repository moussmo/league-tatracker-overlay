class Engine():
    def __init__(self, region):
        self.region = region
        self.default_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "X-Riot-Token": "RGAPI-4b10be2b-f805-4e83-84e4-863a2c96674c"
            }
        
    def get_default_headers(self):
        return self.default_headers
    
    def get_region(self):
        return self.region