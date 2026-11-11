# Installation Guide - Negative Keyword Miner

## Quick Install

### Option 1: Direct Copy (Recommended)

1. **Download the skill files**
   - Download `negative-keyword-miner.zip` 
   - Or clone from repository

2. **Copy to Claude Skills directory**
   ```bash
   # Create skills directory if it doesn't exist
   mkdir -p ~/.config/claude/skills/user
   
   # Copy skill folder
   cp -r negative-keyword-miner ~/.config/claude/skills/user/
   ```

3. **Verify installation**
   - Open Claude
   - Type: "negative keyword miner"
   - Skill should load automatically

### Option 2: Manual Setup

1. **Create skill directory**
   ```bash
   mkdir -p ~/.config/claude/skills/user/negative-keyword-miner
   cd ~/.config/claude/skills/user/negative-keyword-miner
   ```

2. **Create directory structure**
   ```bash
   mkdir -p references scripts assets
   ```

3. **Copy files**
   - Copy `SKILL.md` to main directory
   - Copy `skill.yaml` to main directory  
   - Copy reference files to `references/`
   - Copy Python script to `scripts/`
   - Copy README, EXAMPLES, INSTALL files to main directory

4. **Set permissions**
   ```bash
   chmod +x scripts/analyze_search_terms.py
   ```

## Verification

### Check File Structure

Your directory should look like this:

```
negative-keyword-miner/
├── SKILL.md
├── README.md
├── EXAMPLES.md
├── INSTALL.md
├── skill.yaml
├── references/
│   ├── analysis-framework.md
│   ├── output-template.md
│   ├── best-practices.md
│   └── pattern-library.md
├── scripts/
│   └── analyze_search_terms.py
└── assets/
    └── (placeholder for future assets)
```

### Test the Skill

1. **Basic test**
   ```
   Open Claude and type:
   "Help me analyze negative keywords for my ad campaign"
   ```

2. **With data test**
   ```
   "I have search term data showing wasted spend on job-related searches. 
   Can you help me create negative keywords?"
   ```

If the skill loads and starts asking relevant questions, installation is successful! ✅

## Optional: Python Script Setup

The included Python script can pre-analyze CSV files.

### Requirements

- Python 3.6+
- No additional packages needed (uses standard library)

### Usage

```bash
cd ~/.config/claude/skills/user/negative-keyword-miner/scripts

# Make executable
chmod +x analyze_search_terms.py

# Run analysis
python3 analyze_search_terms.py /path/to/search_terms_report.csv
```

### Expected Output

The script will generate a console report showing:
- Total wasted spend
- Pattern analysis
- Top negative keyword recommendations
- Estimated savings

You can then provide this output to Claude for detailed recommendations.

## Troubleshooting

### Skill Not Loading

**Issue**: Claude doesn't recognize the skill

**Solutions**:
1. Check file location: `~/.config/claude/skills/user/negative-keyword-miner/`
2. Verify `SKILL.md` exists in root of skill directory
3. Verify `skill.yaml` has correct syntax
4. Restart Claude application
5. Check Claude logs for errors

### YAML Parsing Error

**Issue**: "Invalid YAML format" error

**Solutions**:
1. Validate YAML syntax:
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('skill.yaml'))"
   ```
2. Check for:
   - Proper indentation (2 spaces, not tabs)
   - No special characters in strings
   - Correct list formatting

### Reference Files Not Loading

**Issue**: Skill works but doesn't use reference materials

**Solutions**:
1. Check `references/` directory exists
2. Verify all 4 reference files are present:
   - analysis-framework.md
   - output-template.md
   - best-practices.md
   - pattern-library.md
3. Check file permissions (should be readable)

### Python Script Errors

**Issue**: Script won't run or throws errors

**Solutions**:
1. Check Python version: `python3 --version` (need 3.6+)
2. Make executable: `chmod +x analyze_search_terms.py`
3. Verify CSV format has required columns
4. Try running with verbose error output:
   ```bash
   python3 -u analyze_search_terms.py your_file.csv
   ```

## Platform-Specific Notes

### macOS

Default Claude config location: `~/.config/claude/`

If directory doesn't exist:
```bash
mkdir -p ~/.config/claude/skills/user
```

### Linux

Same as macOS: `~/.config/claude/skills/user/`

### Windows

Claude config typically in: `%USERPROFILE%\.config\claude\skills\user\`

PowerShell commands:
```powershell
New-Item -ItemType Directory -Path "$env:USERPROFILE\.config\claude\skills\user\negative-keyword-miner" -Force
```

## Updating the Skill

To update to a new version:

1. **Backup your current version** (if you made customizations)
   ```bash
   cp -r ~/.config/claude/skills/user/negative-keyword-miner ~/negative-keyword-miner-backup
   ```

2. **Download new version**

3. **Replace files**
   ```bash
   rm -rf ~/.config/claude/skills/user/negative-keyword-miner
   cp -r negative-keyword-miner ~/.config/claude/skills/user/
   ```

4. **Restart Claude**

## Uninstallation

To remove the skill:

```bash
rm -rf ~/.config/claude/skills/user/negative-keyword-miner
```

Then restart Claude.

## Getting Help

**Installation Issues**:
- Check the troubleshooting section above
- Verify file structure matches expected layout
- Check Claude documentation for skills installation

**Usage Questions**:
- See README.md for overview
- See EXAMPLES.md for detailed use cases
- Try asking Claude directly: "How do I use the negative keyword miner skill?"

**Bug Reports or Feature Requests**:
- Comment on the skill distribution post
- Tag @jabberwocky in Claude community
- Include: error message, what you were trying to do, your system info

## Success Checklist

- [ ] Files copied to correct directory
- [ ] `SKILL.md` in root of skill folder
- [ ] All reference files in `references/` subdirectory
- [ ] `skill.yaml` validates without errors
- [ ] Skill loads when you mention it to Claude
- [ ] Python script executable (optional)
- [ ] You've reviewed README.md and EXAMPLES.md

---

**Ready to start?** Export your search terms report and ask Claude:

"I have a search terms report from Google Ads. Can you help me identify negative keywords to reduce wasted spend?"

The skill will guide you through the analysis process!
