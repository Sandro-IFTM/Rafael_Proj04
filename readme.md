# TCC — Rafael Santos (Projeto 04)

### Estudo Hedônico de Precificação de Sêmen da Raça Nelore (CRV Lagoa / ANCP)
- **Orientando:** Rafael Santos
- **Orientador:** Prof. Sandro
- **Instituição:** Instituto Federal do Triângulo Mineiro (IFTM)
- **Pós-Graduação:** Especialização em Ciência de Dados / Zootecnia Aplicada

### Como reproduzir
1. **Coleta (caderno 01):** ambiente `environment.yml` (Python 3.11). Gera `Dados/CSV/NeloreCRV.csv`. Executar de novo
   baixa o catálogo atual e substitui a base de setembro de 2026 usada no artigo.
2. **Análises (cadernos 02 a 13):** ambiente `requirements_analise.txt`. Executar **em ordem**, a partir da raiz do
   repositório: 02 gera os CSVs por programa e `NeloreCRV_Dados_Gerais.csv`; 03 gera `NeloreCRV_ANCP_valido.csv`
   (N = 115); 04 a 13 leem esses arquivos.
3. **Figuras do artigo:** geradas pelos cadernos 04 (Figuras 1 e 2) e 13 (Figuras 3 e 4) em `Figuras/`, com o estilo
   comum de `figuras_estilo.py` (16 cm de largura, 300 dpi, Times New Roman).

### Pastas
- `Dados/`: CSVs e XLSX da coleta e da limpeza.
- `Docs/`: versões do artigo (SIMPÓS 2026) e proposta do TCC.
- `Figuras/`: figuras do artigo.
- `Referencias/`: PDFs citados, textos convertidos (`texto/`) e a planilha `Verificacao_citacoes.xlsx`.
