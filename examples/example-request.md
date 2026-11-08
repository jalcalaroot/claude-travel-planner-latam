# Example request

This example shows how to ask for a trip. The traveler data is fictional.

## Request (Spanish)

> Usá la skill travel-planner-latam. Somos 2 adultos y 2 chicos de 6 y 9 años. Salimos de Ezeiza (EZE) una semana entre el 10 y el 31 de enero. Queremos playa en el Caribe, presupuesto de USD 6.000 en total, como máximo una escala y hotel all inclusive con piscina para chicos.

## Request (English)

> Use the travel-planner-latam skill. We are 2 adults and 2 children aged 6 and 9. We fly from Ezeiza (EZE) for one week between January 10 and January 31. We want a beach in the Caribbean, a total budget of USD 6,000, one stop at most, and an all-inclusive hotel with a pool for children.

## What Claude returns

- A short list of questions only if something important is missing.
- A comparison table like this one (values are placeholders, not real prices):

| Option | Flight | Hotel | Estimated total | Pros | Cons | Links |
|---|---|---|---|---|---|---|
| Cheapest | `<airline, stops, times>` | `<hotel>` | `<USD ...>` | `<...>` | `<...>` | `<...>` |
| Most convenient | `<...>` | `<...>` | `<USD ...>` | `<...>` | `<...>` | `<...>` |
| Preferred airline | `<...>` | `<...>` | `<USD ...>` | `<...>` | `<...>` | `<...>` |

- Three to five activities suitable for children.
- A warning if the dates fall in the hurricane season.
- Reminders to compare local installments and to confirm entry requirements on official websites.
