// Fills the video lists from data/episodes.json. Videos open on YouTube; nothing is embedded or tracked here.
(function () {
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var fmtDate = function (iso) {
    var p = String(iso || "").split("-");
    if (p.length !== 3) return "";
    var d = new Date(Date.UTC(+p[0], +p[1] - 1, +p[2], 12));
    return d.toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "long", year: "numeric", timeZone: "UTC" });
  };
  var watchUrl = function (v) { return v.type === "short" ? "https://www.youtube.com/shorts/" + v.youtube : "https://www.youtube.com/watch?v=" + v.youtube; };
  var label = { episode: "Story", compilation: "Story collection", short: "Short" };

  var card = function (v) {
    var img = v.thumb ? '<img class="thumb" loading="lazy" src="' + esc(v.thumb) + '" alt="">' : "";
    var meta = [v.story, v.length].filter(Boolean).map(esc).join(" · ");
    return '<a class="card" href="' + watchUrl(v) + '" target="_blank" rel="noopener">' + img +
      '<div class="body"><span class="tag">' + esc(label[v.type] || "Video") + '</span><h3>' + esc(v.title) + '</h3>' +
      (meta ? '<div class="meta">' + meta + "</div>" : "") +
      (v.date ? '<div class="meta">' + esc(fmtDate(v.date)) + "</div>" : "") + "</div></a>";
  };

  var put = function (id, html) { var el = document.getElementById(id); if (el) el.innerHTML = html; };

  fetch("data/episodes.json", { cache: "no-cache" }).then(function (r) { return r.json(); }).then(function (d) {
    var vids = d.videos || [];
    var long = vids.filter(function (v) { return v.type !== "short"; }).sort(function (a, b) { return a.date < b.date ? 1 : -1; });
    var shorts = vids.filter(function (v) { return v.type === "short"; });

    put("episodes", long.map(card).join(""));
    put("latest", long.slice(0, 3).map(card).join(""));
    put("shorts", shorts.map(function (v) {
      return '<li><a href="' + watchUrl(v) + '" target="_blank" rel="noopener">' + esc(v.title) + "</a></li>";
    }).join(""));
    put("count", String(long.filter(function (v) { return v.type === "episode"; }).length));

    var n = d.next;
    var today = new Date().toISOString().slice(0, 10);
    if (n && n.date && n.date >= today) {
      put("next", '<div class="next"><span class="tag soon">Next story</span><div><div class="when">' + esc(fmtDate(n.date)) +
        '</div><div><strong>' + esc(n.title) + "</strong>" + (n.story ? ' <span class="muted">· ' + esc(n.story) + "</span>" : "") +
        "</div></div></div>");
    } else {
      put("next", '<div class="next"><span class="tag soon">Next story</span><div>A new story every two weeks. <a href="' + esc(d.channel) + '" target="_blank" rel="noopener">Subscribe on YouTube</a> so you never miss one.</div></div>');
    }
  }).catch(function () {
    put("episodes", '<p>Watch every story on <a href="https://www.youtube.com/@Little-Leap-Studios">our YouTube channel</a>.</p>');
  });
})();
