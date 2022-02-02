from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

class Application():
	"""Main class for the app """
	def __init__(self, master=None):
		"""Class attributes"""
		self.fonteTitulo = ("Helvetica", "20", "bold")
		self.fonteLabels = ("Helvetica", "14", "bold", "italic")
		self.fonteAvisos = ("Helvetica", "18", "bold")
		self.fonteEntry = ("Helvetica", "14")
		self.fonteRodape = ("Helvetica", "7", "bold", "italic")
		self.imgBanner = ImageTk.PhotoImage(Image.open("./resources/img_banner.png").resize((800, 75),Image.ANTIALIAS))
		self.bgColor = "#cecece"
		# Listas de informacoes disponiveis sobre estacoes para consulta
		self.optionsNomeEstacao = ["teste1", "teste2", "teste3"]
		self.optionsCodEstacao= ["teste4", "teste5", "teste6"]
		self.optionsNomeLinha = ['teste7', "teste8", "teste9"]
		self.optionsNomeLinha = ['teste10', "teste11", "teste12"]
		self.optionsNomeAdministradora = ['teste13', "teste14", "teste15"]
		self.optionsTransferencia = ["Sim", "Não"]

		self.testarJanelas()

		"""Creating screen elements"""

		"""Container Geral"""
		self.containerGeral = Frame(master, bg=self.bgColor, height=600, width=800, borderwidth=2, relief=RIDGE)
		self.containerGeral.pack()
		

		"""Container banner"""
		self.containerBanner = Frame(self.containerGeral, bg=self.bgColor, height=75, width=800, borderwidth=2, relief=RIDGE)
		self.containerBanner.pack()
		self.bannerLabel = Label(self.containerBanner, image=self.imgBanner, bg=self.bgColor)
		self.bannerLabel.image=self.imgBanner
		self.bannerLabel.pack()


		"""Container do título"""
		self.containerTitulo = Frame(self.containerGeral, height=30, width=600, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerTitulo.pack(pady=(10,0))
		self.tituloLabel = Label(self.containerTitulo, text="GESTÃO DE ESTAÇÕES", font=self.fonteTitulo, bg=self.bgColor)
		self.tituloLabel.pack()


		"""Container consulta/inclusao"""
		self.containerConsultaInclusao = Frame(self.containerGeral, height=528, width=800, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerConsultaInclusao.pack(pady=(10,20))


		"""Container de consulta"""
		self.containerConsulta = Frame(self.containerConsultaInclusao, height=525, width=400, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerConsulta.pack(side=LEFT, padx=(0,30), pady=(18,0))
		# 
		# Container de consulta - Campos
		self.containerConsultaCampos = Frame(self.containerConsulta, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerConsultaCampos.pack()
		# 
		# nome da estacao
		self.labelNomeEstacaoConsulta = Label(self.containerConsultaCampos, text="NOME DA ESTAÇÃO", font=self.fonteLabels, bg=self.bgColor)
		self.labelNomeEstacaoConsulta.pack(anchor=W, pady=(5,0))
		self.entryNomeEstacaoConsulta = ttk.Combobox(self.containerConsultaCampos, font=self.fonteEntry, width=22)
		self.entryNomeEstacaoConsulta["values"] = self.optionsNomeEstacao
		# self.entryNomeEstacaoConsulta.bind("<<ComboboxSelected>>", funcao)
		self.entryNomeEstacaoConsulta.pack(anchor=W)
		# 
		# codigo da estacao
		self.labelCodEstacaoConsulta = Label(self.containerConsultaCampos, text="CÓDIGO DA ESTAÇÃO", font=self.fonteLabels, bg=self.bgColor)
		self.labelCodEstacaoConsulta.pack(anchor=W, pady=(5,0))
		self.entryCodEstacaoConsulta = ttk.Combobox(self.containerConsultaCampos, font=self.fonteEntry, width=22)
		self.entryCodEstacaoConsulta["values"] = self.optionsCodEstacao
		# self.entryCodEstacaoConsulta.bind("<<ComboboxSelected>>", funcao)
		self.entryCodEstacaoConsulta.pack(anchor=W)
		# 
		# transferencia
		self.labelTransferenciaConsulta = Label(self.containerConsultaCampos, text="TRANSFERÊNCIA", font=self.fonteLabels, bg=self.bgColor)
		self.labelTransferenciaConsulta.pack(anchor=W, pady=(5,0))
		self.entryTransferenciaConsulta = Entry(self.containerConsultaCampos, font=self.fonteEntry, bg=self.bgColor, state="readonly", width=24)
		self.entryTransferenciaConsulta.pack(anchor=W)
		# 
		# nome da linha
		self.labelNomeLinhaConsulta = Label(self.containerConsultaCampos, text="LINHA", font=self.fonteLabels, bg=self.bgColor)
		self.labelNomeLinhaConsulta.pack(anchor=W, pady=(5,0))
		# self.scrollbarNomeLinhaConsulta = Scrollbar(self.containerConsultaCampos, orient=VERTICAL)
		self.listboxNomeLinhaConsulta = Listbox(self.containerConsultaCampos, width=25, height=5, font=self.fonteEntry)
		self.listboxNomeLinhaConsulta.pack()
		# for item in self.optionsNomeLinha:
		# 	self.listboxNomeLinhaConsulta.insert(END, item)
		# self.entryNomeLinhaConsulta = Entry(self.containerConsultaCampos, font=self.fonteEntry, bg=self.bgColor, state="readonly", width=24)
		# self.entryNomeLinhaConsulta.pack(anchor=W)
		# 
		# nome da administradora
		self.labelNomeAdministradoraConsulta = Label(self.containerConsultaCampos, text="NOME DA ADMINISTRADORA", font=self.fonteLabels, bg=self.bgColor)
		self.labelNomeAdministradoraConsulta.pack(anchor=W, pady=(5,0))
		self.entryNomeAdministradoraConsulta = Entry(self.containerConsultaCampos, font=self.fonteEntry, bg=self.bgColor, state="readonly", width=24)
		self.entryNomeAdministradoraConsulta.pack(anchor=W)
		# 
		# Container de consulta - Botoes
		self.containerConsultaBotoes = Frame(self.containerConsulta, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerConsultaBotoes.pack(pady=10)
		# 
		self.btnConsultar = Button(self.containerConsultaBotoes, text="CONSULTAR", font=self.fonteLabels, width=12, command=lambda: self.consultarEstacao())
		self.btnConsultar.pack(side=LEFT, padx=(10,5))
		# 
		self.btnEditar = Button(self.containerConsultaBotoes, text="EDITAR", font=self.fonteLabels, width=12, command=lambda: self.abrirJanelaEdicao())
		self.btnEditar.pack(side=LEFT, padx=(5,5))
		# 
		self.btnLimparConsulta = Button(self.containerConsultaBotoes, text="LIMPAR", font=self.fonteLabels, width=12, command=lambda: self.limparConsulta())
		self.btnLimparConsulta.pack(side=RIGHT, padx=(5,10))

		"""Container de inclusão"""
		self.containerIncluir = Frame(self.containerConsultaInclusao, height=525, width=400, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerIncluir.pack(side=LEFT, padx=(50,0))
		# 
		#  Container de inclusão - Campos
		self.containerIncluirCampos = Frame(self.containerIncluir, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerIncluirCampos.pack()
		#
		# nome estacao
		self.labelNomeEstacaoIncluir = Label(self.containerIncluirCampos, text="NOME DA ESTAÇÃO", font=self.fonteLabels, bg=self.bgColor)
		self.labelNomeEstacaoIncluir.pack(anchor=W, pady=(5,0))
		self.entryNomeEstacaoIncluir = Entry(self.containerIncluirCampos, font=self.fonteEntry, width=24)
		self.entryNomeEstacaoIncluir.pack(anchor=W)
		# 
		# transferencia
		self.labelTransferenciaIncluir = Label(self.containerIncluirCampos, text="TRANSFERÊNCIA", font=self.fonteLabels, bg=self.bgColor)
		self.labelTransferenciaIncluir.pack(anchor=W, pady=(5,0))
		self.entryTransferenciaIncluir = ttk.Combobox(self.containerIncluirCampos, font=self.fonteEntry, width=22, state="readonly")
		self.entryTransferenciaIncluir["values"] = self.optionsTransferencia
		self.entryTransferenciaIncluir.bind("<<ComboboxSelected>>", self.selecionarLinhasTransferencia)
		self.entryTransferenciaIncluir.pack(anchor=W)
		# 
		# nome linha principal
		self.labelNomeLinhaIncluir = Label(self.containerIncluirCampos, text="LINHA", font=self.fonteLabels, bg=self.bgColor)
		self.labelNomeLinhaIncluir.pack(anchor=W, pady=(5,0))
		self.entryNomeLinhaIncluir = ttk.Combobox(self.containerIncluirCampos, font=self.fonteEntry, width=22, state="readonly")
		self.entryNomeLinhaIncluir["values"] = self.optionsNomeLinha
		# self.entryNomeLinhaIncluir.bind("<<ComboboxSelected>>", funcao)
		self.entryNomeLinhaIncluir.pack(anchor=W)
		# 
		# nome linha adj 1
		self.entryNomeLinhaAdj1Incluir = ttk.Combobox(self.containerIncluirCampos, font=self.fonteEntry, width=22, state="disabled")
		self.entryNomeLinhaAdj1Incluir["values"] = self.optionsNomeLinha
		# self.entryNomeLinhaAdj1Incluir.bind("<<ComboboxSelected>>", funcao)
		self.entryNomeLinhaAdj1Incluir.pack(anchor=W)
		# 
		# nome linha adj 2
		self.entryNomeLinhaAdj2Incluir = ttk.Combobox(self.containerIncluirCampos, font=self.fonteEntry, width=22, state="disabled")
		self.entryNomeLinhaAdj2Incluir["values"] = self.optionsNomeLinha
		# self.entryNomeLinhaAdj2Incluir.bind("<<ComboboxSelected>>", funcao)
		self.entryNomeLinhaAdj2Incluir.pack(anchor=W)
		# 
		# nome linha adj 3
		self.entryNomeLinhaAdj3Incluir = ttk.Combobox(self.containerIncluirCampos, font=self.fonteEntry, width=22, state="disabled")
		self.entryNomeLinhaAdj3Incluir["values"] = self.optionsNomeLinha
		# self.entryNomeLinhaAdj3Incluir.bind("<<ComboboxSelected>>", funcao)
		self.entryNomeLinhaAdj3Incluir.pack(anchor=W)
		# 
		# nome linha adj 4
		self.entryNomeLinhaAdj4Incluir = ttk.Combobox(self.containerIncluirCampos, font=self.fonteEntry, width=22, state="disabled")
		self.entryNomeLinhaAdj4Incluir["values"] = self.optionsNomeLinha
		# self.entryNomeLinhaAdj4Incluir.bind("<<ComboboxSelected>>", funcao)
		self.entryNomeLinhaAdj4Incluir.pack(anchor=W)
		# 
		# estacao referencia
		self.labelEstacaoRefIncluir = Label(self.containerIncluirCampos, text="ESTAÇÃO REFERÊNCIA", font=self.fonteLabels, bg=self.bgColor)
		self.labelEstacaoRefIncluir.pack(anchor=W, pady=(5,0))
		self.entryEstacaoRefIncluir = ttk.Combobox(self.containerIncluirCampos, font=self.fonteEntry, width=22, state="readonly")
		self.entryEstacaoRefIncluir["values"] = self.optionsCodEstacao
		# self.entryEstacaoRefIncluir.bind("<<ComboboxSelected>>", funcao)
		self.entryEstacaoRefIncluir.pack(anchor=W)
		# 
		#  Container de inclusão - Botões de Rádio
		self.containerIncluirRadioBtn = Frame(self.containerIncluir, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerIncluirRadioBtn.pack()
		self.opcaoPosicaoReferencia = StringVar()
		self.radioBtnPosicaoAnterior = Radiobutton(self.containerIncluirRadioBtn, text="ANTERIOR", variable=self.opcaoPosicaoReferencia, value="anterior", font=self.fonteLabels, bg=self.bgColor)
		self.radioBtnPosicaoAnterior.pack(side=LEFT)
		self.radioBtnPosicaoPosterior = Radiobutton(self.containerIncluirRadioBtn, text="POSTERIOR", variable=self.opcaoPosicaoReferencia, value="posterior", font=self.fonteLabels, bg=self.bgColor)
		self.radioBtnPosicaoPosterior.pack(side=RIGHT)
		# 
		#  Container de inclusão - Botão
		self.containerIncluirBotao = Frame(self.containerIncluir, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerIncluirBotao.pack(pady=10)
		self.btnIncluir = Button(self.containerIncluirBotao, text="INCLUIR", font=self.fonteLabels, width=12, command=lambda: self.incluirEstacao())
		self.btnIncluir.pack(side=LEFT, padx=(10,5))
		self.btnLimpar = Button(self.containerIncluirBotao, text="LIMPAR", font=self.fonteLabels, width=12, command=lambda: self.limparInclusao())
		self.btnLimpar.pack(side=RIGHT, padx=(5,10))
		

		"""Container Rodapé"""
		self.containerRodape = Frame(self.containerGeral, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		self.containerRodape.pack(padx=(660,0))
		self.labelRodape = Label(self.containerRodape, text="METRÔ GO VERSÃO DE TESTES - 2.0", font=self.fonteRodape, bg=self.bgColor)
		self.labelRodape.pack(anchor=E)

	
	"""Application functions"""

	def limparConsulta(self):
		self.entryNomeEstacaoConsulta.set("")
		self.entryCodEstacaoConsulta.set("")
		self.listboxNomeLinhaConsulta.delete(0, END)
		self.entryNomeAdministradoraConsulta.delete(0, END)
		self.entryTransferenciaConsulta.delete(0, END)


	def selecionarLinhasTransferencia(self, event=None):
		transferencia = str(self.entryTransferenciaIncluir.get())
		if transferencia == 'Sim':
			self.entryNomeLinhaAdj1Incluir['state'] = 'readonly'
			self.entryNomeLinhaAdj2Incluir['state'] = 'readonly'
			self.entryNomeLinhaAdj3Incluir['state'] = 'readonly'
			self.entryNomeLinhaAdj4Incluir['state'] = 'readonly'
		else:
			self.entryNomeLinhaAdj1Incluir['state'] = 'disabled'
			self.entryNomeLinhaAdj2Incluir['state'] = 'disabled'
			self.entryNomeLinhaAdj3Incluir['state'] = 'disabled'
			self.entryNomeLinhaAdj4Incluir['state'] = 'disabled'
		# print(event)

	def limparInclusao(self):
		self.entryNomeEstacaoIncluir.delete(0, END)
		self.entryTransferenciaIncluir.set("")
		self.selecionarLinhasTransferencia()
		self.entryNomeLinhaIncluir.set("")
		self.entryNomeLinhaAdj1Incluir.set("")
		self.entryNomeLinhaAdj2Incluir.set("")
		self.entryNomeLinhaAdj3Incluir.set("")
		self.entryNomeLinhaAdj4Incluir.set("")
		self.entryEstacaoRefIncluir.set("")

	def consultarEstacao(self):
		self.abrirAvisoConsulta()
		return


	def abrirAvisoConsulta(self):
		self.construirJanelaMensagem("Nenhuma estação selecionada!")


	def abrirJanelaEdicao(self):
		self.construirJanelaEdicao()


	def incluirEstacao(self):
		return


	def editarEstacao(self):
		return


	def deletarEstacao(self):
		self.construirJanelaConfirmacao("Deletar a estação selecionada?")


	def construirJanelaEdicao(self):
		"""Janela de Edição de Estações"""
		janelaEdicao = Toplevel()
		janelaEdicao.title("Editar Estação")

		"""Elementos da tela"""
		containerGeral = Frame(janelaEdicao, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerGeral.pack()
		# 
		# titulo
		containerTitulo = Frame(containerGeral, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerTitulo.pack()
		labelTitulo = Label(containerTitulo, text="EDIÇÃO DE ESTAÇÃO", font=self.fonteTitulo, bg=self.bgColor)
		labelTitulo.pack()
		# 
		# campos
		containerCampos = Frame(containerGeral, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerCampos.pack()
		# 
		# nome estacao
		labelNomeEstacao = Label(containerCampos, text="NOME DA ESTAÇÃO", font=self.fonteLabels, bg=self.bgColor)
		labelNomeEstacao.pack(anchor=W, pady=(5,0))
		entryNomeEstacao = Entry(containerCampos, font=self.fonteEntry, width=24)
		entryNomeEstacao.pack(anchor=W)
		# 
		# nome administradora
		labelNomeAdmin = Label(containerCampos, text="NOME DA ADMINISTRADORA", font=self.fonteLabels, bg=self.bgColor)
		labelNomeAdmin.pack(anchor=W, pady=(5,0))
		entryNomeAdmin = ttk.Combobox(containerCampos, font=self.fonteEntry, width=22, state="readonly")
		entryNomeAdmin["values"] = self.optionsNomeAdministradora
		# entryNomeAdmin.bind("<<ComboboxSelected>>", funcao)
		entryNomeAdmin.pack(anchor=W)
		# 
		# tranferencia
		labelTransferencia = Label(containerCampos, text="TRANSFERÊNCIA", font=self.fonteLabels, bg=self.bgColor)
		labelTransferencia.pack(anchor=W, pady=(5,0))
		entryTransferencia = ttk.Combobox(containerCampos, font=self.fonteEntry, width=22, state="readonly")
		entryTransferencia["values"] = self.optionsTransferencia
		# entryTransferencia.bind("<<ComboboxSelected>>", funcao)
		entryTransferencia.pack(anchor=W)
		# 
		# botoes
		containerBotoes = Frame(containerGeral, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerBotoes.pack()
		btnConfirmar = Button(containerBotoes, text="INCLUIR", font=self.fonteLabels, width=12, command=lambda: self.editarEstacao())
		btnConfirmar.pack(side=LEFT, padx=(10,5))
		btnDeletar = Button(containerBotoes, text="DELETAR", font=self.fonteLabels, width=12, command=lambda: self.deletarEstacao())
		btnDeletar.pack(side=LEFT, padx=(5,5))
		btnCancelar = Button(containerBotoes, text="CANCELAR", font=self.fonteLabels, width=12, command=janelaEdicao.destroy)
		btnCancelar.pack(side=LEFT, padx=(5,10))


	def construirJanelaMensagem(self, mensagem=None):
		mensagem = str(mensagem)
		"""Janela de Mensagem"""
		janelaMensagem = Toplevel()
		janelaMensagem.title("AVISO")

		"""Elementos da tela"""
		containerGeral = Frame(janelaMensagem, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerGeral.pack()
		# 
		# mensagem
		containerMensagem = Frame(containerGeral, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerMensagem.pack(padx=10, pady=15)
		labelMensagem = Label(containerMensagem, text=mensagem, font=self.fonteAvisos, bg=self.bgColor)
		labelMensagem.pack()
		# botoes
		containerBotoes = Frame(containerGeral, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerBotoes.pack(pady=(0,10))
		btnConfirmar = Button(containerBotoes, text="OK", font=self.fonteLabels, width=12, command=janelaMensagem.destroy)
		btnConfirmar.pack()


	def construirJanelaConfirmacao(self, mensagem=None):
		mensagem = str(mensagem)
		"""Janela de Confirmação"""
		janelaConfirmacao = Toplevel()
		janelaConfirmacao.title("CONFIRMAÇÃO")

		"""Elementos da tela"""
		containerGeral = Frame(janelaConfirmacao, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerGeral.pack()
		# 
		# mensagem
		containerMensagem = Frame(containerGeral, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerMensagem.pack(padx=10, pady=15)
		labelMensagem = Label(containerMensagem, text=mensagem, font=self.fonteAvisos, bg=self.bgColor)
		labelMensagem.pack()
		# botoes
		containerBotoes = Frame(containerGeral, bg=self.bgColor, borderwidth=2, relief=RIDGE)
		containerBotoes.pack(pady=(0,10))
		btnConfirmar = Button(containerBotoes, text="SIM", font=self.fonteLabels, width=12, command=janelaConfirmacao.destroy)
		btnConfirmar.pack(side=LEFT, padx=(10,5))
		btnCancelar = Button(containerBotoes, text="NÃO", font=self.fonteLabels, width=12, command=janelaConfirmacao.destroy)
		btnCancelar.pack(side=RIGHT, padx=(5,10))

	def testarJanelas(self):
		self.construirJanelaMensagem("Nenhuma estação selecionada!")
		self.construirJanelaMensagem("Estação incluída!")
		self.construirJanelaMensagem("Estação já existe!")
		self.construirJanelaMensagem("Estação editada!")
		self.construirJanelaMensagem("Estação deletada do sistema!")
		self.construirJanelaConfirmacao("Deletar a estação selecionada?")


root = Tk()
root.title("MetroGO - Sistema de Gerenciamento")
root.geometry("800x600")
Application(root)
root.mainloop()