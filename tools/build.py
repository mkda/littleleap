#!/usr/bin/env python3
"""Builds the static pages of the LittleLeap Studios site from one shared header and footer.

Run from the repo root:  python3 tools/build.py
Video lists are not built here: site.js reads data/episodes.json in the browser, so a new
episode only needs a new entry in that file (and a thumbnail in img/ep/). privacy.html is
hand-written and not touched by this script.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHANNEL = "https://www.youtube.com/@Little-Leap-Studios"
ALBUM = {
    "YouTube Music": "https://music.youtube.com/playlist?list=OLAK5uy_lAPZxpzq42qz_niKa5uN-WCKtWJCeMWag",
    "Spotify": "https://open.spotify.com/album/4PjG8Ojt5KI5LFeBbY4HzU",
    "Apple Music": "https://music.apple.com/us/album/little-leap/6835114843",
    "All stores": "https://distrokid.com/hyperfollow/mkda/little-leap",
}
CONTACT = "uxtestsmkda@gmail.com"

NAV = [("index.html", "Home"), ("watch.html", "Watch"), ("listen.html", "Listen"),
       ("play.html", "Play"), ("shop.html", "Shop"), ("parents.html", "Parents")]


def page(file, title, description, body, scripts=False):
    cur = ' aria-current="page"'
    nav = "".join(
        f'<a href="{href}"{cur if href == file else ""}>{name}</a>' for href, name in NAV)
    js = '\n<script src="site.js" defer></script>' if scripts else ""
    full_title = "LittleLeap Studios" if file == "index.html" else f"{title} · LittleLeap Studios"
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#dff1fa">
<link rel="icon" type="image/png" href="img/medallion.png">
<link rel="stylesheet" href="style.css">{js}
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html"><img src="img/logo.png" alt="LittleLeap Studios" width="115" height="40"></a>
  <nav class="nav" aria-label="Main">{nav}</nav>
</div></header>
<main>
{body.strip()}
</main>
<footer class="site"><div class="wrap">
  <span>© LittleLeap Studios</span>
  <a href="parents.html">For parents</a>
  <a href="privacy.html">Privacy policy</a>
  <a href="mailto:{CONTACT}">{CONTACT}</a>
  <a href="{CHANNEL}" target="_blank" rel="noopener">YouTube</a>
</div></footer>
</body>
</html>
"""
    (ROOT / file).write_text(html, encoding="utf-8")
    print("wrote", file)


def album_buttons():
    return "".join(
        f'<a class="btn{"" if i == 0 else " ghost"}" href="{url}" target="_blank" rel="noopener">{name}</a>'
        for i, (name, url) in enumerate(ALBUM.items()))


