
def adicionar_contato(agenda, nome, telefone, email):
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  agenda.append(contato)
  print(f"\nContato {nome} adicionado com sucesso!")
  return

def visualizar_contatos(agenda):
  print("==========================")
  print("Lista de Contatos")
  print("==========================\n")
  for indice, contato in enumerate(agenda, start=1):
    marcado = "★" if contato["favorito"] else " "
    nomes_contatos = contato["nome"]
    telefones_contatos = contato["telefone"]
    email_contatos = contato["email"]
    print(f"[{marcado}] {indice} - Nome: {nomes_contatos}, Telefone: {telefones_contatos}, E-mail: 1{email_contatos}")
  return

def editar_contato(agenda, indice_contato, novo_dados_nome, novo_dados_telefone, novo_dados_email):
  #Selecionando o contato que desejo alterar
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >=0 and indice_contato_ajustado < len(agenda):
    agenda[indice_contato_ajustado]["nome"] = novo_dados_nome
    agenda[indice_contato_ajustado]["telefone"] = novo_dados_telefone
    agenda[indice_contato_ajustado]["email"] = novo_dados_email
    print(f"Cadastro {indice_contato} atualizado com sucesso!")
  else:
    print("Opção invalida!")
    return

def marcar_contato(agenda, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
    agenda[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} marcado como favorito!")
  else:
    print("Opção invalida!")
  return

def desmarcar_contato(agenda, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
    agenda[indice_contato_ajustado]["favorito"] = False
    print(f"Contato {indice_contato} desmarcado como favorito!")
  else:
    print("Opção invalida!")
  return

def visualizar_contatos_favoritos(agenda):
  print("==========================")
  print("Lista de Contatos Favoritos")
  print("==========================\n")
  contatos_favoritos = [contato for contato in agenda if contato.get("favorito") == True]
  if contatos_favoritos:
    for indice, contato in enumerate(contatos_favoritos, start=1):
      contato_favorito = "★" if contato["favorito"] else ""
      nomes_contatos = contato["nome"]
      telefones_contatos = contato["telefone"]
      email_contatos = contato["email"]
      print(f"[{contato_favorito}] {indice} - Nome: {nomes_contatos}, Telefone: {telefones_contatos}, "
            f"E-mail: 1{email_contatos}")
  else:
    print("Não existe contatos favoritos!")
    return

def apagar_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        del agenda[indice_contato_ajustado]
        print(f"Contato {indice_contato} removido com sucesso!")
    else:
        print("Opção invalida!")
    return

agenda = []

while True:
  print("==========================")
  print("Menu de Agenda de Contatos")
  print("==========================\n")
  print("1. Adicionar Contato")
  print("2. Visualizar Contato")
  print("3. Editar um Contato")
  print("4. Marcar um contato como Favorito")
  print("5. Desmarcar um contato como Favorito")
  print("6. Ver Lista de Contatos Favoritos")
  print("7. Apagar um Contato")
  print("8. Sair\n")

  escolha = input("Digite a opção que deseja: ")

  if escolha == "1":
    nome = input("\nDigite o nome do contato que deseja adicionar: ")
    telefone = input("\nDigite o número do telefone: ")
    email = input("\nDigite o email do contato: ")
    favorito = False
    adicionar_contato(agenda, nome, telefone, email)

  elif escolha == "2":
    visualizar_contatos(agenda)

  elif escolha == "3":
    visualizar_contatos(agenda)
    indice_contato = input("Verifique a lista acima e digite o código do contato que deseja alterar: ")
    novo_dados_nome = input("Digite um novo nome para o contato: ")
    novo_dados_telefone = input("Digite um novo telefone para o contato: ")
    novo_dados_email = input("Digite um novo email para o contato: ")
    editar_contato(agenda, indice_contato, novo_dados_nome, novo_dados_telefone, novo_dados_email)

  elif escolha == "4":
    visualizar_contatos(agenda)
    indice_contato = input("Digite o número do contato que deseja marcar como favorito: ")
    marcar_contato(agenda, indice_contato)

  elif escolha == "5":
    visualizar_contatos(agenda)
    indice_contato = input("Digite o número do contato que deseja desmarcar dos favoritos: ")
    desmarcar_contato(agenda, indice_contato)

  elif escolha == "6":
    visualizar_contatos_favoritos(agenda)

  elif escolha == "7":
    visualizar_contatos(agenda)
    indice_contato = input("Qual contato você deseja excluir da lista acima? ")
    apagar_contato(agenda, indice_contato)

  elif escolha == "8":
    break