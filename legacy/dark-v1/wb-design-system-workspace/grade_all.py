#!/usr/bin/env python3
"""Grade assertions for all eval runs."""
import json, re, os
from pathlib import Path

WORKSPACE = Path(__file__).parent / "iteration-1"

def check(content, pattern, flags=re.IGNORECASE):
    return bool(re.search(pattern, content, flags))

def grade_eval0(html):
    results = []
    def a(id, desc, passed, evidence=""):
        results.append({"text": desc, "passed": passed, "evidence": evidence})

    a("has-dark-bg", "Uses #0e0e0e or var(--bg) as background",
      check(html, r'(#0e0e0e|var\(--bg\))'),
      "found" if check(html, r'(#0e0e0e|var\(--bg\))') else "not found")

    a("uses-jetbrains-mono", "Google Fonts JetBrains Mono import present",
      check(html, r'JetBrains.Mono'),
      "found" if check(html, r'JetBrains.Mono') else "not found")

    a("has-section-label-format", "Section label '01 // ' numbering pattern",
      check(html, r'0[1-9]\s*//'),
      "found" if check(html, r'0[1-9]\s*//') else "not found")

    a("has-scroll-observer", "IntersectionObserver present",
      check(html, r'IntersectionObserver'),
      "found" if check(html, r'IntersectionObserver') else "not found")

    a("has-author-attribution", "linkedin.com/in/brasileiro link",
      check(html, r'linkedin\.com/in/brasileiro'),
      "found" if check(html, r'linkedin\.com/in/brasileiro') else "not found")

    has_border_radius = check(html, r'border-radius\s*:\s*(?!0|none|50%)[0-9]')
    a("no-border-radius-cards", "No border-radius on cards (50% for circles is ok)",
      not has_border_radius,
      "VIOLATION: border-radius found" if has_border_radius else "clean")

    extra_colors = check(html, r'color\s*:\s*(blue|red|green|orange|purple|#[0-9a-f]{3,6}(?!\s*;?\s*\/\*\s*accent))')
    a("no-extra-colors", "No extra hue colors outside token palette",
      not extra_colors,
      "VIOLATION: extra colors found" if extra_colors else "clean")

    a("flow-chain-present", ".flow-chain or .flow-step classes present",
      check(html, r'flow-chain|flow-step'),
      "found" if check(html, r'flow-chain|flow-step') else "not found")

    a("cards-present", ".card class present",
      check(html, r'class=["\'][^"\']*card'),
      "found" if check(html, r'class=["\'][^"\']*card') else "not found")

    a("uses-clamp-headings", "clamp() used for heading sizes",
      check(html, r'clamp\('),
      "found" if check(html, r'clamp\(') else "not found")

    return results

def grade_eval1(html):
    results = []
    def a(id, desc, passed, evidence=""):
        results.append({"text": desc, "passed": passed, "evidence": evidence})

    a("split-panel-structure", ".split-panel.old and .split-panel.new present",
      check(html, r'split-panel') and check(html, r'\.old|class=["\'][^"\']*old') and check(html, r'\.new|class=["\'][^"\']*new'),
      "found" if check(html, r'split-panel') else "not found")

    a("old-panel-dimmed", "opacity: 0.4 on old panel",
      check(html, r'opacity\s*:\s*0\.4'),
      "found" if check(html, r'opacity\s*:\s*0\.4') else "not found")

    a("new-panel-accent-border", "accent-dim used for new panel border",
      check(html, r'accent.dim|--accent'),
      "found" if check(html, r'accent.dim|--accent') else "not found")

    a("mono-for-bullets", "Monospace font for bullet points",
      check(html, r'var\(--mono\)|JetBrains'),
      "found" if check(html, r'var\(--mono\)|JetBrains') else "not found")

    a("has-dark-bg", "Dark background used, not light theme",
      check(html, r'(#0e0e0e|var\(--bg\))'),
      "found" if check(html, r'(#0e0e0e|var\(--bg\))') else "not found")

    a("panel-label-uppercase-mono", "Panel labels use uppercase monospace",
      check(html, r'text-transform\s*:\s*uppercase') and check(html, r'var\(--mono\)|font-family.*mono', re.IGNORECASE),
      "found" if check(html, r'text-transform\s*:\s*uppercase') else "not found")

    return results

