#!/usr/bin/env bash
# Connects Claude Code to Google Ads with Google's official MCP server, read-only.
# Follows https://buildwire.ai/blog/how-to-connect-claude-to-google-ads-and-run-a-full-account-audit-in-one-command/
#
# Usage:
#   ./google-ads/setup.sh YOUR_GCP_PROJECT_ID /path/to/oauth-client.json [MANAGER_CUSTOMER_ID]
#
# Before running: in Google Cloud Console, enable the Google Ads API, check the
# project has Explorer/Basic/Standard access, and create a "Desktop app" OAuth
# client. Keep the downloaded JSON outside this repo.
set -euo pipefail

PROJECT_ID="${1:?Give your Google Cloud project ID}"
CLIENT_FILE="${2:?Give the path to your OAuth desktop client JSON}"
MANAGER_ID="${3:-}"
COMMIT="7452a9d49e3d350403f2610cd7125c60f6d05264"   # google-ads-mcp v0.0.6
HERE="$(cd "$(dirname "$0")" && pwd)"
TOOLS_CONFIG="$HERE/tools_config.yaml"

for cmd in gcloud pipx claude; do
  command -v "$cmd" >/dev/null || { echo "Missing: $cmd. Install it first."; exit 1; }
done
[ -f "$CLIENT_FILE" ] || { echo "OAuth client file not found: $CLIENT_FILE"; exit 1; }
[ -f "$TOOLS_CONFIG" ] || { echo "Missing $TOOLS_CONFIG"; exit 1; }

echo "Step 2: sign in to Google (a browser window opens)..."
gcloud auth application-default login \
  --scopes=https://www.googleapis.com/auth/adwords,https://www.googleapis.com/auth/cloud-platform \
  --client-id-file="$CLIENT_FILE"

ADC="${CLOUDSDK_CONFIG:-$HOME/.config/gcloud}/application_default_credentials.json"
[ -f "$ADC" ] || { echo "Could not find the saved credentials at $ADC. Pass the path gcloud printed."; exit 1; }

echo "Step 4: register the server with Claude Code (user scope)..."
claude mcp remove google-ads-mcp --scope user >/dev/null 2>&1 || true
EXTRA=()
[ -n "$MANAGER_ID" ] && EXTRA=(--env "GOOGLE_ADS_LOGIN_CUSTOMER_ID=$MANAGER_ID")
claude mcp add --transport stdio --scope user google-ads-mcp \
  --env "GOOGLE_PROJECT_ID=$PROJECT_ID" \
  --env "GOOGLE_APPLICATION_CREDENTIALS=$ADC" \
  --env "GOOGLE_ADS_MCP_TOOLS_CONFIG=$TOOLS_CONFIG" \
  "${EXTRA[@]}" \
  -- pipx run --spec "git+https://github.com/googleads/google-ads-mcp.git@$COMMIT" google-ads-mcp

claude mcp get google-ads-mcp
echo
echo "Done. Open Claude Code in this folder, type /mcp and check google-ads-mcp shows only:"
echo "  customers_list_accessible_customers, search_search, metadata_get_resource_metadata"
echo "Then paste the prompt from google-ads/AUDIT_PROMPT.md."
