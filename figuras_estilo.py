# -*- coding: utf-8 -*-
"""Padrão visual das figuras do artigo (usado pelos cadernos 04 e 13).

- Largura fixa de 16 cm (6,3 pol.), a largura útil de uma página A4 com margens de 2,5 cm: inserida no Word a 100%,
  a fonte sai no tamanho real (9 pt) e igual em todas as figuras.
- Sem bbox='tight': o PNG sai exatamente com o tamanho pedido (1890 px de largura a 300 dpi).
- Uma cor de destaque (azul-escuro) contra cinza: a diferença de claridade se mantém em impressão P&B, e o destaque
  também é marcado pelo preenchimento do marcador (cheio x vazado), não só pela cor.
- Fonte: Times New Roman (template do evento); Liberation Serif tem as mesmas métricas e é usada quando a Times não
  está instalada (Linux).
"""
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

AZUL = '#1c5cab'        # destaque (significativo / estimativa principal)
AZUL_CLARO = '#86b6ef'
CINZA = '#a3a29c'       # não significativo / contexto
CINZA_PONTO = '#8d8c86'
TINTA, TINTA_2, GRADE = '#0b0b0b', '#52514e', '#e4e3df'
LARGURA = 6.3           # polegadas (16 cm)


def estilo():
    mpl.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
        'mathtext.fontset': 'stix',
        'font.size': 9, 'axes.labelsize': 9, 'xtick.labelsize': 8.5, 'ytick.labelsize': 9, 'legend.fontsize': 8.5,
        'axes.edgecolor': TINTA_2, 'axes.labelcolor': TINTA, 'xtick.color': TINTA_2, 'ytick.color': TINTA,
        'axes.linewidth': 0.6, 'xtick.major.width': 0.6, 'ytick.major.width': 0.6,
        'axes.spines.top': False, 'axes.spines.right': False, 'axes.grid': True, 'axes.grid.axis': 'x',
        'grid.color': GRADE, 'axes.axisbelow': True, 'grid.linewidth': 0.6,
        'savefig.dpi': 300, 'savefig.facecolor': 'white', 'savefig.bbox': None,
    })
    os.makedirs('Figuras', exist_ok=True)


def virgula(casas):
    """Formatador de eixo com vírgula decimal e sinal de menos tipográfico."""
    return FuncFormatter(lambda v, _: f'{v:.{casas}f}'.replace('.', ',').replace('-', '−'))


def br(v, casas=2, sinal=False):
    s = f'{v:+.{casas}f}' if sinal else f'{v:.{casas}f}'
    return s.replace('.', ',').replace('-', '−')


def p_txt(p):
    return 'p < 0,001' if p < 0.001 else 'p = ' + f'{p:.3f}'.replace('.', ',')


def coluna(ax, y, texto, dx_pt, ha='right', **kw):
    """Escreve texto numa coluna à direita do eixo, a dx_pt pontos da borda direita (independe da escala)."""
    kw.setdefault('fontsize', 8.5)
    t = ax.annotate(texto, xy=(1, y), xycoords=('axes fraction', 'data'), xytext=(dx_pt, 0),
                    textcoords='offset points', ha=ha, va='center', annotation_clip=False, **kw)
    t.set_in_layout(False)   # o espaço da coluna é reservado por rect=... no layout, não pelo texto


def salvar(fig, nome):
    caminho = os.path.join('Figuras', nome)
    fig.savefig(caminho)     # sem bbox_inches='tight': largura final fixa de 16 cm
    print('Figura salva em', caminho)
    return caminho
