pip install graphviz
from graphviz import Digraph

dot = Digraph(comment='Modelo Conceitual - Oficina Mecânica')

# Estilo dos nós
node_attr = {'shape': 'record', 'style': 'filled', 'fillcolor': '#f9f9f9'}

# Entidades
dot.node('Cliente', '''{Cliente|+ id_cliente (PK)\\l- nome\\l- telefone\\l- endereco\\l}''', **node_attr)
dot.node('Veiculo', '''{Veículo|+ id_veiculo (PK)\\l- id_cliente (FK)\\l- placa\\l- modelo\\l- marca\\l- ano\\l}''', **node_attr)
dot.node('Equipe', '''{Equipe|+ id_equipe (PK)\\l- nome_equipe\\l}''', **node_attr)
dot.node('Mecanico', '''{Mecânico|+ id_mecanico (PK)\\l- nome\\l- endereco\\l- especialidade\\l- id_equipe (FK)\\l}''', **node_attr)
dot.node('OS', '''{Ordem_Serviço|+ id_os (PK)\\l- id_veiculo (FK)\\l- id_equipe (FK)\\l- data_emissao\\l- data_conclusao\\l- status\\l- valor_total\\l}''', **node_attr)
dot.node('Servico', '''{Serviço|+ id_servico (PK)\\l- descricao\\l- valor_mao_obra\\l}''', **node_attr)
dot.node('Peca', '''{Peça|+ id_peca (PK)\\l- descricao\\l- valor\\l}''', **node_attr)
dot.node('Item_Servico', '''{Item_Serviço|+ id_item_servico (PK)\\l- id_os (FK)\\l- id_servico (FK)\\l- aprovado (bool)\\l}''', **node_attr)
dot.node('Item_Peca', '''{Item_Peça|+ id_item_peca (PK)\\l- id_os (FK)\\l- id_peca (FK)\\l- quantidade\\l}''', **node_attr)

# Relacionamentos
dot.edge('Cliente', 'Veiculo', label='1:N')
dot.edge('Veiculo', 'OS', label='1:N')
dot.edge('Equipe', 'OS', label='1:N')
dot.edge('Equipe', 'Mecanico', label='1:N')
dot.edge('OS', 'Item_Servico', label='1:N')
dot.edge('Servico', 'Item_Servico', label='1:N')
dot.edge('OS', 'Item_Peca', label='1:N')
dot.edge('Peca', 'Item_Peca', label='1:N')

# Exportar como imagem
dot.format = 'png'
dot.render('modelo_conceitual_oficina', cleanup=True)
