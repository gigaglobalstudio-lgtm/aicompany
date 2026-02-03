---
name: market-hunter-pro
description: Advanced sourcing agent integrating Search, NotebookLM, and Filesystem MCPs. Use for "deep sourcing", "market research automation", or "create sourcing report".
---

# Market Hunter Pro (MCP Enhanced)

## Workflow Overview
This skill orchestrates multiple MCP tools to perform deep market analysis and asset creation.

## Instructions

### Phase 1: Deep Research (Search MCP)
1. **Tool Call:** Use `brave_search` (or `google_search`) to find top 5 videos/articles for the user's keyword.
2. **Filter:** Focus on content created in 2024-2025.
3. **Extraction:** Identify key "Pain Points" and "Buying Factors".

### Phase 2: Knowledge Base Creation (NotebookLM MCP)
1. **Tool Call:** Use `notebook_create` to create a new notebook named "[Keyword] Analysis 2026".
2. **Data Entry:** Use `notebook_add_source` to feed the URLs found in Phase 1 into this notebook.
3. **Insight:** Ask the notebook to generate a "SWOT Analysis" based on the added sources.

### Phase 3: Visual Output (Filesystem & Slide MCP)
1. **Excel Report:**
   - Format the margin calculation data into CSV format.
   - **Tool Call:** Use `filesystem_write` to save it to `Output/[Keyword]_margin.csv`.
2. **Battle Slide Generation:**
   - Structure a comparison: Competitor (Villain) vs. Us (Hero).
   - **Tool Call:** Use `slide_create` (if available) or generate a detailed prompt for Gamma App.
   - **Style:** "Pokemon Battle Style" with stats for Price, Quality, and Delivery.

## Error Handling
- If `notebook_create` fails, create a local Markdown file summary instead.
- If MCP tools are offline, fallback to standard text analysis.
