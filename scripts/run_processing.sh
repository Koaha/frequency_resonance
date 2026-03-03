#!/usr/bin/env bash
# ── run_processing.sh ────────────────────────────────────────────────────────
# Cron-friendly wrapper for the signal processing pipeline.
#
# Usage:
#   ./scripts/run_processing.sh                  # uses default config.yaml
#   ./scripts/run_processing.sh /path/to/cfg.yaml
#
# Crontab example (every day at 02:00):
#   0 2 * * * /path/to/frequency_resonance/scripts/run_processing.sh >> /path/to/frequency_resonance/output/cron.log 2>&1
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG="${1:-$PROJECT_DIR/config.yaml}"
SRC_DIR="$PROJECT_DIR/src"
LOG_DIR="$PROJECT_DIR/output"

mkdir -p "$LOG_DIR"

echo "========================================"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting processing"
echo "  Project : $PROJECT_DIR"
echo "  Config  : $CONFIG"
echo "========================================"

# Activate virtual environment if one exists
if [ -f "$PROJECT_DIR/venv/bin/activate" ]; then
    source "$PROJECT_DIR/venv/bin/activate"
elif [ -f "$PROJECT_DIR/.venv/bin/activate" ]; then
    source "$PROJECT_DIR/.venv/bin/activate"
fi

cd "$SRC_DIR"
python main_processing.py --config "$CONFIG"

EXIT_CODE=$?
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Finished with exit code $EXIT_CODE"
exit $EXIT_CODE
