from openai import OpenAI, BadRequestError

retries = 1
p = '''
Black and white manga background lines, radial lines.
Empty center of frame. Asset
Minimal lines.
White background.
'''

"""
Black and white manga portrait of a character.
TODO
Bold lines, anime effects, motion lines.
Character is a human base mesh template, drawing figure.
They are bald, without hair, faceless and featureless.
White background.

Characters are human base mesh templates, drawing figures.
They both are bald, without hair, faceless and featureless.
White background.

Black and white manga of a hand is fist raised vertically.
Another hand enters the scene horizontally,
wrapping itself tightly around the first hand's wrist with a firm, gripping hold.
Bold lines, anime effects, motion lines.
White background.

Black and white manga closeup a fist in a hand.
Fist being squeezed by a separate gripping hand.
Bold lines, anime effects, motion lines.
White background.

For inpainting:
Black and white manga depicting two figures.
One is on their back, pushing on the other with their foot.
MMA, BJJ, wrestling
Bold lines, anime effects, motion lines.
Characters are human base mesh templates, drawing figures.
They both are bald, without hair, faceless and featureless.
White background.
"""

class ImageGen():
    @classmethod
    def list_recent(cls):
        print("Listing")
        try:
            with open('recent_images.txt', 'r') as file:
                urls = file.read().splitlines()
                print(f"Found: {urls}")
        except FileNotFoundError as e:
            print(f"Not found: {e}")
            urls = []

        urls.reverse()
        return urls

    @classmethod
    def gen(cls):
        for i in range(retries):
            client = OpenAI()
            try:
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=p,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )
                print(f"{i+1}/{retries}: {response.data}" )
                image_url = response.data[0].url

                # Append the image URL to the recent_images.txt file
                with open('recent_images.txt', 'a') as file:
                    file.write(image_url + '\n')

            # If it is just a content policy, try again 3 times
            except BadRequestError as e:
                if 'content_policy_violation' not in str(e):
                    raise e
                else:
                    print(f"(skipped) {i+1}/{retries}: {e}")

if __name__ == "__main__":
    ImageGen().gen()
