# Mesa Receptora de Votos (MRV) – Eleições 2026

Material interativo e didático de apoio e instrutoria para treinamento de mesárias e mesários nas Eleições de 2026, material complementar baseado no **Manual do Mesário 2026** (*Resolução-TSE nº 23.751/2026*).

🌐 **Acesso Online (GitHub Pages):** [https://darkfl-source.github.io/apoio_tre/](https://darkfl-source.github.io/apoio_tre/)

---

## 📌 Módulos e Recursos Interativos

1. **Mapa Mental Interativo (D3 / Markmap):** Navegação hierárquica por papéis e procedimentos com zoom, recolhimento de ramos e botão de exportação em PNG de alta resolução.
2. **Fichas Individuais por Função:** Detalhamento das atribuições de Presidente, 1º e 2º Mesários e Secretário(a).
3. **Matriz de Responsabilidades:** Cruzamento de 12 tarefas com badges de responsabilidade por papel.
4. **Linha Sucessória e Hierarquia:** Regra de substituição das 07h30 e linha de sucessão presidencial da seção.
5. **Documentos de Identificação Civil:** Tabela de documentos aceitos e proibidos (Pág. 10 do Manual), regras de nome social e simulador prático.
6. **Checklist Pré-Votação (antes das 08h00):** 28 itens de conferência em 4 etapas com barra dinâmica de progresso.
7. **Guia de Assinaturas e Relatórios:** Regras de ouro (biometria dispensando assinatura, o que fiscais podem/não podem assinar, Lacre Azul) e simulador rápido (quiz).
8. **Catálogo de Ocorrências em Ata:** Os 25 itens oficiais do verso da Ata (Pág. 32 do Manual) organizados em 6 categorias e 14 fichas com sugestões de redação, a adaptar aos fatos ocorridos.
9. **Operação da Urna, Logística e Encerramento:** Passo a passo do registro de mesários na urna, consulta aos cadernos da seção, de seções agregadas e de transferência temporária, mídias da urna (MR vs MV), rito das 17h00 e matriz tripla de destinação final de materiais.

---

## 🛠️ Tecnologias Utilizadas
- HTML5 / CSS3 responsivo (tema institucional da Justiça Eleitoral)
- JavaScript Vanilla (sem dependências locais)
- D3.js + Markmap View / Markmap Lib
- Font Awesome 6 + Google Fonts (Plus Jakarta Sans)
- html2canvas (para exportação em imagem nítida)

---
*Desenvolvido para apoio às equipes de treinamento da Justiça Eleitoral.*

## Revisão e manutenção

Revisão de conteúdo em **05/09/2026**, tendo como referência o `manual_do_mesario.pdf` deste repositório. As referências nas tabelas abrem as páginas do PDF. O material complementa o manual e as orientações do Cartório Eleitoral; não é uma publicação oficial do TSE. Todos os horários são de Brasília.

O arquivo fonte é `mapa_mental_mrv.html`. Após editá-lo, atualize a entrada do GitHub Pages:

```sh
python scripts/sync_site.py
python scripts/sync_site.py --check
```

Faça commit dos dois HTMLs juntos. A publicação existente do Pages acompanha a branch `main`. Detalhes da revisão: [revisao-manual-2026.md](docs/revisao-manual-2026.md).

As bibliotecas do mapa, exportação, fontes e ícones são carregadas de serviços externos; o funcionamento completo offline não é garantido.
