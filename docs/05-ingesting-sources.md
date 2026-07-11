# Ingesting sources

Your vault doesn't just hold what you tell your agent; it can absorb what you read. Adapted from Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern: instead of re-reading raw sources every time a question comes up, the agent integrates each source into the vault once, and the synthesis compounds.

## The workflow

When the user says "ingest this" / "process this source" (or drops a file or URL):

1. **Read** the source in full.
2. **Extract** the claims and facts that matter to the user's domains (check `Context/me.md` for what they care about).
3. **Integrate**: update or create pages in `Knowledge/{domain}/`. New concept gets a new note; existing topic gets edited in place. Note where the new source contradicts something already written, don't silently overwrite.
4. **Cross-reference**: wikilink the touched pages to each other and to any related project or daily note. One source often touches several pages; that's normal.
5. **Log**: one line in today's `Daily/` note under Progress: what was ingested, which pages changed.

## Where sources live

Save a copy of the raw source (or its markdown conversion) under `Knowledge/{domain}/sources/` when the user wants it kept; otherwise integrating its content is enough. Raw sources are read-only once filed; the agent edits wiki pages, never the source.

## Keeping it healthy

Periodically ask the agent to lint: contradictions between pages, stale claims a newer source superseded, orphan pages nothing links to, concepts mentioned often but lacking their own note. (Claude Code users: the `optimize` extra in `.claude/skills/` does exactly this.)

## Tips

- **Obsidian Web Clipper** (browser extension) converts articles to markdown in one click — the fastest way to get web sources in.
- **Obsidian graph view** shows the shape of what you've built: hubs, clusters, orphans.
