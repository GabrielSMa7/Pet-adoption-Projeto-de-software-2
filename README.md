# Pet-adoption-Projeto-de-software-2
Classes adicionadas:

classe adicionada em pet_profile
  Pet
  A classe pets tem name, size, age, type, color, shelter(que apresenta em qual abrigo o pet está) e race

classe adicionada na funcionalidade de user_profile
  User
  A classe users tem name, password, email, phone e age

classe adicionada na funcionalidade de shelter_profile
  Shelter
  A classe shelter name, local, email, pets (que apresenta a quantidade de pets disponiveis) e us(uma breve descrição do abrigo)

# Pet-adoption-Projeto-de-software
Recursos implementados:

# Pet Profile Management:
     Apresenta características básicas do pet disponível para adoção como por exemplo, nome, cor, idade, tamanho e tipo

# User Account Management:
     Cria e modifica informações da conta do usuário como nome, endereço, idade e email
     Caso digite 1 ele cria a conta e caso 2 altera as informações desejadas e caso 3 retorna para o menu inicial

# Search and Filter Options:
     Filtra os pets que vão ser apresentados de acordo com a escolha do usuario podendo escolher entre "type"(Cat ou Dog), "size"(Big, medium ou small) e "gender"(Male ou female)
     Digitando "y" apresenta os tipos de filtros disponiveis
     Após aplicado é apresentados quantos itens são compativéis e se deseja adicionar outro filtro
     Digitando "n" nenhum outro filtro é adicionado

# Shelter and Rescue Organization Proles:
     Apresenta características básicas do abrigos disponiveis como nome, quantidade de pets disponiveis, email, telefone e uma preve descrição do abrigo
     Digitando o nome do abrigo é apresentado as informações basicas dele
     Caso digite 1 é apresentado os pets que o abrigo tem disponivel
     Caso 2 é feita uma doação para o abrigo escolhido
     Caso 3 retorna para o menu inicial
     
# Donation Processing:
     Caso o usuario escolha a opção doar para o abrigo de adoção o programa pede o valor que vai ser doado e retorna uma mensagem de agradecimento do abrigo ajudado

# Community Forum:
     Um forum onde é possivel acessar a lista de eventos(Digitando 1), perguntas de usuarios(Digitando 2), dicas de cuidados e auxilio no processo de adoção(Digitando 3) e historias de pets resgatados(digitando 5) 

# Educational Resources:
     No menu de forum em Help and tips
     Apresenta dicas de cuidado com pets e como funciona o processo de adoção

# Event Listing and Management:
     No menu do forum em Events
     Apresenta uma lista de eventos agendados e mostra informações basicas deles como hórario de inicio e encerramento, local, e finalidade
     Os eventos apresentados podem ser filtrados por tipo, eventos de vacinação ou de adoção.

#  Success Stories and Testimonials:
     No menu do forum em Successful stories
     É apresentado uma lista com pets que já foram resgatados 
     O usuario pode escolher qual historia ele quer ver e então é apresentado o abrigo que o pet fazia parte e sua historia
