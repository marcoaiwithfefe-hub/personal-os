# Projects

One folder per project: `Projects/{name}/`.

## Structure

- `README.md`: the entry point. Overview, current status, next steps, the first thing you or Claude reads when picking the project back up.
- `CLAUDE.md`: rules for this project only. Created when the first correction about this project arrives, not before. Read it before working on the project.
- `specs/`, `research/`, `notes/`: created only when content actually arrives, not scaffolded up front.

## Rules

- A rule that applies to one project lives in that project's `CLAUDE.md`, never in the root file. The root file holds only rules for every session.
- Don't create empty subfolders for a project that doesn't need them yet.
- When a project finishes, move its folder to an archive location rather than leaving it live among active projects.
