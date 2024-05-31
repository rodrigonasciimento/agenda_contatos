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
    nomes_contatos = contato["nome"]
    telefones_contatos = contato["telefone"]
    email_contatos = contato["email"]
    print(f"{indice} - Nome: {nomes_contatos}, Telefone: {telefones_contatos}, E-mail: 1{email_contatos}")
  return

def editar_contato(agenda, novo_dados_nome, novo_dados_telefone, novo_dados_email):
  #Selecionando o contato que desejo alterar
    contato = agenda
    contato["nome"] = novo_dados_nome
    contato["telefone"] = novo_dados_telefone
    contato["email"] = novo_dados_email
    print(f"Cadastro atualizado com sucesso!")
    return
  

agenda = []
while True:
  print("==========================")
  print("Menu de Agenda de Contatos")
  print("==========================\n")
  print("1. Adicionar Contato")
  print("2. Visualizar Contato")
  print("3. Editar um Contato")
  print("4. Marcar/Desmarcar um contato como Favorito")
  print("5. Ver Lista de Contatos Favoritos")
  print("6. Apagar um Contato")
  print("7. Sair\n")

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
    edicao_contato = input("Verifique a lista acima e digite o código do contato que deseja alterar: ")
    novo_dados_nome = input("Digite um novo nome para o contato: ")
    novo_dados_telefone = input("Digite um novo telefone para o contato: ")
    novo_dados_email = input("Digite um novo email para o contato: ")
    editar_contato(agenda, novo_dados_nome, novo_dados_telefone, novo_dados_email)
    
  elif escolha == "7":
    break