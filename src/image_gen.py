from openai import OpenAI


p = '''
Black and white manga portrait of a fearful character.
A hand reaches out, and grabs their hair.
They are wincing, angry.
Bold lines, anime effects, motion lines.
Character is a human base mesh template, drawing figure.
They are bald, without hair, faceless and featureless.
White background.
'''

"""
Black and white manga portrait of a character.
TODO
They are terrified.
Bold lines, anime effects, motion lines.
Character is a human base mesh template, drawing figure. They are bald, without hair, faceless and featureless.
White background.

Characters are human base mesh templates, drawing figures.
They both are bald, without hair.
White background.
"""
retries = 3
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
                print(response.data)
            # If it is just a content policy, try again 3 times
            except openai.BadRequestError as e:
                if 'content_policy_violation' not in str(e):
                    raise e
                else:
                    print(f"Continuing {i}/{retries}: {e}")

            image_url = response.data[0].url

            # Append the image URL to the recent_images.txt file
            with open('recent_images.txt', 'a') as file:
                file.write(image_url + '\n')

            return image_url


if __name__ == "__main__":
    ImageGen().gen()
