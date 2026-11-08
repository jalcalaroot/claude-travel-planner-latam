# Install guide: Claude app

This is the recommended way to use `travel-planner-latam`. Trip planning is a conversation, so the Claude app (web, desktop or mobile) is the best place for it.

> [Guía en español](#guía-en-español)

## Before you start

- You have a paid Claude plan (Pro, Max, Team or Enterprise).
- You use the Claude app on the web ([claude.ai](https://claude.ai)) or the desktop app. You can use the skill on mobile after you install it.

## Step 1: Add the travel connectors

A plugin or a skill **cannot add connectors for you.** Add them once to your Claude account:

1. Open [claude.ai/customize/connectors](https://claude.ai/customize/connectors).
2. Browse the connector directory and add each connector. The five travel connectors do not require an account with the travel company.

   | Connector | Needed | Why |
   |---|---|---|
   | Expedia | Required | Flights and hotels |
   | eDreams | Required | Second flight source, to compare prices |
   | Booking.com | Required | Hotels, apartments and homes |
   | Tripadvisor | Required | Reviews, to discard bad hotels |
   | Viator | Recommended | Activities at the destination |

3. Optional: install **Claude in Chrome** so that Claude can read Google Flights and airline websites, and add the **Google Calendar** connector to check date conflicts.

## Step 2: Add this repository as a marketplace

1. In the Claude app, open **Customize** in the sidebar, then **Plugins**.
2. Select **Add marketplace**.
3. Enter `jalcalaroot/claude-travel-planner-latam` (or `https://github.com/jalcalaroot/claude-travel-planner-latam`).

## Step 3: Install the plugin

1. The plugin **travel-planner-latam** appears in the list of plugins.
2. Select it and click **Install**.
3. Open the installed plugin and check that the skill **travel-planner-latam** is enabled.

## Step 4: Try it

Start a new conversation and ask for a trip, for example:

> We are 2 adults and 2 children aged 6 and 9. We fly from Ezeiza (EZE) for one week in January. We want a beach in the Caribbean, all inclusive, one stop at most, and a total budget of USD 6,000.

The skill starts on its own when you ask for a trip. You can also name it: "Use the travel-planner-latam skill".

## Update and uninstall

- **Update:** in **Customize, Plugins**, select **Update** on the marketplace.
- **Uninstall:** open the plugin in **Customize, Plugins** and click **Uninstall**.

## Alternative: upload the skill as a file

If you cannot add a marketplace (for example, your organization does not allow it):

1. Download this repository as a ZIP file and extract it.
2. Create a ZIP file of the `skills/travel-planner-latam` folder.
3. Upload it as a custom skill. See [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

With this method, you do not get updates. Repeat the upload for each new version.

## Optional: personalize the skill

To save your home airport, preferred airlines and travel style, use the file method above with your own copy: fill in the **Traveler profile** section of `SKILL.md` before you create the ZIP file, and change `name:` to `my-travel-planner` so that you can tell it apart from the plugin. Keep that copy private.

## Troubleshooting

- **The skill does not start:** check in **Customize, Plugins** (or **Customize, Skills**) that it is enabled, then start a new conversation.
- **Claude says a connector is missing:** add it at [claude.ai/customize/connectors](https://claude.ai/customize/connectors) and start a new conversation.
- **There is no Add marketplace option:** your plan or your organization may not allow it. Use the file method.

---

## Guía en español

Es la forma recomendada de usar la skill: planificar un viaje es una conversación, y la app de Claude (web, escritorio o celular) es el mejor lugar.

### Antes de empezar

- Tenés un plan pago de Claude (Pro, Max, Team o Enterprise).
- Usás Claude en la web ([claude.ai](https://claude.ai)) o en la app de escritorio. Después de instalarla, también la podés usar en el celular.

### Paso 1: Agregar los conectores de viaje

Un plugin o una skill **no puede agregar conectores por vos.** Agregalos una sola vez en [claude.ai/customize/connectors](https://claude.ai/customize/connectors): **Expedia, eDreams, Booking.com y Tripadvisor** (necesarios) y **Viator** (recomendado). Ninguno pide cuenta en la empresa de viajes. Opcional: **Claude in Chrome**, para leer Google Flights y las webs de las aerolíneas, y **Google Calendar**, para revisar conflictos de fechas.

### Paso 2: Agregar este repositorio como marketplace

En la app, abrí **Customize** en la barra lateral, después **Plugins**, elegí **Add marketplace** y escribí `jalcalaroot/claude-travel-planner-latam`.

### Paso 3: Instalar el plugin

Elegí **travel-planner-latam** en la lista, tocá **Install** y verificá que la skill esté habilitada.

### Paso 4: Probarla

Abrí una conversación nueva y pedí un viaje, por ejemplo:

> Somos 2 adultos y 2 chicos de 6 y 9 años. Salimos de Ezeiza una semana en enero, queremos playa en el Caribe, all inclusive, como máximo una escala y USD 6.000 en total.

La skill se activa sola cuando pedís un viaje. También la podés nombrar: "Usá la skill travel-planner-latam".

### Actualizar y desinstalar

- **Actualizar:** en **Customize, Plugins**, tocá **Update** en el marketplace.
- **Desinstalar:** abrí el plugin en **Customize, Plugins** y tocá **Uninstall**.

### Alternativa: subir la skill como archivo

Si no podés agregar un marketplace, descargá el repositorio, comprimí la carpeta `skills/travel-planner-latam` en un ZIP y subila como skill propia. Con este método no recibís actualizaciones.

### Personalizarla (opcional)

Usá el método del archivo con tu propia copia: completá la sección **Traveler profile** del `SKILL.md`, cambiá `name:` por `my-travel-planner` para distinguirla del plugin y mantené esa copia privada.

### Solución de problemas

- **La skill no se activa:** verificá en **Customize, Plugins** (o **Customize, Skills**) que esté habilitada y abrí una conversación nueva.
- **Claude dice que falta un conector:** agregalo en [claude.ai/customize/connectors](https://claude.ai/customize/connectors) y abrí una conversación nueva.
- **No aparece Add marketplace:** tu plan o tu organización puede no permitirlo. Usá el método del archivo.
