# claude-travel-planner-latam

[![Validate](https://github.com/jalcalaroot/claude-travel-planner-latam/actions/workflows/validate.yml/badge.svg)](https://github.com/jalcalaroot/claude-travel-planner-latam/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Version](https://img.shields.io/badge/version-0.1.0-informational)

A Claude skill that compares flights, hotels and activities across several sources at once, built for travelers departing from Latin America.

> [Leer en español](#español)

## Why use this skill

Without this skill, Claude can search travel sites, but each answer depends on how you ask. You can get one source, no comparison, or no reviews. With this skill:

- **One request, a complete comparison.** Claude always checks two flight sources, hotels with reviews, and activities, without step-by-step instructions from you.
- **Better prices.** The same route is compared across sources, so you see differences that one site alone does not show.
- **Fewer bad hotels.** Hotel options are checked against traveler reviews before they reach you.
- **Made for Latin America.** It looks for regional airlines and connections (Panama, Sao Paulo, Bogota, Lima) and reminds you to compare local payment options, such as installments.
- **Family friendly.** Children's ages, kid-friendly hotels and activities, and the Caribbean hurricane season are part of the process.
- **Safe by design.** It never books or pays, and it treats website content as data, not as instructions.
- **Same format every time.** You always get one table with the total price for the whole group, pros, cons and links to buy.

## Requirements

A skill contains instructions only. **It cannot install connectors for you.** Before you use this skill, connect the following connectors from the Claude connector directory (in Claude: Settings, then Connectors). None of them requires an account.

### Required connectors

| Connector | Why it is needed |
|---|---|
| **Expedia** | Main source for flights, hotels and flight-plus-hotel packages. Strong coverage of the United States and the Caribbean. |
| **eDreams** | Second flight source. The skill compares the same route against Expedia to find the best price. |
| **Booking.com** | Main source for hotels, apartments and homes. |
| **Tripadvisor** | Traveler reviews. The skill uses them to discard hotels with repeated complaints. |

Without the required connectors, the skill still works, but the comparison is weaker. It tells you which ones are missing.

### Recommended connectors and tools

| Connector or tool | Why it helps |
|---|---|
| **Viator** | Activities and tours at the destination. Without it, the answer has no activity suggestions. |
| **Claude in Chrome** | Lets Claude open Google Flights and airline websites in your browser to confirm prices and see the fare calendar. |
| **Google Calendar** | Checks your calendar for conflicts with the trip dates. Uses your own Google account. |

## How it works

1. **Profile:** uses your home airport, preferred airlines and travel style, or asks for them.
2. **Sources:** checks which connectors are available and tells you if one is missing.
3. **Flights:** searches the same route in Expedia and eDreams, and confirms prices in Google Flights when a browser is available. Keeps three options: the cheapest, the most convenient, and the best one with your preferred airline.
4. **Hotels:** searches Booking.com and checks the best options against Tripadvisor reviews. For the Caribbean, it includes an all-inclusive option.
5. **Activities:** suggests three to five activities from Viator.
6. **Calendar and season:** checks date conflicts and warns about the Atlantic hurricane season (June to November).
7. **Result:** one comparison table with the total price for the whole group, pros, cons and links to buy.

## Installation

### Claude app (web, desktop)

1. Connect the required connectors listed above.
2. Download this repository and create a ZIP file of the `skills/travel-planner-latam` folder.
3. Upload the ZIP file as a custom skill. See [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### Claude Code

```
/plugin marketplace add jalcalaroot/claude-travel-planner-latam
/plugin install travel-planner-latam@claude-travel-planner-latam
```

The connectors must also be available in your Claude Code session.

## Make it yours

Open `skills/travel-planner-latam/SKILL.md` and fill in the **Traveler profile** section: home airport, preferred airlines, hotel style, and whether you travel with children. If you leave the placeholders, Claude asks only for what it needs.

Keep your personal copy private if it contains private details.

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
- [CHANGELOG.md](CHANGELOG.md): version history.

## License

MIT. See [LICENSE](LICENSE).

---

## Español

Una skill de Claude que compara vuelos, hoteles y actividades en varias fuentes a la vez, pensada para viajeros que salen de Latinoamérica.

### Por qué usar esta skill

Sin la skill, Claude puede buscar en sitios de viaje, pero el resultado depende de cómo le pidas. Puede usar una sola fuente, no comparar o no mirar reseñas. Con la skill:

- **Un pedido, una comparación completa.** Siempre revisa dos fuentes de vuelos, hoteles con reseñas y actividades, sin que tengas que pedir cada paso.
- **Mejores precios.** Compara la misma ruta en varias fuentes y te muestra diferencias que un solo sitio no muestra.
- **Menos hoteles malos.** Filtra los hoteles con reseñas de viajeros antes de mostrártelos.
- **Pensada para Latinoamérica.** Busca aerolíneas y conexiones de la región (Panamá, San Pablo, Bogotá, Lima) y te recuerda comparar opciones de pago locales, como las cuotas.
- **Para viajar en familia.** Tiene en cuenta las edades de los chicos, hoteles y actividades aptos para ellos y la temporada de huracanes del Caribe.
- **Segura.** Nunca reserva ni paga, y trata el contenido de las webs como datos, no como instrucciones.
- **Siempre el mismo formato.** Una tabla con el precio total para todo el grupo, pros, contras y links para comprar.

### Requisitos

Una skill contiene solo instrucciones: **no puede instalar conectores por vos.** Antes de usarla, conectá estos conectores desde el directorio de Claude (en Claude: Configuración, Conectores). Ninguno pide cuenta.

**Conectores necesarios**

| Conector | Para qué se necesita |
|---|---|
| **Expedia** | Fuente principal de vuelos, hoteles y paquetes de vuelo más hotel. Muy fuerte en Estados Unidos y el Caribe. |
| **eDreams** | Segunda fuente de vuelos. La skill compara la misma ruta contra Expedia para encontrar el mejor precio. |
| **Booking.com** | Fuente principal de hoteles, departamentos y casas. |
| **Tripadvisor** | Reseñas de viajeros. La skill las usa para descartar hoteles con quejas repetidas. |

Sin los conectores necesarios la skill igual funciona, pero la comparación es más débil. Te avisa cuáles faltan.

**Conectores y herramientas recomendados**

| Conector o herramienta | Para qué sirve |
|---|---|
| **Viator** | Actividades y excursiones en destino. Sin él, la respuesta no sugiere actividades. |
| **Claude in Chrome** | Permite abrir Google Flights y las webs de las aerolíneas en tu navegador para confirmar precios y ver el calendario de tarifas. |
| **Google Calendar** | Revisa conflictos con las fechas del viaje. Usa tu propia cuenta de Google. |

### Instalación

- **App de Claude:** conectá los conectores necesarios, comprimí la carpeta `skills/travel-planner-latam` en un ZIP y subila como skill propia.
- **Claude Code:** usá los dos comandos `/plugin` de la sección *Installation*. Los conectores también tienen que estar disponibles en tu sesión.

### Personalizala

Abrí `skills/travel-planner-latam/SKILL.md` y completá la sección **Traveler profile**: aeropuerto de salida, aerolíneas preferidas, tipo de hotel y si viajás con chicos. No publiques tu copia personal si tiene datos privados.

### Límites

Los precios cambian: confirmá el precio final en la web del vendedor antes de pagar. Confirmá visas y documentos en sitios oficiales. Este proyecto no está afiliado a Anthropic ni a ninguna aerolínea, hotel o agencia.
