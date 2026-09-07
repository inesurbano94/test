# Sine — Brinquedos personalizados a partir de desenhos

Site de página única em português (pt-PT), estático, **ficheiro único**
(`index.html` — HTML, CSS e JS inline, sem `assets/` nem build step),
seguindo a mesma estrutura de ficheiro do site real do Isaías Rocha
(branch `novo-site-isaias`, publicado em produção via Vercel).

## Sobre a réplica de design

O primeiro rascunho deste site (agora substituído) tinha sido construído
a partir de uma versão antiga/diferente do site do Isaías que existia no
branch por defeito deste repositório — não a versão real publicada. Esta
versão foi reconstruída a partir do ficheiro real do branch
`novo-site-isaias` (fundo escuro/branco minimalista, tipografia
-apple-system/Helvetica, botões em pílula, nav fixa com menu hamburger,
carrossel horizontal com snap-scroll, cartões full-bleed, secção de
métricas com cartão branco com grelha de ícones, CTA final escura com
textura de pontos). A cor de destaque (laranja/coral) e todo o conteúdo
são próprios do Sine — só a técnica/estrutura visual foi replicada, nunca
o nome, morada, telefone ou testemunhos reais do Isaías.

## Contexto: isto é uma página de "fake door" (validação de ideia)

O negócio ainda não está lançado. Segundo o briefing: uma criança desenha
um brinquedo, o desenho é transformado num modelo 3D, impresso e entregue
em casa. Preços, materiais definitivos e prazos **ainda não estão
decididos**. Por isso, este site foi construído deliberadamente para:

- Não inventar preços — não há secção de preços fixos; os CTAs pedem para
  "registar interesse", não para comprar.
- Não fabricar testemunhos de clientes reais — `#inspiracao` mostra
  cartões de "ideias/conceito", não avaliações de pessoas que não existem.
- Usar ilustrações CSS/SVG em vez de fotos reais do produto (ainda não
  existem) — inclusive no hero, que por isso tem altura definida pelo
  conteúdo em vez de forçar uma altura de ecrã inteiro só para uma foto
  que ainda não existe (ver comentário no CSS do `.hero`).

## Antes de publicar / lançar a sério

1. **Número de WhatsApp** — o número usado (`351900000000`) é placeholder;
   procurar por essa string no `index.html` e substituir em todas as
   ocorrências.
2. **Preços** — definir e adicionar uma secção de preços reais quando
   estiverem decididos.
3. **Materiais e segurança** — confirmar e documentar de forma concreta os
   materiais de impressão usados e a sua adequação a brinquedos infantis
   (certificações aplicáveis) antes de vender a sério.
4. **Fotos/logo reais** — substituir as ilustrações SVG (hero, cartões)
   por fotos reais de brinquedos e/ou um logo, assim que existirem. Nessa
   altura, o hero pode voltar a ser um hero de foto full-bleed com altura
   de ecrã (ver nota no CSS).
5. **Testemunhos reais (`#inspiracao`)** — substituir os cartões de
   "inspiração" por histórias reais de famílias, com consentimento
   explícito, assim que houver clientes reais.
6. **Entregas** — confirmar zonas de entrega, transportadora e prazos
   reais de produção.

## Correr localmente

```
python3 -m http.server 8000
```

depois abrir `http://localhost:8000/sine/`.
