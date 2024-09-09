cidade = str(input('Em que cidade você nasceu? '))
cidade_sem_espacos = cidade.strip()

if cidade_sem_espacos.lower().startswith("santo"):
    print(True)
else:
    print(False)