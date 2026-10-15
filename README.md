# Boondock Math

The RV boondocking honesty tool. The gray tank ends more trips than
the weather, the battery's name counts amp-hours it will never give,
and the furnace counts its nights in bottles. Boondock Math turns the
tank, the bank and the bottles into the days and nights you actually
have.

- Live app: https://ilanis-agent.github.io/boondockmath/app.html
- Landing: https://ilanis-agent.github.io/boondockmath/

## What it does

1. **The tank truth** - gray gallons / (people x 4 gallons at the
   navy-shower norm, labeled) into days, with verdicts for an early
   weekend, a working week, and outlasting the fresh water.
2. **The battery truth** - bank amp-hours x usable percent (labeled
   norms: 50 lead-acid, 80 lithium) / the daily draw into honest
   nights.
3. **The bottle truth** - bottles x 12 furnace-hours each (labeled
   norm) / the furnace hours per night into honest nights of heat.

## Files

- `engine.js` - pure functions (`tankPlan`, `battPlan`, `propPlan`) plus renderers
- `app.html` - the app; `index.html` - the landing page
- `oracle.py` - independent Python mirror of the engine
- `test.js` + `expected.json` - 26 oracle cases, `node test.js` runs green

The norms are labeled; the dump station keeps the honest ledger.
