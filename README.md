# controle_barbearia
É um aplicativo simples para controle de serviços/agendamentos de barbearia usando o framework Flask em Python.

Funcionalidades

Exibição da Agenda: 
	Acessa a página principal para visualizar a agenda e horários disponíveis.
Agendamento: 
	O usuário preenche o formulário com o nome, seleciona um horário e o serviço desejado para agendar.
Cancelamento: 
	Se necessário, é possível cancelar um agendamento existente clicando no botão "Cancelar" ao lado do horário na lista de agendamentos.

Como Executar:
	1. Necessário ter o Python instalado.
	2. Instale a biblioteca Flask para executar:
		pip install Flask
	3. Execute o aplicativo no CMD usando o comando:
		python Controle_servicos_barbearia.py
	4. Abra o navegador e acesse http://localhost:5000/

Estrutura do Código:
	app.py: Estrutura lógica do aplicativo Flask.
	templates/index.html: O arquivo HTML responsável por renderizar a interface do usuário.

Desenvolvimento:
	A agenda de horários é gerada automaticamente para as horas entre 9h e 21h.
	Os horários disponíveis são exibidos na página principal.
	Os usuários podem agendar um horário preenchendo o formulário.
	O aplicativo verifica se o horário escolhido está disponível antes de confirmar o agendamento.
	Os agendamentos são canceláveis, removendo as informações associadas ao horário selecionado.

Contribuições:
	Se tratando de um app simples, qualquer contribuição para melhoria e crescimento será bem vinda!

Bruno Kleins

