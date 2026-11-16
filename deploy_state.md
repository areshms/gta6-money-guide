# Deploy State — GTA 6 Money Guide

**Date:** November 16, 2026
**Agent:** Prime (HMS LLC)
**Domain:** gta6-moneyguide.com (hyphenated — gta6moneyguide.com was taken)

---

## ✅ Completed

### Domain Research
- [x] Porkbun API credentials verified (ping SUCCESS, account: Areshms)
- [x] Account has `civicrecord.news` (1 existing domain)
- [x] Checked: gta6moneyguide.com → **taken** (not available)
- [x] Best available alternative: **gta6-moneyguide.com** → available, $11.81/yr

### Build
- [x] `build.py` updated to use `https://gta6-moneyguide.com` as base URL
- [x] Build verified PASS (55 questions, 10 pages, FAQPage JSON-LD on all pages)
- [x] sitemap.xml generated with all 10 URLs
- [x] llms.txt generated with all page links
- [x] Staging directory: `/Users/ares.hmsgmail.com/projects/gta6-answers/staging/`

### GitHub & Vercel Prep
- [x] Git repo initialized: `areshms/gta6-money-guide`
- [x] Repo pushed to GitHub: https://github.com/areshms/gta6-money-guide
- [x] `vercel.json` added (cleanUrls, trailingSlash)
- [x] **Not yet imported to Vercel** — needs a browser/UI step or CLI deploy after domain is live

### DNS Plan (ready to apply)
- Root @ A → `76.76.21.21` (Vercel)
- WWW CNAME → `cname.vercel-dns.com`
- Manage via Porkbun DNS API

---

## ❌ Blocked

### Domain Registration — BLOCKED

Porkbun account requires **phone verification** before domain registration.

**What happened:**
1. Sent SMS code to +1 ***52 (phone on Porkbun account) — 11:21 AM EST
2. Sent phone call to same number — 11:31 AM EST
3. Cannot verify without the code received by the account holder

**Resolution needed:** Blake (or person with access to Porkbun account's phone) provides the verification code. API call:
```bash
curl -X POST https://api.porkbun.com/api/json/v3/account/verifyPhone/confirm \
  -H "Content-Type: application/json" \
  -d '{"apikey":"...","secretapikey":"...","code":"<CODE>"}'
```
Then retry domain create. Code expires in ~10 minutes from the send/call.

---

## PENDING After Domain Registration

Once phone is verified and domain registered:

### Step 1: Set DNS Records (via Porkbun API)
```bash
# A record for root
curl -X POST https://api.porkbun.com/api/json/v3/dns/create/gta6-moneyguide.com \
  -H "Content-Type: application/json" \
  -d '{"apikey":"...","secretapikey":"...","type":"A","name":"","content":"76.76.21.21","ttl":"600"}'

# CNAME for www
curl -X POST https://api.porkbun.com/api/json/v3/dns/create/gta6-moneyguide.com \
  -H "Content-Type: application/json" \
  -d '{"apikey":"...","secretapikey":"...","type":"CNAME","name":"www","content":"cname.vercel-dns.com","ttl":"600"}'
```

### Step 2: Deploy to Vercel
```bash
# Option A: Vercel CLI (if authenticated)
cd /Users/ares.hmsgmail.com/projects/gta6-answers
vercel --prod --yes

# Option B: Web dashboard (preferred for reliability)
# Go to https://vercel.com/new, import areshms/gta6-money-guide
# Framework: Other, Root Directory: staging/
```

### Step 3: Attach Custom Domain
- In Vercel dashboard: Project → Settings → Domains → Add `gta6-moneyguide.com`

### Step 4: Verify
```bash
dig +short gta6-moneyguide.com A      # Expect: 76.76.21.21
curl -sI https://gta6-moneyguide.com   # Expect: 200 + Vercel server header
curl -s https://gta6-moneyguide.com/llms.txt | head -3
curl -s https://gta6-moneyguide.com/sitemap.xml | head -3
curl -s https://gta6-moneyguide.com/how-to-make-money-fast-gta-6/ | grep -c FAQPage
```

---

## OPEN

### Google Search Console
- **Status: OPEN** — Requires interactive Google login to create `sc-domain:gta6-moneyguide.com` property
- Cannot be done programmatically (no GSC service account credentials found)
- Blake must do this manually via https://search.google.com/search-console

### AdSense
- DECISION.md notes use existing HMS publisher ID (pub-4655953013932674) with new site approval
- Or apply fresh for GTA gaming niche
- Needs Blake's decision

---

## Files Created/Modified

| File | Change |
|------|--------|
| `/Users/ares.hmsgmail.com/projects/gta6-answers/build.py` | Updated base_url to `gta6-moneyguide.com` + added Optional links to llms.txt |
| `/Users/ares.hmsgmail.com/projects/gta6-answers/vercel.json` | Created for Vercel clean URL deployment |
| `/Users/ares.hmsgmail.com/projects/gta6-answers/DECISION.md` | Updated with chosen domain, hosting plan, pending items |
| `/Users/ares.hmsgmail.com/projects/gta6-answers/deploy_state.md` | This file |