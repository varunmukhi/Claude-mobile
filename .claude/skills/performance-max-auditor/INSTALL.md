# Performance Max Auditor - Installation Guide

## Quick Install

1. **Download** `performance-max-auditor.skill`

2. **Extract and copy:**
   ```bash
   # macOS/Linux
   unzip performance-max-auditor.skill -d ~/.config/claude/skills/user/
   
   # Windows: Extract to %APPDATA%\Claude\skills\user\
   ```

3. **Restart Claude**

4. **Verify:** Type "List available skills" - you should see `performance-max-auditor`

## First Use

```
Audit this Performance Max campaign
[attach Google Ads export]
```

## Troubleshooting

**Skill not appearing:**
- Ensure folder name is exactly `performance-max-auditor`
- Check it's in the `user` subdirectory
- Completely restart Claude (quit and relaunch)

**Permission errors (macOS/Linux):**
```bash
chmod -R 755 ~/.config/claude/skills/user/performance-max-auditor
```

## Uninstall

```bash
# macOS/Linux
rm -rf ~/.config/claude/skills/user/performance-max-auditor

# Then restart Claude
```

---

See **README.md** for complete documentation and **EXAMPLES.md** for usage scenarios.
