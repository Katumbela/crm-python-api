import facebook_scraper as fs

# Obtém um objeto gerador de posts
gen = fs.get_posts('facebook', page=50, options={"progress": True})

# Itera sobre o objeto gerador para imprimir os posts
for post in gen:
    print(post['text'][:50])  # Imprime os primeiros 50 caracteres do texto do post
