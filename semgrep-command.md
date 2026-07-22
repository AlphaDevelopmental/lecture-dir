======================================================================
                  SEMGREP CLI & POLICY CHEAT SHEET
======================================================================

1. ADVANCED SCANNING COMMANDS
----------------------------------------------------------------------
# Run standard auto-detected rulesets
semgrep scan --config auto

# Scan strictly for OWASP Top 10 vulnerabilities
semgrep scan --config p/owasp-top-10

# Scan strictly for hardcoded secrets, API keys, and tokens
semgrep scan --config p/secrets

# Combine multiple specific rulesets at once
semgrep scan --config p/owasp-top-10 --config p/secrets

# Scan a single specific file instead of the whole directory
semgrep scan --config auto pathways/to/file.js

# Scan a single specific directory
semgrep scan --config auto routes/


2. REPORTING & AUTOMATION FLAGS
----------------------------------------------------------------------
# Run a "quiet" scan (hides progress bars, only outputs findings)
semgrep scan --config auto -q

# Save findings into a clean JSON file for parsing
semgrep scan --config auto --json -o results.json

# Save findings into a standardized SARIF file for CI/CD pipelines
semgrep scan --config auto --sarif -o results.sarif


3. CORE RULES GUIDING SEMGREP USE
----------------------------------------------------------------------
• RULE 1: The '.semgrepignore' File
  Works exactly like a .gitignore file. Add heavy folders like 
  node_modules/ or build artifacts here to bypass scanning them.

• RULE 2: Code vs. Comments (AST Parsing)
  Semgrep reads the structural layout of code, not raw strings. 
  It will flag an active flaw, but ignores it if it sits inside 
  a regular comment block.

• RULE 3: Inline Ignoring via Code Comments
  To bypass a known false positive permanently, append an inline 
  comment directly above the specific line in your source code:
  
  // nosemgrep
  const private_key = "test_key_not_real";

======================================================================

4. MANUAL CODE AUDITING (GREP HUNTS)
----------------------------------------------------------------------
# Find all HTTP POST user inputs (Sources)
grep -rn "req\.body" app/

# Find all HTTP URL query inputs (Sources)
grep -rn "req\.query" app/

# Hunt for dangerous Evaluation Sinks
grep -rn "eval(" app/

# Hunt for System Command Sinks (RCE vectors)
grep -rn "exec(" app/
======================================================================
