class Reviewer:
    def __init__(self, mode="cli"):
        self.mode = mode

    def review(self, original: dict, suggestion: dict) -> bool:
        """
        Review Gemini suggestion.
        Returns True if accepted, False otherwise.
        """
        print("\n❌ Payload failed validation")
        print("Original:", original)
        print("💡 Suggested fix:", suggestion)

        if self.mode == "cli":
            choice = input("Accept fix? (y/n): ")
            return choice.lower().startswith("y")
        return False
