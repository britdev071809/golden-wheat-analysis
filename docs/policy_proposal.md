# Supply Management Program for Golden Wheat Market

## Problem Statement

The Golden Wheat market has experienced persistent oversupply over the last decade, driven by technological improvements, favorable weather patterns, and expanded acreage. This oversupply has led to chronically low market prices, often below the cost of production for small‑scale farmers. The result is a steady decline in farm profitability, increasing debt loads, and the exit of family‑scale operations from the industry. Without intervention, the long‑term viability of the wheat‑producing sector is at risk.

## Proposed Solution

We propose a voluntary set‑aside program that is activated only when the market exhibits both excessive production and depressed prices. Using a dual‑condition trigger ensures that government intervention occurs precisely when supply‑side adjustments are most needed.

**Trigger criteria:**
1. **Production threshold:** Annual production exceeds the 5‑year moving average by more than 3%.
2. **Price threshold:** The annual average price falls below the 10‑year moving average price.

When both conditions are met in a given crop year, the program invites producers to enroll a portion of their base acreage in a temporary set‑aside. Participating farmers receive a per‑hectare payment that compensates for the forgone revenue, while the overall supply reduction helps lift prices back toward the long‑term average.

## Impact Analysis

Based on the revised oversupply analysis, the program would be triggered in approximately 8 of the last 20 years. For those years, a production reduction of 5–7 % relative to the moving‑average trend is sufficient to raise prices above the 10‑year average. Translated into acreage, this corresponds to a **set‑aside of 6 % of base acreage** in triggered years. Model simulations indicate that this level of supply management would raise farm‑gate prices by an estimated 8–12 % in the following marketing year, restoring profitability for the majority of small‑ and medium‑scale operations while adding only a modest fiscal burden (estimated at 0.2 % of annual agricultural GDP).

## Implementation

1. **Program trigger:** The dual‑condition oversupply indicator will be calculated each year by the Department of Agricultural Statistics using the methodology in `src/analyze_supply.py`. A public announcement of a triggered year will be made by March 1, before spring planting decisions are finalized.

2. **Enrollment:** Within 30 days of the trigger announcement, producers may enroll eligible acreage through their local Farm Service Agency office. Enrollment will be capped at 6 % of each farm’s base acreage to match the overall supply‑reduction target.

3. **Compensation:** Participants will receive a per‑hectare payment equal to 80 % of the county‑level expected revenue for wheat, paid in two installments (50 % upon verification of set‑aside, 50 % after harvest season).

4. **Monitoring and evaluation:** Annual audits will verify that enrolled land remains fallow or is used for approved non‑commodity cover crops. Price and production data will be reviewed each year to confirm that the program is achieving its intended market‑stabilization effect.

5. **Sunset provision:** The program will be automatically reviewed every five years; if the oversupply trigger is not activated for three consecutive reviews, the program will be placed in a standby status until needed again.