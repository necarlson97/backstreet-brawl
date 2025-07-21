from jinja2 import Environment, FileSystemLoader
import os
import glob

from html2image import Html2Image
from pathlib import Path
from PIL import Image

from src.card import Card
from src.anubis import Anubis
from src.all_cards import *  # Loads all cards into Card
from src.loss_cards import *
from src.image_gen import ImageGen

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

print(f"Found: {glob.glob('templates/*.j2')}")
for template_file in glob.glob('templates/*.j2'):
    # Extract the template name without extension
    template_name = os.path.basename(template_file).split('.')[0]
    if template_name.startswith('_'):
        continue
    rendered_html = env.get_template(f'{template_name}.j2').render(
        Card=Card, Anubis=Anubis, ImageGen=ImageGen
    )

    # Write the output to an HTML file
    output_path = Path(f'templates/{template_name}.html')
    output_path.write_text(rendered_html, encoding="utf-8")
    print(f"Rendered {template_name} {rendered_html[200:220]}...")


# Draw all cards as their own PNGs
def card_pngs(card_types, output_dir='templates/card'):
    size = (234, 332)
    scale = 2

    hti = Html2Image(
        output_path=output_dir,
        # Was getting weird cutoff- brute force by rendering with extra height,
        # then just crop out the extra as a post-process
        size=(size[0], size[1] * 2),
        custom_flags=[
            '--disable-gpu',
            '--disable-software-rasterizer',
            '--use-gl=swiftshader',

            f'--force-device-scale-factor={scale}',
        ]
    )
    tpl = env.get_template('_single_card.j2')

    for card_type in card_types:
        print(f"Rendering {card_type}")
        for i in range(card_type.count):

            html = tpl.render(
                cwd=Path.cwd(),
                card_type=card_type, i=i + 1
            )
            name = card_type.name + (f"_{i+1}" if i else "")

            htl_filepath = Path(f"{output_dir}/{name}.html")
            htl_filepath.parent.mkdir(parents=True, exist_ok=True)
            htl_filepath.write_text(html, encoding="utf-8")

            hti.screenshot(
                html_str=html, save_as=f"{name}.png",
            )

            # Crop top portion to desired height
            height = size[1] * scale
            path = Path(f'{output_dir}/{name}.png')
            with Image.open(path) as im:
                cropped = im.crop((0, 0, im.width, height))
                cropped.save(path)

card_pngs(Card.rule_cards(), 'templates/card/rules')
