# Sine — Brinquedos personalizados a partir de desenhos

Site de página única em português (pt-PT), estático (HTML/CSS/JS puros — sem
build step). Reutiliza a mesma estrutura/design system do template de
referência (`isaias`), com conteúdo adaptado ao negócio do Sine.

## Estrutura

```
index.html            todo o conteúdo/marcação, organizado por <section id="...">
assets/css/style.css   sistema de design (cores, tipografia, layout, animações)
assets/js/main.js      menu mobile, scroll reveal, botão flutuante, links de WhatsApp
```

## Contexto: isto é uma página de "fake door" (validação de ideia)

O negócio ainda não está lançado. Segundo o briefing: uma criança desenha um
brinquedo, o desenho é transformado num modelo 3D, impresso e entregue em
casa. Preços, materiais definitivos e prazos **ainda não estão decididos**.

Por isso, este site foi construído deliberadamente para:
- Não inventar preços — `#servicos` usa "A definir" em vez de números reais.
- Não fabricar testemunhos de clientes reais — `#resultados` mostra cartões
  de "inspiração" (ideias de conceito), não avaliações de pessoas que não
  existem.
- Usar ilustrações SVG em vez de fotos reais do produto (ainda não existem).

## Antes de publicar / lançar a sério

1. **Número de WhatsApp** — editar `WHATSAPP_NUMBER` em `assets/js/main.js`.
2. **Preços (`#servicos`)** — substituir "A definir" pelos preços reais assim
   que estiverem decididos.
3. **Materiais e segurança (`#faq`)** — confirmar e documentar de forma
   concreta os materiais de impressão usados e a sua adequação a brinquedos
   infantis (certificações aplicáveis) antes de vender a sério.
4. **Fotos/logo reais** — substituir as ilustrações SVG (hero e "Sobre") por
   fotos reais de brinquedos e/ou um logo, assim que existirem.
5. **Testemunhos reais (`#resultados`)** — substituir os cartões de
   "inspiração" por histórias reais de famílias, com consentimento explícito,
   assim que houver clientes reais.
6. **Entregas (`#localizacao`)** — confirmar zonas de entrega, transportadora
   e prazos reais de produção.

## Correr localmente

```
python3 -m http.server 8000
```

depois abrir `http://localhost:8000/sine/`.