def grade_eval2(fixed_html, review_md):
    results = []
    def a(id, desc, passed, evidence=""):
        results.append({"text": desc, "passed": passed, "evidence": evidence})

    a("removes-white-bg", "background:#fff removed from fixed output",
      not check(fixed_html, r'background\s*:\s*#fff\b'),
      "clean" if not check(fixed_html, r'background\s*:\s*#fff\b') else "VIOLATION: #fff still present")

    a("removes-border-radius", "border-radius removed from fixed output",
      not check(fixed_html, r'border-radius\s*:\s*(?!0|none|50%)[0-9]'),
      "clean" if not check(fixed_html, r'border-radius\s*:\s*(?!0|none|50%)[0-9]') else "VIOLATION: border-radius still present")

    a("removes-box-shadow", "box-shadow removed from fixed output",
      not check(fixed_html, r'box-shadow'),
      "clean" if not check(fixed_html, r'box-shadow') else "VIOLATION: box-shadow still present")

    a("removes-blue-accent", "color:blue removed from fixed output",
      not check(fixed_html, r'color\s*:\s*blue\b'),
      "clean" if not check(fixed_html, r'color\s*:\s*blue\b') else "VIOLATION: color:blue still present")

    a("applies-dark-bg-token", "#0e0e0e or var(--bg) present in fixed output",
      check(fixed_html, r'(#0e0e0e|var\(--bg\))'),
      "found" if check(fixed_html, r'(#0e0e0e|var\(--bg\))') else "not found")

    a("applies-fg-for-text", "Design token colors used for text",
      check(fixed_html, r'var\(--fg\)|var\(--dim\)|#f3f1ec'),
      "found" if check(fixed_html, r'var\(--fg\)|var\(--dim\)|#f3f1ec') else "not found")

    a("review-md-exists", "review.md file exists",
      bool(review_md),
      "exists" if review_md else "MISSING")

    violation_count = len(re.findall(r'(?:^|\n)\s*(?:\d+[\.\)]|[-*])\s+\S', review_md or ""))
    a("review-identifies-violations", f"review.md lists ≥4 violations ({violation_count} found)",
      violation_count >= 4,
      f"{violation_count} bullet items found")

    return results

def read_file(path):
    try:
        return Path(path).read_text()
    except:
        return None

def write_grading(run_dir, assertions):
    Path(run_dir).mkdir(parents=True, exist_ok=True)
    grading = {"expectations": assertions}
    (Path(run_dir) / "grading.json").write_text(json.dumps(grading, indent=2))
    passed = sum(1 for a in assertions if a["passed"])
    total = len(assertions)
    print(f"  {run_dir.name}: {passed}/{total} passed")

# Grade eval 0
for variant in ["with_skill", "without_skill"]:
    run_dir = WORKSPACE / "eval-new-hotsite" / variant
    html = read_file(run_dir / "outputs/index.html")
    if html:
        assertions = grade_eval0(html)
        write_grading(run_dir, assertions)

# Grade eval 1
for variant in ["with_skill", "without_skill"]:
    run_dir = WORKSPACE / "eval-content-section" / variant
    html = read_file(run_dir / "outputs/index.html")
    if html:
        assertions = grade_eval1(html)
        write_grading(run_dir, assertions)

# Grade eval 2
for variant in ["with_skill", "without_skill"]:
    run_dir = WORKSPACE / "eval-subtle-violation" / variant
    fixed = read_file(run_dir / "outputs/fixed.html")
    review = read_file(run_dir / "outputs/review.md")
    if fixed:
        assertions = grade_eval2(fixed, review)
        write_grading(run_dir, assertions)

print("\nDone.")
