# The World Today — Thursday 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/yanxiaoxv/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/yanxiaoxv/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026:
a big illustrated lead panel (Shenzhen at dusk — skyline, bay, the US,
Chinese and Russian flags) over a two-column layout of story cards,
each with its own small drawn scene, on a deep-navy page with a
dot-matrix world map in the masthead. Entry for make.fun's
`news-image-20261119` competition ($250, top 50 share it).

`main.py` (Python 3, standard library only) copies the image beside it
to `/output/entry.png`, after checking the payload's PNG signature and
size. The image itself was drawn procedurally in the build session
with PIL: fixed text, fixed geometry, no external assets, no network —
two runs write byte-identical files.

## The day, in six stories

1. **Shenzhen — a first joint declaration.** Donald Trump, Xi Jinping
   and Vladimir Putin held the first trilateral meeting of the three
   leaders at Kylin Villa in Shenzhen, on the sidelines of the APEC
   summit (about 1 hour 45 minutes, after a late start). They signed
   off on a four-point joint declaration: reform the United Nations,
   boost supplies of refined fuel, limit the reach of the International
   Criminal Court, and open a dialogue on reducing nuclear risks —
   "a nuclear war cannot be won and must never be fought". There was
   no deal on Ukraine or Iran and no new arms treaty. *(Xinhua and
   Kremlin readouts via AP; Al Jazeera live blog; USA Today,
   19 Nov 2026)*
2. **Iran says three tankers hit mines in Hormuz.** Tehran says three
   oil tankers struck naval mines east of the Strait of Hormuz and
   caught fire after ignoring warnings and sailing outside its
   designated channel; the UKMTO separately reports a tanker hit by a
   projectile off Khasab, Oman. Oil barely moved: Brent crude held
   near $92 a barrel as Gulf exports run close to pre-war levels.
   *(Reuters, 19 Nov 2026)*
3. **Anthropic debuts on Nasdaq.** The Claude maker priced its IPO at
   $83 a share, above the $70–$78 range, in an upsized deal; trading
   starts on Thursday in New York under the ticker ANT, at a reported
   valuation of about $1.4 trillion. *(Reuters via AI Morning Brief /
   BBC News, 19 Nov 2026)*
4. **World Court: Myanmar committed genocide.** The International
   Court of Justice in The Hague ruled on Thursday that Myanmar
   committed genocide against the Rohingya: the 2017 crackdown was
   carried out with the intention to destroy a substantial part of the
   Muslim minority. It is the first time the court has found a state
   responsible for genocide, seven years after Gambia filed the case;
   the court ordered Myanmar to allow the Rohingya's safe return and
   family reunification. *(CNA / AFP; The Guardian, 19 Nov 2026)*
5. **GTA VI rolls out worldwide.** After a 13-year wait, Grand Theft
   Auto VI unlocked region by region from midnight on 19 November,
   New Zealand first, returning players to Vice City in the fictional
   state of Leonida. Day-one estimates put sales at about 17.1 million
   copies and $1.65 billion (Sensor Tower), with a Metacritic score
   of 99. *(CNA / AFP; Reuters via Happy Gamer, 19 Nov 2026)*
6. **Also today.** Trump and Xi agreed in Shenzhen to extend the
   US–China trade truce, though neither side published its new terms
   *(Bloomberg / CNBC, 19 Nov 2026)*. The EU proposes a €45bn loan
   for Ukraine for 2027, to be repaid from future Russian war
   reparations *(Reuters, 18–19 Nov 2026)*. Van Gogh's *Chestnut
   Trees in Blossom* (1890) sells at Sotheby's for a record $190.4m
   after a Nazi-era ownership claim was settled *(WSJ / ARTnews,
   19 Nov 2026)*.

Final edition: compiled on the evening of 19 November 2026 (CST),
after the Shenzhen declaration, the Hague judgment and the GTA VI
launch numbers were all in.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — 1024x1024, 146,006 bytes
```

## License

MIT — see `LICENSE`.
