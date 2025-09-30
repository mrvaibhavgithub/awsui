"""Custom autocomplete widget for AWS CLI commands."""

from textual.widgets import OptionList
from textual.widgets.option_list import Option
from textual.message import Message


class CommandAutocomplete(OptionList):
    """Enhanced autocomplete with fuzzy matching and highlighting."""

    class CommandSelected(Message):
        """Message sent when a command is selected from autocomplete."""

        def __init__(self, command: str) -> None:
            self.command = command
            super().__init__()

    def __init__(self, commands: list[str], command_categories: dict[str, str], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_commands = commands
        self.command_categories = command_categories
        self.filtered_commands: list[str] = []
        self.display = False  # Hidden by default
        self.can_focus = False  # Don't steal focus from Input

    def fuzzy_match(self, text: str, query: str) -> tuple[bool, int]:
        """
        Check if query fuzzy matches text with scoring.
        Returns (matched, score) where higher score = better match.
        """
        text_lower = text.lower()
        query_lower = query.lower()

        # Exact substring match - highest score
        if query_lower in text_lower:
            # Score based on position (earlier is better)
            position = text_lower.find(query_lower)
            score = 100 - (position * 2)
            return (True, max(score, 80))

        # Fuzzy match - all chars in order
        text_idx = 0
        query_idx = 0
        matches = 0

        while text_idx < len(text_lower) and query_idx < len(query_lower):
            if text_lower[text_idx] == query_lower[query_idx]:
                matches += 1
                query_idx += 1
            text_idx += 1

        if query_idx == len(query_lower):
            # All query chars found in order
            score = int((matches / len(text_lower)) * 60)
            return (True, max(score, 20))

        return (False, 0)

    def highlight_match(self, text: str, query: str) -> str:
        """Highlight matching substring in text."""
        if not query:
            return text

        lower_text = text.lower()
        lower_query = query.lower()
        start = lower_text.find(lower_query)

        if start >= 0:
            end = start + len(query)
            return f"{text[:start]}[bold yellow]{text[start:end]}[/]{text[end:]}"

        return text

    def filter_commands(self, query: str) -> None:
        """Filter commands with fuzzy matching and scoring."""
        if not query or len(query) < 2:
            self.display = False
            self.filtered_commands = []
            self.clear_options()
            return

        # Fuzzy match with scores
        matches = []
        for cmd in self.all_commands:
            matched, score = self.fuzzy_match(cmd, query)
            if matched:
                matches.append((cmd, score))

        if matches:
            # Sort by score (highest first)
            matches.sort(key=lambda x: x[1], reverse=True)
            self.filtered_commands = [cmd for cmd, _ in matches[:10]]

            self.clear_options()
            for cmd in self.filtered_commands:
                # Get category for badge
                category = self.command_categories.get(cmd, "")
                if category:
                    # Shorten category name for badge
                    badge_text = category.split("/")[0][:4].upper()
                    badge = f"[dim cyan]{badge_text}[/dim cyan]"
                else:
                    badge = ""

                # Highlight matching substring
                highlighted = self.highlight_match(cmd, query)

                # Create option with badge and highlighted command
                label_text = f"{badge} {highlighted}" if badge else highlighted
                self.add_option(Option(label_text, id=cmd))

            self.display = True
            if len(self.filtered_commands) > 0:
                self.highlighted = 0  # Select first item
        else:
            self.display = False
            self.filtered_commands = []
            self.clear_options()

    def get_selected_command(self) -> str | None:
        """Get currently highlighted command."""
        if self.highlighted is not None and 0 <= self.highlighted < len(self.filtered_commands):
            return self.filtered_commands[self.highlighted]
        return None

    def move_cursor_down(self) -> None:
        """Move selection down."""
        if self.filtered_commands and self.highlighted is not None:
            self.highlighted = min(self.highlighted + 1, len(self.filtered_commands) - 1)

    def move_cursor_up(self) -> None:
        """Move selection up."""
        if self.filtered_commands and self.highlighted is not None:
            self.highlighted = max(self.highlighted - 1, 0)