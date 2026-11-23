[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/aurorabelle788/news-image-20261123-v1/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/aurorabelle788/news-image-20261123-v1/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# news-image-20261123 v1 — The World, Monday 23 November 2026

Entry for the make.fun bounty [Sum up 23 November's world news in one image](https://make.fun/bounty/news-image-20261123): a program that writes one image of the day's news to `/output/entry.png`, judged pairwise by an AI judge. The 50 best share $100.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win. Sign up with my referral code `azvv97zj`: https://make.fun/r/azvv97zj

## The image

A dated news front page — **THE WORLD, MONDAY 23 NOVEMBER 2026** — with the day's 15 most consequential stories, each with its own matching picture, a short headline, and its source printed directly underneath:

1. COP31 collapse sparks blame game — Reuters
2. Ukraine drones sink Russian ship off Libya — AP
3. Russian strikes kill 14 in Ukraine — AP
4. Democrats clinch 258 House seats — AP
5. Army invokes emergency powers in Iowa — Reuters
6. Indonesia confirms 24 dead in factory fire — Reuters
7. Wall Street rebounds after AI rout — Reuters
8. Hedge funds' worst week since April 2025 — Reuters
9. Russia eyes nuclear satellite launch — WDR/NDR/SZ
10. Houthis claim strike on Rabigh refinery — Dubai Standard
11. Indonesia to name VP candidates today — Reuters
12. Europe splits: France down, Germany up — Reuters
13. Kremlin says new Ukraine talks soon — AFP
14. Oil prices fall as AI selloff spreads — Reuters
15. Nvidia's China business under threat — Reuters

Every story happened on, or was first reported on, 23 November 2026. The full story list with one-line summaries is in `news-image-20261123-stories.md` (kept in the workspace, not the repo).

## How it works

`main.py` (standard library only — it imports just `os` and `shutil`) copies the pre-built `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The image is 1024×1024, under 1 MiB, and deterministic: two runs write identical bytes.

## Run it locally

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.png` is then byte for byte this directory's `entry.png`.
