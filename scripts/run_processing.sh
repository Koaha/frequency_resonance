#!/usr/bin/env bash
# ── run_processing.sh ────────────────────────────────────────────────────────
# Cron-friendly wrapper for the signal processing pipeline.
#
# Usage:
#   ./scripts/run_processing.sh                       # all patients, default config
#   ./scripts/run_processing.sh --max-patients 10     # first 10 patients only
#   ./scripts/run_processing.sh --config /path/to/cfg.yaml --max-patients 5
#
# Crontab example (every day at 02:00):
#   0 2 * * * /path/to/frequency_resonance/scripts/run_processing.sh >> /path/to/frequency_resonance/output/cron.log 2>&1
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SRC_DIR="$PROJECT_DIR/src"
LOG_DIR="$PROJECT_DIR/output"

# ── parse named arguments ────────────────────────────────────────────────────
CONFIG="$PROJECT_DIR/config.yaml"
MAX_PATIENTS=0
EXTRA_ARGS=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --config)       CONFIG="$2";       shift 2 ;;
        --max-patients) MAX_PATIENTS="$2"; shift 2 ;;
        *)              EXTRA_ARGS+=("$1"); shift ;;
    esac
done

mkdir -p "$LOG_DIR"

echo "========================================"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting processing"
echo "  Project      : $PROJECT_DIR"
echo "  Config       : $CONFIG"
echo "  Max patients : ${MAX_PATIENTS:-all}"
echo "========================================"

# Activate virtual environment if one exists
if [ -f "$PROJECT_DIR/venv/bin/activate" ]; then
    source "$PROJECT_DIR/venv/bin/activate"
elif [ -f "$PROJECT_DIR/.venv/bin/activate" ]; then
    source "$PROJECT_DIR/.venv/bin/activate"
fi

cd "$SRC_DIR"

CMD=(python main_processing.py --config "$CONFIG")
if [ "$MAX_PATIENTS" -gt 0 ] 2>/dev/null; then
    CMD+=(--max-patients "$MAX_PATIENTS")
fi
if [ ${#EXTRA_ARGS[@]} -gt 0 ]; then
    CMD+=("${EXTRA_ARGS[@]}")
fi

"${CMD[@]}"

EXIT_CODE=$?
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Finished with exit code $EXIT_CODE"
exit $EXIT_CODE
