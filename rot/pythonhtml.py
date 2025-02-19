from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Define the template
template = env.get_template('template.html')

# Define the data to be passed to the template
data = {
    'title': 'Intro til HTML og CSS',
    'header': 'Velkommen til Kodehode',
    'article_title': 'Kakapo',
    'image_src': './assets/fugl.jpg',
    'image_alt': 'Bilde av fugl',
    'paragraph': (
        'This is a big kakapo Bird. The kakapo, also known as the owl parrot,\n'
        'is a species of large, flightless, nocturnal parrot endemic to New Zealand.\n'
        'It is critically endangered, with only about 200 individuals remaining.\n'
        'The kakapo is known for its distinctive, musky odor and its unique mating call,\n'
        'which can be heard up to 5 kilometers away. Despite its inability to fly,\n'
        'the kakapo is an excellent climber and uses its wings for balance and to break its fall when leaping from trees.'
    )
}

# Render the template with the data
output = template.render(data)

# Write the output to an HTML file
with open('output.html', 'w') as f:
    f.write(output)