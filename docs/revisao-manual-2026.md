# Revisão de conteúdo — 05/09/2026

Referência: `manual_do_mesario.pdf` do repositório, edição TSE 2026. Os exemplos de Ata são sugestões de redação; não são transcrições nem substituem as orientações do Cartório.

| Tema | Páginas do manual | Ajuste |
| --- | --- | --- |
| Trabalho em equipe e horários | 7–9, 31 | Distribuição usual na matriz, possibilidade de designação pela Presidência e regra de substituição às 07h30. Chegada conforme o Cartório. Preferências conferidas com a lista da pág. 9, incluindo a expressão “mais de 80 anos”. |
| Identificação e nome social | 10, 16, 18, 21 | Inclusão de identidade social, consulta pelo documento quando não se sabe CPF/título e retirada de afirmações sobre prints não detalhadas no manual. Persistindo dúvida de identidade, solicitar a Juíza ou o Juiz Eleitoral. |
| Instalação e Zerésima | 4, 9, 12–15 | Sequência antes da votação, teste de autenticidade antes da Zerésima quando sorteada, indicadores de segurança e participação facultativa das duas primeiras pessoas. |
| Biometria | 19, 21 | Separação entre ausência de dados biométricos e falha após quatro tentativas. Ano de nascimento, atestação pela Presidência quando aplicável e assinatura antes do voto. |
| Suspensão e ocorrências | 16–17, 21–22, 24, 28–32 | Distinção entre ausência total de voto e voto em algum cargo; comunicação ao Cartório, registro de aceitação/recusa dos convidados e exemplos sem presunção de providências. |
| Encerramento e MR | 24–25, 29 | Atender a fila antes de encerrar, manter a porta aberta, retirar a MR apenas após mensagem da urna, recolocar tampa, aplicar lacre assinado e aguardar FIM DOS TRABALHOS. Exceção de BU ilegível persistente: não retirar a MR. |
| Relatórios e destinação | 26–27, 32 | BEHB = Boletim de Eleitores Habilitados Biograficamente. Destinação das vias do BU sem inventar numeração ou terceira via anexada à Ata. NC somente ao final da votação. Devolução de RJE e formulários de deficiência preenchidos e não utilizados. |
| Cadernos e mídias | 17–18, 24–25, 32 | Remoção do limite não fundamentado de três cadernos físicos e das descrições técnicas de mídias não respaldadas pelo manual. |

## Verificação técnica

- Base preservada: commit `f4286c3`, que introduziu os ajustes de responsividade do autor.
- HTML conferido quanto a fechamento de tags e IDs duplicados; 28 itens de checklist e 14 fichas cobrindo os 25 itens da Ata.
- Nove abas verificadas com viewport de 320 pixels, sem transbordamento horizontal da página; tabelas com rolagem interna.
- Checklist: marcar todos (28/28), limpar (0/28) e marcação individual (1/28).
- Filtros de assinaturas e ocorrências, resposta do quiz e expansão/recolhimento do mapa verificados no navegador.
- Mapa passa a abrir recolhido e a se reenquadrar ao redimensionar a tela.
- `scripts/sync_site.py --check` verifica a igualdade entre o HTML fonte e a entrada do Pages.

Esta revisão é uma conferência editorial contra a edição do manual incluída no repositório, não uma homologação pela Justiça Eleitoral. Alterações futuras no manual ou orientações locais devem motivar nova revisão.
