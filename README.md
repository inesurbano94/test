# Isaías Rocha — Personal Trainer (Lisboa)

Site de página única em português (pt-PT), estático (HTML/CSS/JS puros — sem build step).

## Estrutura

```
index.html            todo o conteúdo/marcação, organizado por <section id="...">
assets/css/style.css   sistema de design (cores, tipografia, layout, animações)
assets/js/main.js      menu mobile, scroll reveal, botão flutuante, links de WhatsApp
```

## Fonte de conteúdo

Todo o texto (bio, certificações, abordagem, objetivos, processo, serviços e preços)
vem diretamente do documento de briefing do cliente — não foram inventados factos.
Onde o briefing não tinha informação (nº de WhatsApp, Instagram, e-mail, testemunhos
reais de clientes, fotografia profissional), foi deixado um placeholder claro em vez
de se inventar um valor. Ver notas abaixo.

## Antes de publicar

1. **Número de WhatsApp** — editar `WHATSAPP_NUMBER` em `assets/js/main.js` (linha ~10).
   Todos os botões "Falar no WhatsApp" / "Marcar sessão" leem deste único sítio.
2. **Fotografias** — as imagens atuais são placeholders do Unsplash (a preto e branco/duotone
   via CSS). Substituir os `src` das `<img>` em Hero, Sobre, Serviços e Localização por
   fotografia real do Isaías (idealmente still shots de treino, retrato editorial, mesma
   paleta tonal).
3. **Instagram / e-mail** — o briefing não incluía estes dados, por isso não aparecem no
   site. Assim que existirem, adicionar um link discreto na secção `#contacto`.
4. **Testemunhos reais** — a secção `#confianca` liga diretamente para as avaliações no
   Google Maps (link do briefing) em vez de citações inventadas. Quando houver testemunhos
   reais de clientes (nome, comentário, resultado, foto autorizada), podem substituir ou
   complementar esse link com citações na própria secção.
5. **Localização exata** — a secção `#localizacao` usa o link de Google Maps fornecido no
   briefing como CTA "Ver no Google Maps", em vez de um mapa embutido (não havia morada
   exata/Place ID para gerar um embed fiável).
6. **Preços e serviços** — já refletem os valores reais do briefing (Personal Training 1:1,
   Bring a Friend, Avaliação Física + Plano de Treino). Rever periodicamente caso os preços
   mudem.

## Adicionar versão em inglês

O conteúdo está isolado do layout (nenhum texto está "cozido" em CSS/imagens), pelo que basta:

1. Duplicar `index.html` como `en.html`.
2. Traduzir apenas os nós de texto — manter classes, ids e estrutura intactos.
3. Adicionar um seletor de idioma na nav (`.nav__links`) a apontar `index.html` ⇄ `en.html`.

## Correr localmente

Qualquer servidor estático funciona, por exemplo:

```
python3 -m http.server 8000
```

depois abrir `http://localhost:8000`.