# ---------------------------------------------------------------- Home
page("index.html", "Home",
     "Gentle cartoon stories for children aged 3 to 7: classic public-domain tales retold with Zippy, Tomo and their friends from the Big Meadow.",
     f"""
<section class="hero"><div class="wrap">
  <div>
    <h1>Gentle stories from the Big Meadow</h1>
    <p class="lead">Zippy the bunny, Tomo the turtle and their friends retell classic fairy tales and fables for children aged 3 to 7. Every story is warm and funny, has no villains and ends calmly, with little moments where children can join in.</p>
    <div class="btns">
      <a class="btn" href="watch.html">Watch the stories</a>
      <a class="btn ghost" href="listen.html">Listen to the album</a>
    </div>
  </div>
  <div class="cast" aria-hidden="true">
    <img src="img/cast/zippy.webp" alt="" width="76" height="190">
    <img src="img/cast/tomo.webp" alt="" width="130" height="121">
    <img src="img/cast/silvia.webp" alt="" width="100" height="116">
    <img src="img/cast/little_sugar.webp" alt="" width="104" height="144">
  </div>
</div></section>

<section class="block"><div class="wrap">
  <div id="next"></div>
</div></section>

<section class="block"><div class="wrap">
  <h2>Latest stories</h2>
  <div class="grid" id="latest"><p>Loading…</p></div>
  <div class="btns"><a class="btn ghost" href="watch.html">See all stories and Shorts</a></div>
</div></section>

<section class="block"><div class="wrap">
  <div class="grid">
    <a class="card" href="listen.html"><img class="thumb" src="img/album.jpg" alt="Little Leap album cover" style="aspect-ratio:16/9;object-position:center 58%"><div class="body"><span class="tag">Music</span><h3>The “Little Leap” album</h3><div class="meta">8 gentle songs from the Big Meadow</div></div></a>
    <a class="card" href="play.html"><img class="thumb" src="img/play_race.jpg" alt=""><div class="body"><span class="tag">Games</span><h3>Meadow Games</h3><div class="meta">The Big Meadow Race and Meadow Memory, free in the browser</div></div></a>
    <a class="card" href="shop.html"><img class="thumb" src="img/play_memory.jpg" alt=""><div class="body"><span class="tag soon">Coming soon</span><h3>Shop</h3><div class="meta">Coloring pages, a coloring book and a character gift</div></div></a>
  </div>
</div></section>

<section class="block"><div class="wrap narrow">
  <h2>LittleLeap News</h2>
  <p>Happy news for kids aged 3 to 7, live on YouTube from the LittleLeap Studios channel. Zippy, Tomo and their friends share good news from around the world, fun facts, new words, counting, kindness and the local weather.</p>
  <p>Editions go live every morning and after school for friends in the UK and Ireland, the US East Coast and Eastern Australia.</p>
  <p><a href="https://www.youtube.com/channel/UCfHazWNqEypzrdYbXHwj4kg">Watch LittleLeap Studios on YouTube</a></p>
  <p>The LittleLeap News app on Google is only used by LittleLeap Studios itself, to schedule its own live editions on its own YouTube channel and read its own channel statistics.</p>
  <p class="small"><a href="privacy.html">Privacy policy</a> · Contact: <a href="mailto:{CONTACT}">{CONTACT}</a></p>
</div></section>
""", scripts=True)

# ---------------------------------------------------------------- Watch
page("watch.html", "Watch",
     "Every LittleLeap Studios story, story collection and Short, with links to watch on YouTube.",
     f"""
<section class="block"><div class="wrap">
  <h1>Watch</h1>
  <p class="lead">A new story every two weeks, about 10 minutes each, with chapters. Each one retells a public-domain tale in our own words. Audio is also available in Spanish, Italian, Portuguese (Brazil), German and French: pick the language under ⚙️ “Audio track” on YouTube.</p>
  <div id="next"></div>
</div></section>
<section class="block"><div class="wrap">
  <h2>Stories</h2>
  <div class="grid" id="episodes"><p>Loading…</p></div>
</div></section>
<section class="block"><div class="wrap">
  <h2>Shorts</h2>
  <p class="muted">One-minute meet-the-friends, learning and bedtime Shorts.</p>
  <ul class="shorts" id="shorts"></ul>
  <div class="btns"><a class="btn" href="{CHANNEL}" target="_blank" rel="noopener">Open the YouTube channel</a></div>
</div></section>
""", scripts=True)

# ---------------------------------------------------------------- Listen
tracks = ["Good Morning, Meadow", "Tiptoe Adventure", "Brave Together", "We Did It!",
          "Meadow Dance-Off", "Sunset Goodnight", "Everything's All Right Now", "Sleepy Paws Lullaby"]
page("listen.html", "Listen",
     "Little Leap, the album: 8 gentle songs from the Big Meadow by LittleLeap Studios.",
     f"""
<section class="block"><div class="wrap">
  <h1>Listen</h1>
  <div class="album">
    <img src="img/album.jpg" alt="Little Leap album cover: a glowing sprout under a full moon" width="320" height="320">
    <div>
      <h2>Little Leap</h2>
      <p>8 gentle songs from the Big Meadow: the music you hear in the stories, from the first “good morning” to the last lullaby.</p>
      <ol class="tracks">{"".join(f"<li>{t}</li>" for t in tracks)}</ol>
      <div class="btns">{album_buttons()}</div>
    </div>
  </div>
</div></section>
""")

