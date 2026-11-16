# Domain vs Subpath Decision — GTA 6 Answers Site

**Date:** November 16, 2026
**Decision deadline:** November 17 (1 day before launch)

---

## Options

### Option A: New Domain (gta6moneyguide.com)
Dedicated brandable domain for the GTA 6 money guide vertical.

### Option B: hms-site Subpath (hightower-marketing.com/gta6-money-guide/)
Adds the guides as a section under the existing HMS marketing site.

---

## Comparison

| Factor | Option A: New Domain | Option B: hms-site Subpath |
|---|---|---|
| **SEO start** | Fresh domain, zero authority | Inherits existing domain authority (GSC verified, ~38 pages indexed) |
| **Branding** | Clean, memorable, niche-specific | Diluted — hightower-marketing is a marketing agency, not gaming |
| **GEO/AI citation** | New domain may take longer to get cited | Existing domain authority helps AI trust |
| **Monetization** | Full freedom — ads, affiliate, sponsorship | Must align with hms-site brand; gaming affiliate may feel off-brand |
| **Topic mismatch** | None — gaming-focused | Marketing agency + gaming guide = confusing user intent |
| **Launch speed** | ~1-2 days (domain + DNS + deploy) | Can deploy immediately (staging already exists) |
| **Risk** | Domain cost + setup time | No additional cost; can be removed cleanly |
| **Netlify deploy** | New site/repo = new Netlify setup | Uses existing HMS deploy pipeline |
| **GSC verification** | Fresh submission | Already verified (sc-domain:hightower-marketing.com) |
| **Sitemap/IndexNow** | Fresh setup | Already wired |
| **If GTA 6 fails to generate sustained traffic** | Domain is stranded asset | Clean removal, no impact |
| **Content reuse** | Difficult to repurpose | Easy to repurpose if topic expands |
| **AdSense** | Fresh application needed | Already approved on hms-site (pub-4655953013932674) |
| **Plugin directory URL** | Clean plugin endpoint | Would need subpath anyway |

---

## Recommendation: Option A — New Domain

**Rationale:**

1. **Topic mismatch is the killer** — hightower-marketing.com is a B2B marketing agency. Adding "how to get rich in GTA 6" guides creates conflicting user intent signals. Visitors arriving at /gta6-money-guide/ see "AI marketing services" in the header and bounce.

2. **Brand dilution works both ways** — The GTA 6 guides dilute hms-site's professional brand, and hms-site's corporate brand reduces the gaming guides' perceived authority.

3. **Fresh domain risk is manageable** — The site is designed for a 6-12 month window (launch spike + online anticipation). If it works, the domain has resale value. If it doesn't, the domain cost (~$12/yr) is negligible.

4. **GEO doesn't care about domain age** — FAQPage JSON-LD + llms.txt are the primary signals for ChatGPT/Perplexity citation, not domain authority. FreeAcademy gets 25% of traffic from GPT without a legacy domain.

5. **AdSense can use separate account** — Or use existing publisher ID with a new site approval. The effort to re-apply is small.

### Chosen Domain: gta6moneyguide.com

- Clean, keyword-rich, memorable
- Low brand confusion risk
- Available for purchase (~$12/yr)
- Easy to pivot to other game money guides if GTA 6 works

---

## Implementation Plan

1. Blake approves domain choice
2. Buy gta6moneyguide.com (or alternative)
3. DNS: CNAME www to Netlify or Cloudflare Pages
4. Deploy staging build to site
5. Blake approves deployment to www
6. Add domain to Cloudflare (orange cloud)
7. Submit sitemap to Google (via GSC)
8. IndexNow submission for initial pages
9. Wire llms.txt at root

---

## Open Decision for Blake

- **Domain choice:** Propose gta6moneyguide.com — approve or suggest alternative
- **www deploy:** Staging build is complete — approve deployment to www.gta6moneyguide.com when ready
- **AdSense:** Use existing HMS publisher ID (pub-4655953013932674) with new site approval, or apply fresh?
- **Plugin directory:** Skip for now per feasibility report — approve?