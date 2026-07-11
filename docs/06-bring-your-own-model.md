# Bring Your Own Model

`SETUP.md` works the same way no matter which agent CLI you paste it into: it detects your CLI, wires the right rule file, and interviews you. This page is only the step BEFORE that, the one SETUP.md itself doesn't cover, getting the CLI installed and pointed at a model. Pick your CLI below, run its install + config recipe, then paste `SETUP.md` into it and let it take over.

## Claude Code

Install: [claude.com/claude-code](https://claude.com/claude-code).

Once installed, open a terminal in the vault folder (the one directly containing `CLAUDE.md`) and run:

```bash
claude
```

Then paste the contents of `SETUP.md`.

`Tested with: Claude Code 2.1.207 on 2026-07-12.`

## Codex CLI

```bash
npm i -g @openai/codex
```

Open a terminal in the vault folder and run:

```bash
codex
```

Codex CLI reads `AGENTS.md` natively, no extra wiring needed once SETUP.md's Phase 3 has written it. Paste `SETUP.md` in to kick off setup.

`Recipe only — community verification welcome (open an issue).`

## Gemini CLI

```bash
npm i -g @google/gemini-cli
```

Open a terminal in the vault folder and run:

```bash
gemini
```

Gemini CLI reads `GEMINI.md`, which SETUP.md's Phase 3 writes as a one-line pointer to `CLAUDE.md`. One thing to expect: Gemini CLI's approval prompts default to on, so it'll ask before each shell command and file write during setup, same as most CLIs, just confirm your way through.

`Recipe only — community verification welcome (open an issue).`

## Grok Builder

Install Grok Builder per [xAI's docs](https://x.ai) for your platform. Once installed, open it in the vault folder and paste `SETUP.md`.

Grok Builder reads `AGENTS.md`, which SETUP.md's Phase 3 writes as a full copy of `CLAUDE.md` — verified live: a restarted session with no setup context loaded it, routed a new fact to the right daily note, and reported the path.

`Tested with: Grok Builder on 2026-07-12.`

## opencode + any endpoint

opencode doesn't ship a fixed provider list, you point it at any OpenAI-compatible endpoint yourself via `opencode.json` in the vault folder. Once a provider is configured, `AGENTS.md` (written by SETUP.md's Phase 3) covers the rest, paste `SETUP.md` in as usual.

Each block below is a working `opencode.json` for that provider: install opencode, drop the file in your vault folder, set the env var, smoke-test with `opencode run "say ok"`, then paste `SETUP.md`. Model ids rot, always check the vendor's current model page before you rely on the example id below.

### GLM (Zhipu)

Endpoint: `https://open.bigmodel.cn/api/paas/v4`
Env var: `ZHIPUAI_API_KEY`
Example model: `glm-4.6` family

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "zhipu": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "GLM (Zhipu)",
      "options": {
        "baseURL": "https://open.bigmodel.cn/api/paas/v4",
        "apiKey": "{env:ZHIPUAI_API_KEY}"
      },
      "models": {
        "glm-4.6": {
          "name": "GLM-4.6"
        }
      }
    }
  }
}
```

```bash
export ZHIPUAI_API_KEY=your-key-here
opencode run "say ok"
```

Model ids rot, check [open.bigmodel.cn](https://open.bigmodel.cn) for the current GLM model list before you rely on `glm-4.6`.

### Grok (xAI)

Endpoint: `https://api.x.ai/v1`
Env var: `XAI_API_KEY`
Example model: `grok-4` family

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "xai": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Grok (xAI)",
      "options": {
        "baseURL": "https://api.x.ai/v1",
        "apiKey": "{env:XAI_API_KEY}"
      },
      "models": {
        "grok-4": {
          "name": "Grok 4"
        }
      }
    }
  }
}
```

```bash
export XAI_API_KEY=your-key-here
opencode run "say ok"
```

Model ids rot, check [x.ai](https://x.ai) for the current Grok model list before you rely on `grok-4`.

### Qwen (Alibaba)

Endpoint: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
Env var: `DASHSCOPE_API_KEY`
Example model: `qwen3` family

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "qwen": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Qwen (Alibaba)",
      "options": {
        "baseURL": "https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
        "apiKey": "{env:DASHSCOPE_API_KEY}"
      },
      "models": {
        "qwen3": {
          "name": "Qwen3"
        }
      }
    }
  }
}
```

```bash
export DASHSCOPE_API_KEY=your-key-here
opencode run "say ok"
```

Model ids rot, check [dashscope.aliyun.com](https://dashscope.aliyun.com) for the current Qwen model list before you rely on `qwen3`.

### DeepSeek

Endpoint: `https://api.deepseek.com`
Env var: `DEEPSEEK_API_KEY`
Example model: `deepseek-chat`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "deepseek": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "DeepSeek",
      "options": {
        "baseURL": "https://api.deepseek.com",
        "apiKey": "{env:DEEPSEEK_API_KEY}"
      },
      "models": {
        "deepseek-chat": {
          "name": "DeepSeek Chat"
        }
      }
    }
  }
}
```

```bash
export DEEPSEEK_API_KEY=your-key-here
opencode run "say ok"
```

Model ids rot, check [platform.deepseek.com](https://platform.deepseek.com) for the current DeepSeek model list before you rely on `deepseek-chat`.

### Kimi (Moonshot)

Endpoint: `https://api.moonshot.ai/v1`
Env var: `MOONSHOT_API_KEY`
Example model: `kimi-k2` family

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "moonshot": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Kimi (Moonshot)",
      "options": {
        "baseURL": "https://api.moonshot.ai/v1",
        "apiKey": "{env:MOONSHOT_API_KEY}"
      },
      "models": {
        "kimi-k2": {
          "name": "Kimi K2"
        }
      }
    }
  }
}
```

```bash
export MOONSHOT_API_KEY=your-key-here
opencode run "say ok"
```

Model ids rot, check [platform.moonshot.ai](https://platform.moonshot.ai) for the current Kimi model list before you rely on `kimi-k2`.

## Tier 2: anything else

Running a CLI not listed above? Check what it reads for project-level rules first.

If it reads `AGENTS.md`: nothing new to do, `SETUP.md`'s Phase 3 already writes a full copy of `CLAUDE.md` into `AGENTS.md` for exactly this case, install your CLI, run it in the vault folder, paste `SETUP.md`.

If it uses a different rules-file convention (its own filename, its own pointer syntax): find that convention in its docs, then apply the same full-copy treatment SETUP.md's Phase 3 uses for `AGENTS.md`, a complete copy of `CLAUDE.md`'s content under your CLI's expected filename, not a one-line pointer. Future sessions of that CLI only load their native filename, a partial copy means partial rules.
