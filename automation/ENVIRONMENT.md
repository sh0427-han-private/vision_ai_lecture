# Execution environment · 2026-10-19

- Repository: main ad3f0a8, approved storyboard 28fc97d, existing A/B builder 9ce8be57 reused on automation/approved-55-20261019. No main merge/deploy authorized during this project.
- Git read/write: read verified by fetch; branch push verification pending. GitHub PR API: GraphQL Forbidden. GH_TOKEN binding exists from earlier session; values are never printed. No assumption that an unset token means absent Git proxy authentication.
- Python3.12.14, Playwright/Pillow/lxml imports PASS in /workspace/.venvs/vision-ai. Chromium154 /usr/bin/chromium. Use supported Playwright executable_path override through /workspace/.onboarding/vision-ai/run_browser_check.py.
- Existing verify_two_hour_course.py fails on main due to obsolete exact AND phrase; diagnose against actual code and preserve behavioral math checks during 55-slide migration.
- Local server available at port8766 for internal QA. Tool setup was reused; no installation or reusable environment configuration changes required.
- Independent Reviewer child agent available. User explicitly authorized Builder/Reviewer delegation. Reviews pin commit SHA; reports never count classroom rehearsal or public deployment as performed.
- External image hosts and api.github.com remain blocked; github.com and native git work. Prefer source-registered local scientific/generated images; official-source retrieval failures will be recorded.
