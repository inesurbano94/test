# Isaías Rocha — Personal Trainer (Lisboa)

Site de página única em português (pt-PT), estático (HTML/CSS/JS puros — sem build step).

Rebuild feito com a skill `website-studio`, fase 4 (build) — ver
`.claude/skills/website-studio/`. Direção aprovada na fase 2: sistema
`clinic-white` adaptado a quente, tipografia Familjen Grotesk + Instrument
Sans, sem testemunhos fictícios — a prova vem do método, da avaliação por
bioimpedância e das certificações.

## Estrutura

```
index.html             todo o conteúdo/marcação, organizado por <section id="...">
assets/css/style.css   sistema de design (tokens em :root, layout, motion)
assets/js/main.js      número de WhatsApp, menu mobile, scroll reveal, tabs de preços, FAQ
assets/img/            imagens
```

## Fonte de verdade do conteúdo

Todo o texto (bio, certificações, método, preços, localização) vem do
documento "Isaías Rocha — Briefing" no Drive. Qualquer novo facto, preço ou
afirmação deve ser confirmado com o Isaías antes de entrar no site.

**Sem testemunhos.** O briefing não tem testemunhos de clientes reais. Ao
contrário da versão anterior deste site, esta versão **não** usa testemunhos
fictícios — decisão explícita, ver fase 1 da conversa com a skill. A prova de
credibilidade vem da secção `#medicao` (bioimpedância), das certificações em
`#sobre` e do método em `#metodo`.

## Antes de publicar

1. **Número de WhatsApp** — `WHATSAPP_NUMBER` em `assets/js/main.js` (linha
   ~7) está com um placeholder (`351900000000`). O briefing não indica um
   número real — todos os botões de WhatsApp leem deste único sítio, por isso
   basta corrigir aqui.
2. **Fotografia** — só existe uma foto real, `assets/img/isaias-hero.webp`,
   usada em `#sobre`. É um retrato forte mas não um hero: enquadramento
   vertical, passadeiras e dois ecrãs de TV ao fundo, luz de tecto fria. Em
   produção, recortar mais apertado (a `object-position` já força o foco para
   cima) ou substituir por uma foto nova. Ver
   `.claude/skills/website-studio/templates/shot-list.md` para o plano de 5
   fotos que faltam — a mais importante é a da balança de bioimpedância em
   uso, é a única imagem que ainda ninguém tem.
3. **Morada do ginásio** — Av. Almirante Reis 65, 1150-011 Lisboa, em
   `#localizacao`. Veio de pesquisa pública sobre o VivaGym, não do briefing
   do Isaías — confirmar antes de publicar.
4. **Preços e serviços** — confirmar que os valores em `#servicos` continuam
   atualizados; vêm do briefing mas podem mudar com o tempo.
5. **Instagram / Google Maps** — não encontrei perfis públicos do Isaías
   (sem Instagram, sem ficha do Google Maps). O site é, por agora, toda a
   presença online dele — se e quando existirem, adicionar os links em
   `#localizacao` e no rodapé.

## Adicionar versão em inglês

Decisão da fase 1: **pt-PT apenas**, por agora. Se mudar, seguir a regra da
skill — dois ficheiros HTML (`index.html` + `en/index.html`), nunca um
seletor por JavaScript, por SEO e para não haver flash da língua errada.
Ver `.claude/skills/website-studio/guidelines.md`, secção "Bilingual sites".

## Correr localmente

```
python3 -m http.server 8000
```

depois abrir `http://localhost:8000`.
