from jinja2 import Environment, FileSystemLoader
import os
import glob

from src.card import Card

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

for template_file in glob.glob('templates/*.j2'):
    # Extract the template name without extension
    template_name = os.path.basename(template_file).split('.')[0]
    rendered_html = env.get_template(f'{template_name}.j2').render(
        Card=Card,
    )

    # Write the output to an HTML file
    with open(f'templates/{template_name}.html', 'w') as file:
        print(f"Rendered {template_name} {rendered_html[200:220]}...")
        file.write(rendered_html)
