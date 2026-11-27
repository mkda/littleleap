# LittleLeap Studios site

Public showcase for the LittleLeap Studios channel, served by GitHub Pages from `main`.

| Page | What it holds |
|---|---|
| `index.html` | Home: next story, latest stories, album, games, shop teaser, LittleLeap News text (kept for the Google app verification) |
| `watch.html` | Every story, story collection and Short (from `data/episodes.json`) |
| `listen.html` | The "Little Leap" album and its store links |
| `play.html` | Meadow Games (mkda/games) |
| `shop.html` | Shop products (coming soon; sales will run on an outside shop, not on Pages) |
| `parents.html` | About, AI use, safety, contact |
| `privacy.html` | Privacy policy (hand-written, keep at this address) |

## Adding a new video
1. Add an entry to `data/episodes.json` → `videos` (fields are described in its `_readme`).
2. For a story, put a 640×360 JPG thumbnail in `img/ep/` and point `thumb` at it.
3. Update `next` to the following planned story (or `null`).

No rebuild is needed for that. Change the page texts in `tools/build.py`, then run `python3 tools/build.py`.

The site makes no outside requests: fonts (Fredoka, SIL OFL, `fonts/OFL.txt`) and images are bundled, and videos open on YouTube.
