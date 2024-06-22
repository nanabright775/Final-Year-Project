import cohere

class CohereAPI:
    API_KEY = "f0pyvRCiqEXSiCwoceTpjHDbEnlItSb6dCNJ5Tr2"
    MODEL = "command-xlarge-nightly"

    @staticmethod
    def generate_content(prompt):
        co = cohere.Client(CohereAPI.API_KEY)
        response = co.generate(
            model=CohereAPI.MODEL,
            prompt=prompt,
            max_tokens=500,
            temperature=0.7,
        )
        return response.generations[0].text.strip()
