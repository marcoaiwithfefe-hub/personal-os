<!-- CANTO-DRAFT: needs native pass -->

# 1 頁唔使識 code 都跟到嘅 quickstart

用 AI 幫你記住嘢、整理成個人生，唔使識寫 code。

## 你需要乜

- 一部電腦（Mac 定 Windows 都得）
- 大概 30 分鐘
- 一個 Claude 帳號

老實講：Claude Code 呢個工具要俾錢用，唔係完全免費。Obsidian 就梗係免費嘅。

## 5 步開始

**① 裝 Obsidian**

去 [obsidian.md](https://obsidian.md) 撳個掣裝落嚟，跟住畫面指示做就得。
成功嘅樣：部機度開到個 Obsidian app，見到歡迎畫面。

**② 裝 Claude Code**

去官方安裝頁：[claude.com/claude-code](https://claude.com/claude-code)。個安裝器會一步步教你，跟住畫面做就得。
成功嘅樣：安裝器話你安裝完成。

**③ Download 呢個 repo**

Repo 即係「一個 folder 嘅網上版」。去呢個 GitHub 頁面，撳個綠色 **Code** 掣 → **Download ZIP** → 解壓（雙擊個 zip 檔就得）。跟住用 Obsidian 打開嗰個 folder 做 vault（vault 即係 Obsidian 叫你嘅筆記本做嘅名）。
成功嘅樣：Obsidian 左手面見到成堆 folder，例如 `Daily`、`Context`、`Knowledge`。

**④ 喺個 folder 度開 terminal，打兩句嘢**

Terminal（終端機）即係部機入面一個打字用嘅窗口。一定要喺頭先解壓嗰個 folder 度開佢：
Mac：喺 Finder 右 click 個 folder →「New Terminal at Folder」（搵唔到呢個選項嘅話，將個 folder 拖去 Dock 上面個 Terminal icon 度）。
Windows：喺 File Explorer 開個 folder，喺上面地址欄打 `cmd` 撳 Enter。
成功嘅樣：個窗口最尾嗰行見到你 folder 個名。跟住打：

```
claude
```

見到個黑色視窗打字得 = 成功。第一次會叫你登入 Claude 帳號，跟住做就得。跟住打：

```
/onboard
```

Claude 會逐條問你幾條問題（你叫咩名、做咩、想呢個系統幫你顧邊幾樣嘢、有咩短期目標、想點樣睇返啲資訊），照答就得，唔識答可以 skip。
成功嘅樣：佢答完會幫你填好個人資料檔，仲寫低第一篇日記。

**⑤ 之後每日**

開返個 session（即係打 `claude` 再開始傾偈），將發生咗咩、諗到咩、變咗咩，同佢講就得。AI 自己識歸檔，唔使你自己執 file。
成功嘅樣：你會見到 `Daily/` folder 入面自動多咗今日嘅 note。

## 常見問題

**唔識 code 真係得？**
得。成個設計就係俾你打字同佢傾偈，唔使寫一行 code。

**我啲資料去咗邊？**
全部都喺你自己部機嘅 folder 入面，普通 markdown 檔，隨時打得開、攞得走，唔會鎖死喺邊個 app 度。

**搞壞咗點算？**
啲檔案淨係普通文字檔（markdown）。刪咗個 folder，重新 download 過個 repo 就得，唔會整壞你部機。

<!-- /CANTO-DRAFT -->

---

## English (short mirror)

**What you need:** a computer (Mac or Windows), about 30 minutes, a Claude account. Obsidian is free; Claude Code costs money, it isn't free.

**5 steps:**

1. Install [Obsidian](https://obsidian.md). Success looks like: the app opens to a welcome screen.
2. Install [Claude Code](https://claude.com/claude-code), the installer walks you through it.
3. Download this repo (green **Code** button on GitHub → Download ZIP → unzip), then open that folder in Obsidian as a vault. Success looks like: you see folders such as `Daily`, `Context`, `Knowledge` in Obsidian's sidebar.
4. Open a terminal in that folder, type `claude`, then type `/onboard`. It asks a few questions one at a time; answer or skip.
5. From then on: open a session daily, talk to it plainly, it files everything itself.

**FAQ**

- No coding skill required? Correct, the whole design is built around typing plain sentences.
- Where does my data go? Nowhere but your own machine, plain markdown files, yours to read or take anytime.
- What if I break something? Files are just text. Delete the folder and re-download the repo.
