"""Internationalization (i18n) - UI translations for awsui."""

LANG_ZH_TW = {
    "search_placeholder": "搜尋 profiles (按 / 聚焦)...",
    "cli_placeholder": "輸入 AWS CLI 指令（開始輸入顯示建議，空白時 ↑↓ 瀏覽歷史）",
    "no_profiles": "未偵測到 profiles",
    "no_profiles_hint": "請執行 'aws configure sso-session' 或 'aws configure sso' 建立",
    "no_aws_cli": "未偵測到 AWS CLI v2",
    "no_aws_cli_hint": "請依官方文件安裝 AWS CLI v2",
    "detail_name": "名稱",
    "detail_kind": "類型",
    "detail_account": "帳號",
    "detail_role": "角色",
    "detail_region": "區域",
    "detail_session": "SSO Session",
    "panel_profiles": "Profiles",
    "panel_profiles_help": "搜尋與切換",
    "panel_detail": "Profile 詳情",
    "detail_placeholder": "選擇 profile 以顯示資料",
    "panel_cli": "CLI 終端",
    "panel_cli_help": "輸出與歷史",
    "panel_cli_input": "指令輸入",
    "app_subtitle": "Profile 切換與 CLI 助手",
    "authenticating": "驗證中...",
    "login_required": "需要登入",
    "login_success": "登入成功",
    "login_failed": "登入失敗",
    "login_cancelling": "取消登入中...",
    "login_cancelled": "登入已取消",
    "login_in_progress": "登入處理中，請稍候",
    "auth_success": "驗證成功",
    "auth_failed": "驗證失敗",
    "auth_cancelled": "驗證已取消",
    "whoami": "當前身份",
    "whoami_updated": "身份資訊已更新",
    "whoami_failed": "無法取得身份資訊",
    "whoami_account": "帳號",
    "whoami_arn": "ARN",
    "whoami_user": "使用者 ID",
    "no_login_task": "目前沒有登入作業",
    "select_profile_first": "請先選擇 profile",
    "panel_ai": "AI 助手",
    "panel_ai_help": "Amazon Q 開發助手",
    "ai_placeholder": "詢問 Amazon Q (例: 如何列出所有 S3 buckets?)",
    "ai_not_available": "Amazon Q CLI 不可用",
    "ai_install_hint": "請先安裝 Amazon Q Developer CLI",
    "ai_spinner_wait": "正在查詢 Amazon Q",
    "ai_spinner_done": "查詢完成",
    "ai_spinner_error": "查詢失敗",
    "ai_querying": "查詢中...",
    "ai_query_failed": "查詢失敗",
    "ai_cancelled": "已取消查詢",
    "whoami_checking": "正在取得身份資訊...",
    "search_first_result": "已選擇第一個結果，共 {count} 個符合",
    "search_no_results": "沒有符合的 profiles",
    "left_pane_shown": "左側面板已顯示",
    "cli_fullscreen": "CLI 滿版模式 - 按 t 恢復",
    "cli_mode": "CLI 模式",
    "ai_mode": "AI 模式",
    "output_cleared": "輸出已清空",
    "help_displayed": "說明已顯示",
    "region_override_wip": "Region override - 功能開發中",
    "login_loading": "登入 {profile}...",
    "profiles_loaded": "載入 {count} 個 profiles",
    "execute_success": "✓ 完成 ({duration}ms)",
    "execute_failure": "✗ 失敗 ({duration}ms)",
    "cli_error_exit": "✗ 錯誤 (exit code: {code}, {duration}ms)",
    "ai_error_exception": "✗ 發生錯誤: {error} ({duration}ms)",
    "cli_error_exception": "✗ 執行錯誤: {error}",
    "profile_none": "未選擇",
    "error_title": "錯誤",
    "cheatsheet_title": "AWS CLI Cheatsheet",
    "cheatsheet_dismiss": "按 Esc 或 q 關閉",
    "help_text": """[bold]快捷鍵說明:[/bold]

/ - 聚焦搜尋框
c - 切換到 CLI 模式
a - 切換到 AI 助手模式
t - 切換左側面板顯示/隱藏
h - 顯示 AWS CLI Cheatsheet
Enter - 套用選定的 profile
l - 強制執行 SSO login
w - 顯示當前身份 (WhoAmI)
Ctrl+L - 清空輸出區域
Ctrl+U - 清空輸入框
Esc - 離開輸入框
? - 顯示此說明
q - 離開程式

[bold]CLI 輸入框智慧導航:[/bold]

空白時：
  ↑↓ - 瀏覽歷史指令

瀏覽歷史時：
  ↑↓ - 繼續瀏覽（不會觸發 autocomplete）
  修改內容 - 自動離開歷史模式

輸入內容後有建議時：
  ↑↓ - 在 autocomplete 建議中選擇
  Enter - 確認選擇

輸入內容但沒建議時：
  ↑↓ - 瀏覽歷史指令

[bold]使用方式:[/bold]

1. 使用搜尋框過濾 profiles
2. 上下鍵選擇 profile
3. 按 c 進入 CLI 模式，或按 a 進入 AI 助手模式
4. CLI 模式：空白時按 ↑↓ 快速找歷史指令
5. CLI 模式：開始輸入，自動顯示建議（↑↓ 選擇）
6. AI 模式：直接輸入自然語言問題
7. Ctrl+U 快速清空輸入
8. 按 h 查看常用 AWS CLI 指令
9. 按 t 可隱藏左側面板，讓輸出區域滿版顯示""",
}

