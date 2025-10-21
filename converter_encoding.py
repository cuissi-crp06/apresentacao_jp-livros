import os

# Lista de arquivos para converter
arquivos = ['Grupo_1a.csv', 'Grupo_2a.csv']

for arquivo in arquivos:
    if not os.path.exists(arquivo):
        print(f"⚠️  Arquivo {arquivo} não encontrado")
        continue

    # Ler com encoding Windows-1252
    with open(arquivo, 'r', encoding='windows-1252') as f:
        conteudo = f.read()

    # Salvar com UTF-8
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    print(f"✓ {arquivo} convertido para UTF-8")

print("\n✓ Conversão concluída!")