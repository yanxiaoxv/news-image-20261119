# The World Today — Thursday 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/yanxiaoxv/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/yanxiaoxv/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026,
at broadsheet density on a 1024x768 (4:3) page: a "Day in Numbers"
band, fifteen numbered story cards — each with a status/source tag
and its own small drawn scene — a dot world map keyed to the card
numbers ("Where It Happened"), and a one-line briefs section
("Also on 19 November").

`main.py` (Python 3, standard library only) copies the image beside
it to `/output/entry.png`, after checking the payload's PNG
signature and size. The image itself was drawn procedurally in the
build session with PIL: fixed text, fixed geometry, no external
assets, no network — two runs write byte-identical files.

## The day in numbers

- **$83** — Anthropic's IPO price per share, set above the range *(Reuters)*
- **17.1m** — GTA VI copies sold on day one, an estimate *(Sensor Tower)*
- **$190.4m** — Van Gogh's *Chestnut Trees in Blossom*, an auction record *(WSJ)*
- **€45bn** — the loan the EU proposes for Ukraine for 2027 *(Reuters)*
- **$92** — Brent crude per barrel, held near on Thursday *(Reuters)*
- **1 in 4** — children worldwide now living in conflict zones *(Save the Children)*

## The fifteen cards

1. **Shenzhen — a first joint declaration.** Trump, Xi and Putin,
   meeting at Kylin Villa on the sidelines of APEC, sign four points:
   UN reform, more fuel supplies, limits on the International
   Criminal Court, and a dialogue on reducing nuclear risks. No deal
   on Ukraine. *CONFIRMED — Xinhua / AP*
2. **Iran says 3 tankers hit mines in Hormuz.** Tehran says the ships
   ignored warnings and caught fire; the UKMTO reports another tanker
   hit by a projectile off Oman. *CLAIM — Iran navy / UKMTO, via Reuters*
3. **Israeli tanks cross the Yellow Line — then pull back.** The
   first ground raid past the Gaza truce line since October 2025 ends
   on Thursday; dozens fled, and the Salah al-Din road reopens.
   *CONFIRMED — Reuters / AFP*
4. **Crimean Bridge attacked for the third time in a week.** Traffic
   halts again after an overnight strike, Crimea's Russian-installed
   governor says. *CONFIRMED — Reuters*
5. **US and Venezuela restore military ties after 21 years.**
   Hegseth signs in Caracas: joint training and intelligence sharing,
   ten months after Maduro's capture. *CONFIRMED — Al Jazeera / AFP*
6. **World Court: Myanmar committed genocide.** The ICJ's first
   genocide verdict against a state: the 2017 crackdown was meant to
   destroy the Rohingya; safe return ordered. *CONFIRMED — CNA / AFP*
7. **Anthropic lists at $83 a share.** The IPO prices above the
   $70–$78 range; trading opens Thursday in New York as ANT, valued
   near $1.4tn. *CONFIRMED — Reuters*
8. **Trump and Xi extend the US–China trade truce.** Agreed at their
   bilateral before the trilateral talks; terms not published.
   *REPORTED — Bloomberg / CNBC*
9. **EU proposes a €45bn loan for Ukraine.** For 2027, repayable only
   once Russia pays war reparations. *PROPOSED — Reuters*
10. **Gulf oil flows near pre-war levels; LNG lags.** Crude shipments
    largely recover despite the tanker attacks; LNG via Hormuz runs
    at about a third of normal. *DATA — Reuters / Kpler*
11. **GTA VI: 17.1m copies and $1.65bn on day one.** A rolling
    midnight launch, New Zealand first, ends the 13-year wait;
    Metacritic 99. *ESTIMATE — Sensor Tower*
12. **Van Gogh sells for a record $190.4m.** *Chestnut Trees in
    Blossom* (1890) tops the artist's record at Sotheby's New York,
    after a Nazi-era ownership claim was settled.
    *CONFIRMED — WSJ / ARTnews*
13. **A record 1 in 4 children live in conflict zones.** Nearly a
    quarter of the world's children — the highest share ever
    recorded — now grow up amid war. *REPORT — Save the Children*
14. **Dust grains hint at ancient ice beyond Neptune.** Twelve
    stratospheric grains carry chemical signs of an ancient
    water-ice reservoir in the Kuiper Belt. *RESEARCH — NASA / Phys.org*
15. **New Zealand women book their World Cup place.** A 1–0 win over
    Papua New Guinea in the Oceania final: 25 goals scored, none
    conceded, on the way to Brazil 2027. *CONFIRMED — OFC / NZ Football*

## Also on 19 November

The image prints briefs 16–27: flooding in Florida (NBC) · IMF
forecasts 7.3% UAE growth (Khaleej Times) · Malaysia ends visa-free
entry for Indians from 2027 (Deccan Chronicle) · Wellington Test
day 1: NZ 243/5, Nicholls 113* (PTI) · NZ network traffic record
5.6 Tbps (Chorus) · SpaceX Dragon splashdown with ISS medical
samples (NASA) · Alcaraz MRI scan (Tennishead) · Lakshya Sen reaches
the BWF World Tour Finals (PTI) · KKR stake sale values the IPL
team near $1.78bn · England win the ODI series in Australia
(BBC Sport) · Bancroft reopens Sandpapergate (ABC) · PlayStation
sign-in problems on GTA VI launch night (Happy Gamer).

For the record, the day's remaining briefs — compiled but not
printed on the 4:3 page, so that no text had to shrink: Cyclone
Akvan nears Odisha (IMD) · Ras Al Khaimah named top expat city
(Khaleej Times) · Marcos meets Xi at APEC (ONE News) · India women
beat Japan 3–1 in hockey (Sportstar) · violence and arson in
Bangladesh (Deccan Chronicle) · Delhi-NCR schools reopen · Muslims
projected largest faith group by 2035 (Pew) · Zverev into ATP
Finals semi-finals (ATP) · Ukraine strikes two Russian refineries
(UA General Staff) · APEC closing statement (AP) · Eisenkot bids to
form an Israeli government (AFP) · Take-Two stock +6% premarket
(CNBC).

Final edition: compiled on the night of 19 November 2026 (CST),
after the day's main events had concluded.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — 1024x768, 200,215 bytes
```

## License

MIT — see `LICENSE`.
