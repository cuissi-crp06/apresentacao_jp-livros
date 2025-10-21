import os

arquivos = ['Grupo_1a.csv', 'Grupo_2a.csv']

for arquivo in arquivos:
    if not os.path.exists(arquivo):
        print(f"⚠️  {arquivo} não encontrado")
        continue

    print(f"\n🔍 Testando {arquivo}...\n")

    # Testar diferentes encodings e mostrar resultado
    encodings = ['cp1252', 'latin-1', 'iso-8859-1', 'cp850']

    for enc in encodings:
        try:
            with open(arquivo, 'rb') as f:
                raw = f.read()

            decoded = raw.decode(enc)

            # Mostrar primeiras linhas
            primeira_linha = decoded.split('\n')[0]
            print(f"{enc:15} → {primeira_linha[:60]}")

        except Exception as e:
            print(f"{enc:15} → ERRO: {e}")

    # Perguntar qual usar
    print(f"\n👆 Qual encoding mostrou os caracteres corretos para {arquivo}?")
    escolha = input("Digite o nome do encoding (ou 'pular'): ").strip()

    if escolha in encodings:
        with open(arquivo, 'rb') as f:
            raw = f.read()

        conteudo = raw.decode(escolha)

        # Backup
        backup = arquivo.replace('.csv', '_original.csv')
        os.rename(arquivo, backup)

        # Salvar UTF-8
        with open(arquivo, 'w', encoding='utf-8', newline='') as f:
            f.write(conteudo)

        print(f"✅ {arquivo} convertido de {escolha} para UTF-8")
        print(f"   Backup: {backup}\n")

print("\n✅ Concluído!")