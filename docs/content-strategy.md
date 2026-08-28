# Estrutura, conteúdo e SEO — análise

> Auditoria da estrutura atual do `index.html` face aos objetivos de
> negócio em `docs/business-requirements.md`, com recomendações de
> conteúdo, conversão e SEO. Baseada em evidência real do código
> (não em suposições genéricas) — cada ponto abaixo tem origem
> identificada no ficheiro.

## Objetivos de negócio do site

A partir de `docs/business-requirements.md`, o site tem essencialmente
**um** objetivo de conversão — gerar uma mensagem de WhatsApp — e três
objetivos de suporte:

1. **Converter** visitantes em mensagens de WhatsApp qualificadas.
2. **Pré-qualificar** o lead, deixando-o identificar-se com um
   objetivo (dor, força, peso, etc.) antes de escrever.
3. **Credibilizar** o Isaías o suficiente para um estranho lhe mandar
   mensagem (certificações, bio, prova social).
4. **Aparecer** em pesquisas locais — "personal trainer Lisboa",
   "personal trainer VivaGym Almirante Reis".

Não há venda direta no site (sem checkout/pagamento) — todo o
"conteúdo para conversão" existe para reduzir a fricção até ao clique
de WhatsApp.

## Estrutura atual vs. funil

| Secção | Estágio do funil | Serve o objetivo de negócio | Estado |
|---|---|---|---|
| Hero | Atenção | Proposta de valor + CTA imediato | ✅ Dois CTAs (WhatsApp direto e scroll) |
| Objetivos | Interesse / auto-qualificação | Pré-qualificar o lead | ✅ Redesenhado recentemente — rápido de scanear |
| Sobre | Confiança | Certificações, bio, expertise | ✅ Forte — bio completa + pull-quote |
| Resultados | Prova social | Testemunhos | ⚠️ Ver Gap 2 |
| Localização | Redução de fricção | Mostrar opções (ginásio/casa/outdoor) | ⚠️ Fotos ainda stock (já sinalizado) |
| FAQ | Objeções | Responder dúvidas antes do CTA final | ⚠️ Ver Gap 3 |
| Contacto | Ação final | CTA + FAB fixo sempre visível | ✅ |

A ordem das secções está bem pensada: o FAQ (objeções) vem mesmo antes
do CTA final de Contacto, o que é a posição certa — tirar dúvidas
imediatamente antes de pedir a ação.

## Pontos fortes já confirmados no código

- `<title>` e `<meta name="description">` têm as keywords certas
  ("Personal Trainer em Lisboa", "VivaGym Almirante Reis") sem soar a
  spam.
- O `alt` das fotos já inclui contexto geográfico relevante
  ("Sessão de treino na VivaGym Almirante Reis", "...outdoor em
  Lisboa") — bom para SEO de imagem sem exagerar.
- Já existe `JSON-LD` (`ProfessionalService`) no `<head>` — a maioria
  dos sites deste porte nem tem isto.
- O CTA de WhatsApp está omnipresente e consistente: nav, hero, toda a
  grelha de Objetivos (cada cartão é clicável), Localização, Contacto
  e o botão flutuante (FAB).
- Tipografia dos títulos agora consistente (hero + section-title)
  melhora o scanning — indiretamente ajuda conversão.

## Gaps, por impacto

### 🔴 Crítico — bloqueia conversão

**1. Número de WhatsApp ainda é placeholder** (`351900000000` em
`assets/js/main.js`). Todo o site converte para um número que não
existe. Nada dos pontos abaixo importa enquanto isto não for
resolvido.

### 🟠 Alto impacto

**2. "5.0 · Avaliações reais no Google" é uma afirmação não
verdadeira** enquanto os 3 testemunhos em `#resultados` forem
fictícios (confirmado no próprio `README.md`). Isto é um risco de
credibilidade — e reputacional, se alguém for verificar no Google e
não encontrar nada. Recomendação: remover esta linha específica (ou
trocar por algo que não invoque uma fonte externa verificável) até
existirem avaliações reais.

**3. Preço não aparece em lado nenhum do site.** Foi uma decisão
explícita do cliente (secção "Serviços" removida — ver
`docs/business-requirements.md` §3). Do ponto de vista de conversão
há um trade-off real dos dois lados: sem preço reduz-se a hesitação de
"deve ser caro" antes mesmo de escrever, mas aumenta-se o volume de
mensagens que só perguntam valores (que podiam ser respondidas
automaticamente pelo próprio site). Vale a pena confirmar com o
Isaías se prefere manter assim ou testar mostrar só o valor de
entrada ("sessões a partir de €30").

### 🟡 Médio impacto — SEO, baixo risco/esforço

**4. Sem `FAQPage` structured data.** A secção FAQ já tem exatamente o
formato que o Google usa para rich snippets (pergunta + resposta).
Falta o JSON-LD `FAQPage` correspondente — é só extrair o que já está
em `#faq`, sem inventar nada, e sem qualquer alteração visual.

**5. `JSON-LD` incompleto para SEO local.** Falta `streetAddress`,
`telephone`, `openingHours`, `geo` e `image` no `ProfessionalService`
atual. Isto ajuda o Google a mostrar mais informação diretamente nos
resultados e a ligar melhor a um perfil Google Business, se existir.

**6. Sem `og:image`.** Quando o link é partilhado no WhatsApp,
Instagram ou Facebook, não aparece nenhuma imagem de pré-visualização
— só o texto. Para um negócio que depende de recomendação boca-a-boca
via WhatsApp, isto tem impacto direto e é uma correção trivial (já
existe a foto real do hero para usar).

**7. Sem `sitemap.xml` nem `robots.txt`.** Não bloqueiam indexação,
mas são o mínimo esperado por crawlers e triviais de adicionar a um
site estático de uma página.

### 🟢 Já sinalizado noutro lado

**8. Fotos de stock** (Localização, Contacto) e **testemunhos
fictícios** — já documentados em `README.md` e
`docs/business-requirements.md`, não repetido aqui em detalhe.

## Perguntas para o Isaías (decisões que só ele pode tomar)

- Mostrar preços no site, ou manter só disponíveis por WhatsApp?
- Autoriza remover/reformular a linha "avaliações reais no Google" até
  existirem avaliações verdadeiras?
- Morada exata (rua/nº) do VivaGym e um telefone/e-mail para o schema
  de SEO local — ou prefere manter só "Lisboa"?
- Já existe (ou vale a pena criar) um perfil Google Business Profile
  reclamado? Ajuda SEO local mas é trabalho fora do site.

## Próximos passos sugeridos, por ordem

1. **Número de WhatsApp real** — crítico, bloqueador, esforço trivial.
2. **Ajustar a afirmação de avaliações reais** — alto impacto,
   esforço trivial.
3. **`FAQPage` schema + completar `JSON-LD` local + `og:image`** —
   SEO, baixo risco, posso implementar agora sem esperar por decisão
   do cliente (não muda nada visível nem inventa factos).
4. **Decidir sobre mostrar preços** — precisa de confirmação do
   Isaías antes de mexer no site.
5. **Fotos reais e testemunhos reais** — já em curso, sem alteração
   de código necessária até haver material novo.
