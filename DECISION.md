# Domain vs Subpath Decision — GTA 6 Answers Site

**Date:** November 16, 2026
**Decision applied:** Blake approved purchase of new domain

---

## Chosen Domain

**Registered:** gta6-moneyguide.com  
(Note: gta6moneyguide.com was already taken, so the hyphenated version was registered instead at $11.81/yr)

---

## Hosting

**Host:** Vercel (free static hosting tier)
**GitHub repo:** https://github.com/areshms/gta6-money-guide
**Staging build:** /Users/ares.hmsgmail.com/projects/gta6-answers/staging/

---

## DNS

- **Root (@) A record** → `76.76.21.21` (Vercel)
- **WWW CNAME** → `cname.vercel-dns.com` (Vercel)

**Status:** DNS records ready to apply at Porkbun after domain registration completes.

---

## Implementation Plan

1. ~~Blake approves domain choice~~
2. **PENDING: Phone verification** — Porkbun account needs phone verification (SMS/call code sent to +1 ***52). Blake must provide the code.
3. Register gta6-moneyguide.com via Porkbun API
4. Set DNS A/CNAME records via Porkbun DNS API
5. Import repo to Vercel (or CLI deploy)
6. Verify live: landing 200, llms.txt, sitemap.xml
7. Wire GSC (OPEN — needs interactive Google login)

---

## Open Items for Blake

- **Phone verification code** — SMS and call sent to Porkbun account phone. Texted code between 11:21-11:31 AM EST, calling now.
- **GSC** — Needs interactive Google login to create domain property. I cannot log into Google.
- **AdSense** — Use existing HMS publisher ID with new site approval, or apply fresh?