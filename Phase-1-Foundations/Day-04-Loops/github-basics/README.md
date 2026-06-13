# GitHub Basics · Day 4 — Why GitHub? (Part 1 of 3)

The opening talk of a **3-part GitHub mini-track** woven into Days 4–6. Audience: complete beginners
who have *never* used version control. Goal of Part 1: they understand **why** Git/GitHub exist, the
**mental model** (commit = snapshot, local vs remote), the **core words**, and they **create an
account** — no commands yet.

> The 3-part arc: **Day 4 — Why &amp; What** (this deck) → **Day 5 — The Everyday Workflow**
> (add/commit/push) → **Day 6 — Branching &amp; Collaboration** (branches, pull requests).

## How to present it
Self-contained `index.html` — no install (fonts load from Google online; fall back cleanly offline).
The branching/timeline diagrams are **inline SVG**, so they're crisp at any size and need no images.
1. Double-click **`index.html`** (any browser).
2. Press **F** for fullscreen.
3. Navigate: **→ / Space / click-right** = next · **← / click-left** = back · **Home/End** = jump.

Works with a wireless clicker (maps to arrow keys). ~15–20 min with discussion. Slot it into the
day's intro, before the loops modules.

## Slide flow + speaker notes
12 slides.

| # | Slide | Talk about / ask the room |
|--:|-------|---------------------------|
| 1 | Title | "Two things every dev relies on and beginners skip: a time machine + an online home for code." |
| 2 | The "final" file nightmare | ⭐ Ask the room: "who has `project_final2.py`?" Every hand goes up. That pain *is* the hook. |
| 3 | Git vs GitHub | The key distinction. **Git = the camera; GitHub = the cloud photo album.** Repeat the analogy. |
| 4 | Commit = snapshot (SVG) | Walk the timeline left→right. Each dot is a checkpoint with a message; the chain is history. |
| 5 | What it buys you | Undo / backup / collaborate / get hired. Land "your GitHub is your portfolio." |
| 6 | Local &harr; remote (SVG) | Two boxes: laptop vs GitHub. Push = up, Pull = down. Don't drill commands yet — just direction. |
| 7 | Core terminology | repo / commit / push-pull / clone. Tell them: "you'll *use* these tomorrow, just recognise them now." |
| 8 | Create your account | Stress the **professional username** (it's a public URL recruiters see). |
| 9 | Anatomy of a repo page | Open a real repo live if you have a projector: files, README, commits, stars. |
| 10 | Recap | The 4 bullets. Check understanding before moving on. |
| 11 | **GitHub Action** | Give 5 min in-session to actually sign up. Collect usernames for tomorrow. |
| 12 | Close | Tease Day 5: the add → commit → push loop. |

## Teaching tips
- **Resist commands today.** The temptation is to jump into `git init`. Don't — Part 1 is *mental
  model only*. Beginners who get the "why" first stick with it; command-first scares them off.
- **Use the photo analogy relentlessly.** Commit = photo, history = photo album, push = upload album
  to the cloud. It carries the whole deck.
- **Make slide 2 personal.** Tell your own "I lost a week of work" story. The pain sells the tool.
- **Live demo (optional):** open `github.com/python/cpython`, scroll the README, click "commits" to
  show a real 30-year history. Jaws drop.

## Today's GitHub Action
**Create a GitHub account** with a clean, professional username, and explore one real repo (find its
README + commit history). ≤10 min. Bring the username to Day 5 — we connect it and push the first commit.

## Editing
All content + styling inline in `index.html` (same Softpro template as the Career Launchpad decks,
with two added helpers: `.cmd` command blocks and `.diagram` SVG wrappers). To add a slide, copy any
`<section class="slide">…</section>` block — the counter and progress bar update automatically.

➡ Next: **[Day 5 — The Everyday Workflow](../../Day-05-Functions-and-Scope/github-basics/)**
