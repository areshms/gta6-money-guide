# OpenAI Plugin Directory Feasibility Report

**Date:** November 16, 2026
**Context:** GTA 6 "own the answers" GEO hub — evaluating whether to build a ChatGPT plugin/app

---

## 1. Current State of the Directory

### Renamed July 2026
The ChatGPT **App Directory** was renamed to the **Plugin Directory** effective July 9, 2026 (per ChatGPT release notes). Existing apps were auto-packaged into plugins. The Plugin Directory is now the primary discovery surface across ChatGPT, Codex, and ChatGPT Work.

### What You Submit
- A ZIP package containing a `plugin.json` manifest (Agent Plugins format) or `.codex-plugin/plugin.json` (Codex format)
- Optionally: MCP server configuration (`.mcp.json`), skills (`skills/` directory), and UI components
- The ZIP goes through automated validation, then human review for MCP-connected plugins

### Key Requirements (direct from docs)
- **Verified identity** — individual or business verification in organization settings
- **MCP server** — if your plugin connects to an external data source (like our guide site), it needs a stable HTTPS endpoint with domain verification
- **Test cases** — 5 positive, 3 negative for MCP plugins
- **Demo recording** — video walkthrough URL
- **Privacy/terms/support URLs** — all required for MCP review
- **No digital goods commerce** — plugins may only sell physical goods currently
- **Skills-only plugins** — no MCP server possible, just reusable instructions/skills
- **Desktop-only submission** — available for local MCP servers

### Ranking/Discovery Signals
OpenAI mentions: "Plugins that demonstrate strong real-world utility and high user satisfaction may be eligible for enhanced distribution opportunities, such as directory placement or proactive suggestions."

No public ranking algorithm. Signals inferred:
- User satisfaction / engagement metrics (OpenAI-owned, not shared)
- Relevance to conversation context (OpenAI's systems may surface plugins contextually)
- @mention discovery (user must type @pluginname)
- Category browsing

**VERIFIED:** No public API for ranking data. No way to buy placement. No keyword targeting.

---

## 2. Feasibility for a GTA 6 Guide/Walkthrough App

### What Would Our Plugin Do?
- Connect ChatGPT to gta6moneyguide.com content
- Answer "how to make money in GTA 6" questions by fetching our guides
- Provide structured answers from FAQPage JSON-LD

### Requirements We'd Need to Meet
| Requirement | Status | Notes |
|---|---|---|
| Stable HTTPS endpoint | ✅ We have it | Deployed site or staging |
| Domain verification | ✅ Possible | `/.well-known/openai-apps-challenge` |
| Privacy policy URL | ✅ Buildable | Can be created |
| Terms of service URL | ✅ Buildable | Standard terms |
| Support contact | ✅ Possible | Could offer |
| 5 positive test cases | ⚠ Doable | "How to make money fast in GTA 6" etc. |
| 3 negative test cases | ⚠ Doable | "Buy me a car" etc. (plugin should not act) |
| Demo recording | ⚠ Effort | Need to record walkthrough |
| MCP server development | ❌ Significant effort | Need to build + host an MCP server |
| Review queue wait | ❌ Unknown | No public SLA for review times |
| No digital goods restriction | ✅ Fine | We're providing information, not selling |

### Estimated Dev Time
- MCP server build + test: 1-2 weeks
- Plugin package + metadata: 2-3 days
- Review materials (test cases, demo): 3-5 days
- Domain verification + auth: 1-2 days
- **Total: ~3-4 weeks** to submission

### Current Community Sentiment (from forums)
- Developers report slow review cycles (weeks to months)
- "Approved app needs urgent fixes" threads on community.openai.com
- Rejection is common for vague descriptions or incomplete test cases
- MCP server requirements (scan, tools, hints) add friction

---

## 3. Recommendation: HOLD — Build Site First, Revisit After Traffic

**Verdict: NOT WORTH BUILDING NOW.** Here's why:

1. **Timeline mismatch** — 3-4 weeks to build + unknown review queue. GTA 6 launches in 3 days. The plugin would arrive weeks after launch, missing the peak search wave.

2. **OpenAI ranking is opaque** — No keyword targeting, no SEO-style optimization. Even if the plugin is approved, there's no guarantee of visibility. Users must know to @mention it.

3. **Traffic from organic search + ChatGPT Search is already proven** — Sites like FreeAcademy get 25% of traffic from GPT without a plugin. Our FAQPage JSON-LD + llms.txt strategy captures this without the submission overhead.

4. **MCP server requirement adds complexity** — A guide/walkthrough plugin needs a live MCP server with domain verification, auth, test credentials, and ongoing maintenance. This is real engineering debt for uncertain return.

5. **Commerce restriction limits monetization** — Even with a plugin, we can't sell guides or subscriptions through it. The same traffic on our own site can be monetized with ads, affiliate links, and sponsorships.

### When to Reconsider
- If our site reaches 10K+ monthly visitors (proving demand)
- If OpenAI releases plugin analytics or ranking data
- If walkthrough/guide plugins are featured in the directory
- When GTA 6 Online launches (Q1 2027) — second wave of search demand

### What to Do Instead
1. ✅ **Build the site** (this project) with FAQPage JSON-LD + llms.txt — free GEO surface on ChatGPT Search
2. Deploy and index via IndexNow for Google discovery
3. Monitor organic + AI referral traffic for 30 days
4. Only build plugin if traffic proves the demand model

---

## 4. Key Unknowns (Marked)

| Unknown | Impact |
|---|---|
| **Review queue time** for new MCP plugins | Could be 2-8 weeks |
| **Plugin ranking algorithm** — any detail | We can't optimize for placement |
| **Whether guide/walkthrough plugins are viable category** | No data on existing similar plugins |
| **Whether OpenAI prioritizes certain plugin types** | No public documentation |
| **If walkthrough data-source plugins violate any policy** (unofficial fan content) | Need to verify — fan guides are usually fine but MCP serving external content may have different rules |