# ---------------------------------------------------------------- Play
page("play.html", "Play",
     "Free Meadow Games for young children: The Big Meadow Race and Meadow Memory. No ads, no sign-up.",
     """
<section class="block"><div class="wrap">
  <h1>Play</h1>
  <p class="lead">Free games with the Big Meadow friends. They run in the browser on a phone, tablet or computer, with no ads, no sign-up and nothing collected.</p>
  <div class="grid play">
    <a class="card" href="https://mkda.github.io/games/meadow-race/"><img class="thumb" src="img/play_race.jpg" alt=""><div class="body"><span class="tag">Game</span><h3>The Big Meadow Race</h3><div class="meta">Race with Tomo and Zippy, just like in the very first story.</div><span class="btn">Play</span></div></a>
    <a class="card" href="https://mkda.github.io/games/memory/"><img class="thumb" src="img/play_memory.jpg" alt=""><div class="body"><span class="tag">Game</span><h3>Meadow Memory</h3><div class="meta">Find the pairs, 14 levels from very easy to all 18 friends. Also coming to the App Store.</div><span class="btn">Play</span></div></a>
  </div>
  <p class="small muted" style="margin-top:16px"><a href="https://mkda.github.io/games/">All Meadow Games</a> · <a href="https://mkda.github.io/games/memory/privacy.html">Games privacy policy</a></p>
</div></section>
""")

# ---------------------------------------------------------------- Shop
page("shop.html", "Shop",
     "LittleLeap Studios shop, coming soon: printable coloring pages, a printed coloring book, album downloads and a gift that puts a child's own animal friend in a story.",
     """
<section class="block"><div class="wrap">
  <h1>Shop</h1>
  <p class="lead">For grown-ups. Our shop is getting ready. Purchases will go through a secure checkout with a trusted shop provider; this site itself never handles payments.</p>
  <div class="grid">
    <div class="card"><div class="body"><span class="tag soon">Coming soon</span><h3>Printable coloring pages</h3><p>A pack of big, clear outline drawings for each story, plus a whole-cast pack. A4 and US Letter PDFs to print at home.</p></div></div>
    <div class="card"><div class="body"><span class="tag soon">Coming soon</span><h3>The LittleLeap Coloring Book</h3><p>A printed coloring book with all the Big Meadow friends, printed on demand and posted to your door.</p></div></div>
    <div class="card"><div class="body"><span class="tag soon">Coming soon</span><h3>Album download and wallpapers</h3><p>The “Little Leap” album as a download, plus phone, tablet and desktop wallpapers of the cast.</p></div></div>
    <div class="card"><div class="body"><span class="tag soon">Coming soon</span><h3>Gift: a friend in the next story</h3><p>Create an animal friend with your child: a first name or nickname, an animal, one favourite colour, one accessory and a happy catch phrase. The friend appears in an upcoming story and you get a collector card.</p><p class="small muted">Booked at least one month ahead, only one or two places per story. A parent orders and gives consent; first names only. Every request is checked by hand, and anything we can't make is fully refunded.</p></div></div>
  </div>
</div></section>
""")

# ---------------------------------------------------------------- Parents
page("parents.html", "For parents",
     "About LittleLeap Studios: how the stories are made, how AI tools are used, and how we keep things safe for young children.",
     f"""
<section class="block"><div class="wrap narrow">
  <h1>For parents</h1>
  <h2>What LittleLeap is</h2>
  <p>LittleLeap Studios makes gentle cartoon stories for children aged 3 to 7. We retell classic public-domain fables and fairy tales, such as Aesop and the Brothers Grimm, in our own words, with our own original characters: Zippy the bunny, Tomo the turtle, Silvia the squirrel, Little Sugar the bear and their friends from the Big Meadow.</p>
  <ul class="ticks">
    <li>No villains and no scary moments: problems are solved with kindness and teamwork.</li>
    <li>Calm endings, so a story works well before a nap or bedtime.</li>
    <li>Join-in moments: counting, waving, flapping like Zippy.</li>
    <li>About 10 minutes per story, with chapters. A new one every two weeks.</li>
  </ul>
  <h2>How we use AI</h2>
  <p class="note">The stories are written, directed and checked by a person. We use AI tools to help draw the pictures, voice the characters and compose the music, and every episode is reviewed by hand before it goes online. Each YouTube description says that AI tools were used.</p>
  <h2>Safety and privacy</h2>
  <ul class="ticks">
    <li>All our videos are marked “Made for Kids” on YouTube.</li>
    <li>This website has no ads, no cookies, no trackers and no sign-up. Videos open on YouTube.</li>
    <li>Our games collect no data.</li>
    <li>Read the <a href="privacy.html">privacy policy</a>.</li>
  </ul>
  <h2>Contact</h2>
  <p>Questions, ideas or a story your child loves? Write to <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
</div></section>
""")
