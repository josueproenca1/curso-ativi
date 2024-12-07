import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MonitoramentoAgua:
    def __init__(self):  
        self.histórico = []

    def adicionar_consumo(self, consumo):
        """Adiciona um valor de consumo ao histórico e retorna a mensagem formatada."""
        if consumo < 0:
            return consumo, "Erro", "Erro: Consumo inválido."
        self.histórico.append(consumo)
        media = self.calcular_media()
        if consumo > media:
            alerta = "Consumo acima da média!"
        elif consumo < media:
            alerta = "Consumo abaixo da média."
        else:
            alerta = "Consumo dentro da média."
        return consumo, self.histórico, media, alerta

    def calcular_media(self):
        """Calcula a média do consumo de água."""
        if len(self.histórico) > 0:
            return sum(self.histórico) / len(self.histórico)
        else:
            return 0

    def gerar_relatorio(self):
        """Gera um resumo das informações do monitoramento."""
        if not self.histórico:
            return "Nenhum dado registrado."
        total_consumo = sum(self.histórico)
        media_consumo = self.calcular_media()
        num_registros = len(self.histórico)
        maior_consumo = max(self.histórico)
        menor_consumo = min(self.histórico)

        relatorio = (
            f"Relatório de Consumo de Água:\n"
            f"- Total de Consumo: {total_consumo}\n"
            f"- Média Geral: {media_consumo:.2f}\n"
            f"- Número de Registros: {num_registros}\n"
            f"- Maior Consumo: {maior_consumo}\n"
            f"- Menor Consumo: {menor_consumo}\n"
        )
        return relatorio


# Função para carregar os consumos pré-definidos e exibir os resultados na tabela
def carregar_consumos():
    consumos_predefinidos = [50, 60, 100, 0, -20]  # Valores pré-definidos
    for consumo in consumos_predefinidos:
        consumo_valor, historico, media, alerta = monitoramento.adicionar_consumo(consumo)
        # Inserindo os dados na tabela
        tree.insert("", "end", values=(consumo_valor, str(historico), f"{media:.1f}", alerta))


# Função para exibir o relatório em uma janela de diálogo
def exibir_relatorio():
    relatorio = monitoramento.gerar_relatorio()
    messagebox.showinfo("Relatório", relatorio)


# Inicializando o Tkinter
janela = tk.Tk()
janela.title("Monitoramento de Consumo de Água")
janela.geometry("600x400")

# Criando a instância do monitoramento
monitoramento = MonitoramentoAgua()

# Botão para carregar consumos
btn_carregar = tk.Button(janela, text="Carregar Consumos Pré-definidos", command=carregar_consumos)
btn_carregar.pack(pady=10)

# Botão para gerar relatório
btn_relatorio = tk.Button(janela, text="Gerar Relatório", command=exibir_relatorio)
btn_relatorio.pack(pady=10)
# Tabela para exibir os resultados
frame_tabela = tk.Frame(janela)
frame_tabela.pack(fill="both", expand=True, pady=10)

# Criando a tabela com Treeview
tree = ttk.Treeview(frame_tabela, columns=("Consumo", "Histórico", "Média", "Alerta"), show="headings", height=10)

# Definindo os cabeçalhos da tabela
tree.heading("Consumo", text="Consumo")
tree.heading("Histórico", text="Histórico")
tree.heading("Média", text="Média")
tree.heading("Alerta", text="Alerta")

# Definindo a largura das colunas
tree.column("Consumo", width=100, anchor="center")
tree.column("Histórico", width=200, anchor="center")
tree.column("Média", width=100, anchor="center")
tree.column("Alerta", width=200, anchor="center")

# Exibindo a tabela
tree.pack(fill="both", expand=True)

# Iniciar o loop da interface
janela.mainloop()
