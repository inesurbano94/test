# Isaías Rocha — Personal Trainer (Lisboa)

Site de página única em português (pt-PT), estático (HTML/CSS/JS puros — sem build step).

Reconstruído de raiz: nova direção de design (Atelier Soft, adaptado — acento
terracota, Cormorant + Jost), nova estrutura e cópia reescrita, mantendo a
foto real do Isaías. Todo o texto vem do documento "Isaías Rocha — Briefing".

## Estrutura

```
index.html             todo o conteúdo/marcação, organizado por <section id="...">
assets/css/style.css   sistema de design (tokens, tipografia, layout, animações)
assets/js/main.js      número de WhatsApp central, menu mobile, scroll reveal, botão flutuante
assets/img/            fotografia (isaias-hero.webp — foto real)
```

## Antes de publicar

1. **Número de WhatsApp — o mais importante.** O briefing não tem um número
   confirmado. Está como placeholder (`351900000000`) em **um único sítio**:
   `WHATSAPP_NUMBER` em `assets/js/main.js` (linha ~5). Todos os botões e
   links "WhatsApp" do site (hero, serviços, localização, CTA final, botão
   flutuante) leem daí — basta substituir o número real e todo o site fica
   correto.
2. **Testemunhos** — não incluídos. O briefing não tem testemunhos reais
   (nomes, fotos ou avaliações de clientes), por isso a secção não foi
   inventada. Se o Isaías conseguir 2-3 testemunhos reais (com consentimento
   para usar nome e, idealmente, foto), há espaço óbvio para uma secção nova
   entre "Treino" e "Serviços".
3. **Fotografia adicional** — o site usa apenas a foto do hero
   (`assets/img/isaias-hero.webp`, já real). Uma segunda foto — o Isaías a
   dar uma aula de Pilates/Cycling, ou num momento de avaliação física —
   reforçaria a secção "Sobre", que atualmente é só texto.
4. **Mapa (Localização)** — o botão "Ver localização no Google Maps" aponta
   para uma pesquisa real da VivaGym Almirante Reis. Pode ser trocado por um
   embed (`<iframe>`) se preferires um mapa incorporado na página.
5. **Contacto** — o briefing só confirma WhatsApp como canal de marcação; sem
   e-mail ou Instagram confirmados, por isso não aparecem no site. É fácil
   acrescentar um link de Instagram no cabeçalho/rodapé se o Isaías quiser.
6. **Preços e serviços** — confirmar que os valores em `#servicos`
   (Avaliação 50€, Personal Training 1:1, Ao domicílio, Bring Your Friend)
   continuam atuais antes de publicar; são os do briefing mas podem mudar.

## Sistema de design

- **Direção:** Atelier Soft, adaptado — base papel/creme quente, acento
  terracota único, cantos quase retos, espaçamento generoso.
- **Tipografia:** Cormorant (títulos, itálico para ênfase) + Jost (texto,
  navegação, botões).
- **Tokens** em `:root`, no topo de `assets/css/style.css` — trocar a paleta
  ou tipografia é uma edição de ~20 linhas, não uma reescrita do markup.
- Secção "Treino" usa fundo escuro (`--deep`) como pontuação entre secções
  claras, com uma lista assimétrica de focos de treino (não mais um grid de
  3 colunas repetido).

## Adicionar versão em inglês

O conteúdo está isolado do layout (nenhum texto está "cozido" em CSS/imagens):

1. Duplicar `index.html` como `/en/index.html`.
2. Traduzir apenas os nós de texto — manter classes, ids e estrutura intactos.
3. Adicionar `<link rel="alternate" hreflang="...">` a apontar de um para o
   outro, e um seletor de idioma na nav.

## Correr localmente

Qualquer servidor estático funciona, por exemplo:

```
python3 -m http.server 8000
```

depois abrir `http://localhost:8000`.
