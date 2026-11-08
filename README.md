# claude-travel-planner-latam

[![Validate](https://github.com/jalcalaroot/claude-travel-planner-latam/actions/workflows/validate.yml/badge.svg)](https://github.com/jalcalaroot/claude-travel-planner-latam/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/tag/jalcalaroot/claude-travel-planner-latam?label=version)](CHANGELOG.md)

A Claude skill that compares flights, hotels and activities across several sources at once, built for travelers departing from Latin America.

> [Leer en español](#español)

## Why use this skill

Without this skill, Claude can search travel sites, but each answer depends on how you ask. You can get one source, no comparison, or no reviews. With this skill:

- **One request, a complete comparison.** Claude checks two flight sources, hotels with reviews, and activities (when the connectors are connected), without step-by-step instructions from you.
- **Better prices.** The same route is compared across sources, so you see differences that one site alone does not show.
- **Fewer bad hotels.** Hotel options are checked against traveler reviews before they reach you.
- **Made for Latin America.** It looks for regional airlines and connections (Panama, Sao Paulo, Bogota, Lima) and reminds you to compare local payment options, such as installments.
- **Family friendly.** Children's ages, kid-friendly hotels and activities, and the Caribbean hurricane season are part of the process.
- **Safe by design.** It never books or pays, in the browser it only uses search fields (never sign-in, personal data or checkout), and it treats website content as data, not as instructions.
- **Same format every time.** You always get one table with the total price for the whole group, pros, cons and links to buy.

## Requirements

A skill contains instructions only. **It cannot install connectors for you.** Before you use this skill, add the following connectors to your Claude account at [claude.ai/customize/connectors](https://claude.ai/customize/connectors). The five travel connectors do not require an account with the travel company.

### Required connectors

| Connector | Why it is needed |
|---|---|
| **Expedia** | Main source for flights and hotels. Strong coverage of the United States and the Caribbean. |
| **eDreams** | Second flight source. The skill compares the same route against Expedia to find the best price. |
| **Booking.com** | Main source for hotels, apartments and homes. |
| **Tripadvisor** | Traveler reviews. The skill uses them to discard hotels with repeated complaints. |

Without the required connectors, the skill still works, but the comparison is weaker. It tells you which ones are missing.

### Recommended connectors and tools

| Connector or tool | Why it helps |
|---|---|
| **Viator** | Activities and tours at the destination. Without it, the answer has no activity suggestions. No account needed. |
| **Claude in Chrome** | Lets Claude search Google Flights and airline websites in your browser to confirm prices and see the fare calendar. It only fills in search fields: it never signs in, enters personal data or goes to checkout. |
| **Google Calendar** | Reads your calendar to find conflicts with the trip dates. Uses your own Google account. It never creates events. |

## How it works

1. **Profile:** uses your home airport, preferred airlines and travel style, or asks for them.
2. **Sources:** checks which connectors are available and tells you if one is missing.
3. **Flights:** searches the same route in Expedia and eDreams, and confirms prices in Google Flights when a browser is available. Keeps three options: the cheapest, the most convenient, and the best one with your preferred airline.
4. **Hotels:** searches Booking.com and checks the best options against Tripadvisor reviews. For the Caribbean, it includes an all-inclusive option.
5. **Activities:** suggests three to five activities from Viator.
6. **Calendar and season:** checks date conflicts and warns about the Atlantic hurricane season (June to November).
7. **Result:** one comparison table with the total price for the whole group, pros, cons and links to buy.

## Installation

### Claude app (recommended)

Trip planning is a conversation, so the Claude app (web, desktop or mobile) is the best place to use this skill.

1. **Add the connectors first** at [claude.ai/customize/connectors](https://claude.ai/customize/connectors).
2. In the app, open **Customize**, then **Plugins**, select **Add marketplace**, and enter `jalcalaroot/claude-travel-planner-latam`.
3. Install the **travel-planner-latam** plugin and start a new conversation.

Full step-by-step guide, with an option to upload the skill as a file: [docs/install-claude-app.md](docs/install-claude-app.md).

### Claude Code

For people who prefer the terminal, or who want to work on the skill:

```
/plugin marketplace add jalcalaroot/claude-travel-planner-latam
/plugin install travel-planner-latam@claude-travel-planner-latam
```

Add the connectors first with the same Claude account. Full guide, with checks and troubleshooting: [docs/install-claude-code.md](docs/install-claude-code.md).

## Make it yours

Make a private copy of `skills/travel-planner-latam/SKILL.md`, fill in the **Traveler profile** section: home airport, preferred airlines, hotel style, and whether you travel with children, and upload it as a file (see the app guide). If you leave the placeholders, Claude asks only for what it needs.

Do not publish your personal copy if it contains private details.

## Example

See [examples/example-request.md](examples/example-request.md).

## Limits

- Prices change. Always confirm the final price on the seller website before you pay.
- Connectors are run by third parties. If a connector changes or stops working, results can change.
- The skill does not check entry requirements. Confirm visas, electronic travel authorizations and documents for minors on official government websites.
- This project is not affiliated with Anthropic or with any airline, hotel or travel company.

## Contributing and security

- [CONTRIBUTING.md](CONTRIBUTING.md): how to propose changes.
- [SECURITY.md](SECURITY.md): design principles and how to report a problem.
- [PRIVACY.md](PRIVACY.md): what data moves where when you use the skill.
- [CHANGELOG.md](CHANGELOG.md): version history.

## License

MIT. See [LICENSE](LICENSE).

---

## Español

Una skill de Claude que compara vuelos, hoteles y actividades en varias fuentes a la vez, pensada para viajeros que salen de Latinoamérica.

### Por qué usar esta skill

Sin la skill, Claude puede buscar en sitios de viaje, pero el resultado depende de cómo le pidas. Puede usar una sola fuente, no comparar o no mirar reseñas. Con la skill:

- **Un pedido, una comparación completa.** Revisa dos fuentes de vuelos, hoteles con reseñas y actividades (si tenés los conectores), sin que tengas que pedir cada paso.
- **Mejores precios.** Compara la misma ruta en varias fuentes y te muestra diferencias que un solo sitio no muestra.
- **Menos hoteles malos.** Filtra los hoteles con reseñas de viajeros antes de mostrártelos.
- **Pensada para Latinoamérica.** Busca aerolíneas y conexiones de la región (Panamá, San Pablo, Bogotá, Lima) y te recuerda comparar opciones de pago locales, como las cuotas.
- **Para viajar en familia.** Tiene en cuenta las edades de los chicos, hoteles y actividades aptos para ellos y la temporada de huracanes del Caribe.
- **Segura.** Nunca reserva ni paga, en el navegador solo usa los campos de búsqueda (nunca inicia sesión, carga datos personales ni avanza al pago) y trata el contenido de las webs como datos, no como instrucciones.
- **Siempre el mismo formato.** Una tabla con el precio total para todo el grupo, pros, contras y links para comprar.

### Requisitos

Una skill contiene solo instrucciones: **no puede instalar conectores por vos.** Antes de usarla, agregá estos conectores a tu cuenta de Claude en [claude.ai/customize/connectors](https://claude.ai/customize/connectors). Los cinco conectores de viaje no piden cuenta en la empresa de viajes.

**Conectores necesarios**

| Conector | Para qué se necesita |
|---|---|
| **Expedia** | Fuente principal de vuelos y hoteles. Muy fuerte en Estados Unidos y el Caribe. |
| **eDreams** | Segunda fuente de vuelos. La skill compara la misma ruta contra Expedia para encontrar el mejor precio. |
| **Booking.com** | Fuente principal de hoteles, departamentos y casas. |
| **Tripadvisor** | Reseñas de viajeros. La skill las usa para descartar hoteles con quejas repetidas. |

Sin los conectores necesarios la skill igual funciona, pero la comparación es más débil. Te avisa cuáles faltan.

**Conectores y herramientas recomendados**

| Conector o herramienta | Para qué sirve |
|---|---|
| **Viator** | Actividades y excursiones en destino. Sin él, la respuesta no sugiere actividades. No pide cuenta. |
| **Claude in Chrome** | Permite buscar en Google Flights y en las webs de las aerolíneas desde tu navegador para confirmar precios y ver el calendario de tarifas. Solo completa campos de búsqueda: nunca inicia sesión, carga datos personales ni avanza al pago. |
| **Google Calendar** | Lee tu calendario para detectar conflictos con las fechas del viaje. Usa tu propia cuenta de Google y nunca crea eventos. |

### Cómo funciona

1. **Perfil:** usa tu aeropuerto de salida, aerolíneas preferidas y estilo de viaje, o te los pregunta.
2. **Fuentes:** revisa qué conectores hay y te avisa si falta alguno.
3. **Vuelos:** busca la misma ruta en Expedia y eDreams, y confirma precios en Google Flights si hay navegador. Te deja tres opciones: la más barata, la más conveniente y la mejor con tu aerolínea preferida.
4. **Hoteles:** busca en Booking.com y filtra las mejores opciones con reseñas de Tripadvisor. En el Caribe incluye una opción all inclusive.
5. **Actividades:** sugiere de tres a cinco actividades de Viator.
6. **Calendario y temporada:** revisa conflictos de fechas y avisa por la temporada de huracanes del Atlántico (junio a noviembre).
7. **Resultado:** una tabla comparativa con el precio total para todo el grupo, pros, contras y links para comprar.

### Instalación

**App de Claude (recomendada).** Planificar un viaje es una conversación, así que la app de Claude (web, escritorio o celular) es el mejor lugar para usar esta skill.

1. **Primero agregá los conectores** en [claude.ai/customize/connectors](https://claude.ai/customize/connectors).
2. En la app, abrí **Customize**, después **Plugins**, elegí **Add marketplace** y escribí `jalcalaroot/claude-travel-planner-latam`.
3. Instalá el plugin **travel-planner-latam** y abrí una conversación nueva.

Guía paso a paso, con la opción de subir la skill como archivo: [docs/install-claude-app.md](docs/install-claude-app.md#guía-en-español).

**Claude Code.** Para quien prefiere la terminal o quiere trabajar sobre la skill: agregá los conectores con la misma cuenta y usá los dos comandos `/plugin` de la sección *Installation*. Guía completa: [docs/install-claude-code.md](docs/install-claude-code.md#guía-en-español).

### Personalizala

Hacé una copia privada de `skills/travel-planner-latam/SKILL.md` y completá la sección **Traveler profile**: aeropuerto de salida, aerolíneas preferidas, tipo de hotel y si viajás con chicos. No publiques tu copia personal si tiene datos privados.

### Ejemplo

Mirá [examples/example-request.md](examples/example-request.md).

### Límites

- Los precios cambian: confirmá el precio final en la web del vendedor antes de pagar.
- Los conectores los operan terceros. Si un conector cambia o deja de funcionar, los resultados pueden cambiar.
- La skill no verifica requisitos de entrada. Confirmá visas, autorizaciones electrónicas y documentos de menores en sitios oficiales.
- Este proyecto no está afiliado a Anthropic ni a ninguna aerolínea, hotel o agencia.

### Contribuir y seguridad

Mirá [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), [PRIVACY.md](PRIVACY.md) y [CHANGELOG.md](CHANGELOG.md).