LANG_EN = {
    "search_placeholder": "Search profiles (press / to focus)...",
    "cli_placeholder": "AWS CLI command (type to see suggestions, use ↑↓ for history)",
    "no_profiles": "No profiles detected",
    "no_profiles_hint": "Please run 'aws configure sso-session' or 'aws configure sso'",
    "no_aws_cli": "AWS CLI v2 not detected",
    "no_aws_cli_hint": "Please install AWS CLI v2 per official documentation",
    "detail_name": "Name",
    "detail_kind": "Type",
    "detail_account": "Account",
    "detail_role": "Role",
    "detail_region": "Region",
    "detail_session": "SSO Session",
    "panel_profiles": "Profiles",
    "panel_profiles_help": "Search & switch",
    "panel_detail": "Profile Details",
    "detail_placeholder": "Select a profile to view details",
    "panel_cli": "Command Console",
    "panel_cli_help": "Output & history",
    "panel_cli_input": "Command Input",
    "app_subtitle": "Profile switcher & CLI helper",
    "authenticating": "Authenticating...",
    "login_required": "Login required",
    "login_success": "Login successful",
    "login_failed": "Login failed",
    "login_cancelling": "Cancelling login...",
    "login_cancelled": "Login cancelled",
    "login_in_progress": "Login already in progress",
    "auth_success": "Authentication successful",
    "auth_failed": "Authentication failed",
    "auth_cancelled": "Authentication cancelled",
    "whoami": "Current Identity",
    "whoami_updated": "Identity refreshed",
    "whoami_failed": "Unable to fetch identity",
    "whoami_account": "Account",
    "whoami_arn": "ARN",
    "whoami_user": "UserId",
    "no_login_task": "No login is currently running",
    "select_profile_first": "Select a profile first",
    "panel_ai": "AI Assistant",
    "panel_ai_help": "Amazon Q Developer",
    "ai_placeholder": "Ask Amazon Q (e.g., How to list all S3 buckets?)",
    "ai_not_available": "Amazon Q CLI not available",
    "ai_install_hint": "Please install Amazon Q Developer CLI first",
    "ai_spinner_wait": "Querying Amazon Q",
    "ai_spinner_done": "Query complete",
    "ai_spinner_error": "Query failed",
    "ai_querying": "Querying...",
    "ai_query_failed": "Query failed",
    "ai_cancelled": "Query cancelled",
    "whoami_checking": "Fetching identity...",
    "search_first_result": "Selected first result; {count} matches",
    "search_no_results": "No matching profiles",
    "left_pane_shown": "Left pane shown",
    "cli_fullscreen": "CLI fullscreen mode – press t to restore",
    "cli_mode": "Switched to CLI mode",
    "ai_mode": "Switched to AI mode",
    "output_cleared": "Output cleared",
    "help_displayed": "Help displayed",
    "region_override_wip": "Region override – coming soon",
    "login_loading": "Logging in to {profile}...",
    "profiles_loaded": "Loaded {count} profiles",
    "execute_success": "✓ Completed ({duration}ms)",
    "execute_failure": "✗ Failed ({duration}ms)",
    "cli_error_exit": "✗ Error (exit code: {code}, {duration}ms)",
    "ai_error_exception": "✗ Error: {error} ({duration}ms)",
    "cli_error_exception": "✗ Execution error: {error}",
    "profile_none": "No profile",
    "error_title": "Error",
    "cheatsheet_title": "AWS CLI Cheatsheet",
    "cheatsheet_dismiss": "Press Esc or q to close",
    "help_text": """[bold]Keyboard Shortcuts:[/bold]

/ - Focus search box
c - Switch to CLI mode
a - Switch to AI assistant mode
t - Toggle left pane visibility
h - Show AWS CLI Cheatsheet
Enter - Apply selected profile
l - Force SSO login
w - Show current identity (WhoAmI)
Ctrl+L - Clear output area
Ctrl+U - Clear input field
Esc - Exit input field
? - Show this help
q - Quit

[bold]CLI Input Smart Navigation:[/bold]

When empty:
  ↑↓ - Browse command history

While browsing history:
  ↑↓ - Continue browsing (won't trigger autocomplete)
  Type - Exit history mode

When input has content with suggestions:
  ↑↓ - Select from autocomplete suggestions
  Enter - Confirm selection

When input has content without suggestions:
  ↑↓ - Browse command history

[bold]Quick Start:[/bold]

1. Use search box to filter profiles
2. Use ↑↓ keys to select profile
3. Press c for CLI mode, or press a for AI mode
4. CLI mode: Press ↑↓ when empty to browse history
5. CLI mode: Start typing to see suggestions (↑↓ to select)
6. AI mode: Enter natural language questions
7. Press Ctrl+U to quickly clear input
8. Press h to view common AWS CLI commands
9. Press t to hide left pane for fullscreen output""",
}
