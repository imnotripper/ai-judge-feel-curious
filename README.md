[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/imnotripper/ai-judge-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/imnotripper/ai-judge-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

# ai-judge-feel-curious

Entry for the [make.fun bounty "Make the AI judge feel curious"](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311): one short text, written to leave the reader curious — a small observed moment that does not explain itself.

`main.py` (Python 3.13, stdlib only, no network, deterministic) writes the text to `<OUTPUT_DIR>/entry.txt` (default `/output`), atomically via a temp file + `os.replace`.

Run locally:

```sh
OUTPUT_DIR=/tmp/curious-out python3 main.py
cat /tmp/curious-out/entry.txt
```
