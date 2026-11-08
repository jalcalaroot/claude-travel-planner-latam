# Install guide: Claude Code

This guide installs the `travel-planner-latam` skill in Claude Code and connects the travel connectors it uses.

> [Guía en español](#guía-en-español)

## Before you start

- Claude Code is installed, and you are logged in with your **Claude account** (Pro, Max, Team or Enterprise plan).
- You use the same Claude account on [claude.ai](https://claude.ai).

## Important: install the connectors first

A plugin or a skill **cannot install connectors for you.** The travel connectors are added once to your Claude account. After that, Claude Code reads them from your account and they are available in your sessions.

## Step 1: Add the travel connectors

1. Open [claude.ai/customize/connectors](https://claude.ai/customize/connectors).
2. Browse the connector directory and add each of these connectors. None of them requires an account with the travel company.

   | Connector | Needed | Why |
   |---|---|---|
   | Expedia | Required | Flights and hotels |
   | eDreams | Required | Second flight source, to compare prices |
   | Booking.com | Required | Hotels, apartments and homes |
   | Tripadvisor | Required | Reviews, to discard bad hotels |
   | Viator | Recommended | Activities at the destination |

## Step 2: Check the connectors in Claude Code

1. Start Claude Code.
2. Run `/mcp`.
3. Confirm that the connectors appear in the list, with names that start with `claude.ai`, for example `claude.ai Expedia`.

If a connector does not appear:

- Make sure that you are logged in with the same Claude account. Run `/login` if needed.
- Check that the connector is not disabled for the current project in `/mcp`.
- If a connector asks for authorization again, reconnect it at [claude.ai/customize/connectors](https://claude.ai/customize/connectors).

## Step 3: Install the plugin

In Claude Code, run:

```
/plugin marketplace add jalcalaroot/claude-travel-planner-latam
/plugin install travel-planner-latam@claude-travel-planner-latam
```

You can also run the same commands from your terminal:

```bash
claude plugin marketplace add jalcalaroot/claude-travel-planner-latam
claude plugin install travel-planner-latam@claude-travel-planner-latam
```

## Step 4: Check the installation

1. Run `/plugin` and confirm that `travel-planner-latam` is installed and enabled.
2. Restart Claude Code if the skill does not appear in the new session.

## Step 5: Try it

Ask for a trip, for example:

> Use the travel-planner-latam skill. We are 2 adults and 1 child aged 7. We fly from Sao Paulo (GRU) for one week in March. We want a beach in the Caribbean with a total budget of USD 4,000.

Claude first tells you if a connector is missing, then compares flights, hotels and activities.

## Update and uninstall

```
/plugin marketplace update claude-travel-planner-latam
/plugin uninstall travel-planner-latam@claude-travel-planner-latam
```

## Optional: personalize the skill

To save your home airport, preferred airlines and travel style:

1. Copy the folder `skills/travel-planner-latam` to `~/.claude/skills/my-travel-planner`.
2. In the copied `SKILL.md`, change `name: travel-planner-latam` to `name: my-travel-planner`, so that you can tell your copy apart from the plugin.
3. Fill in the **Traveler profile** section.
4. Uninstall the plugin if you only want to use your personal copy, and keep that copy private.

---

## Guía en español

### Antes de empezar

- Tenés Claude Code instalado y con sesión iniciada con tu **cuenta de Claude** (plan Pro, Max, Team o Enterprise).
- Usás la misma cuenta en [claude.ai](https://claude.ai).

### Importante: primero los conectores

Un plugin o una skill **no puede instalar conectores por vos.** Los conectores de viaje se agregan una sola vez a tu cuenta de Claude, y después Claude Code los toma de tu cuenta.

### Paso 1: Agregar los conectores

Entrá a [claude.ai/customize/connectors](https://claude.ai/customize/connectors) y agregá **Expedia, eDreams, Booking.com y Tripadvisor** (necesarios) y **Viator** (recomendado). Ninguno pide cuenta en la empresa de viajes.

### Paso 2: Verificarlos en Claude Code

Abrí Claude Code, corré `/mcp` y confirmá que aparecen con nombres que empiezan con `claude.ai`, por ejemplo `claude.ai Expedia`. Si falta alguno, revisá que estés con la misma cuenta (`/login`), que no esté deshabilitado en `/mcp`, o volvé a conectarlo en claude.ai.

### Paso 3: Instalar el plugin

```
/plugin marketplace add jalcalaroot/claude-travel-planner-latam
/plugin install travel-planner-latam@claude-travel-planner-latam
```

### Paso 4: Verificar y probar

Corré `/plugin` para confirmar que está instalado y habilitado. Después pedí un viaje, por ejemplo:

> Usá la skill travel-planner-latam. Somos 2 adultos y un chico de 7 años, salimos de Ezeiza (EZE) una semana en marzo, queremos playa en el Caribe con USD 4.000 en total.

### Personalizarla (opcional)

Copiá la carpeta `skills/travel-planner-latam` a `~/.claude/skills/my-travel-planner`, cambiá en el `SKILL.md` copiado `name: travel-planner-latam` por `name: my-travel-planner` para distinguirla del plugin, completá la sección **Traveler profile** y mantené esa copia privada. Si solo vas a usar tu copia, desinstalá el plugin.
