import sys
with open('src/components/Catalogue.astro', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(' <code class=\"font-mono\"></code>', ' <code class=\"font-mono\">SKU: </code>')

with open('src/components/Catalogue.astro', 'w', encoding='utf-8') as f:
    f.write(text)
