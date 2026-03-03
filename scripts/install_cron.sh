#!/usr/bin/env bash
# ── install_cron.sh ──────────────────────────────────────────────────────────
# Helper to install (or update) a crontab entry for the processing pipeline.
#
# Usage:
#   ./scripts/install_cron.sh                # default: daily at 02:00
#   CRON_SCHEDULE="0 */6 * * *" ./scripts/install_cron.sh   # every 6 hours
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
RUN_SCRIPT="$SCRIPT_DIR/run_processing.sh"
LOG_FILE="$PROJECT_DIR/output/cron.log"

SCHEDULE="${CRON_SCHEDULE:-0 2 * * *}"
CRON_LINE="$SCHEDULE $RUN_SCRIPT >> $LOG_FILE 2>&1"

MARKER="# frequency_resonance"

# Remove any existing entry, then append the new one
( crontab -l 2>/dev/null | grep -v "$MARKER" ; echo "$CRON_LINE $MARKER" ) | crontab -

echo "Cron job installed:"
echo "  Schedule : $SCHEDULE"
echo "  Script   : $RUN_SCRIPT"
echo "  Log      : $LOG_FILE"
echo ""
echo "Current crontab:"
crontab -l
