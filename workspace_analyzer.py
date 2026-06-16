class WorkspaceAnalyzer:

    def __init__(self):

        self.templates = {

            "auction": [
                "users",
                "auctions",
                "bids",
                "payments"
            ],

            "hospital": [
                "patients",
                "doctors",
                "appointments",
                "billing"
            ],

            "freelancer": [
                "users",
                "jobs",
                "proposals",
                "payments",
                "reviews"
            ],

            "ecommerce": [
                "products",
                "orders",
                "customers",
                "payments"
            ],

            "chat": [
                "users",
                "messages",
                "rooms",
                "authentication"
            ]
        }

    def analyze(self, idea):

        idea = idea.lower()

        for keyword, modules in (
            self.templates.items()
        ):

            if keyword in idea:

                return modules

        return [
            "backend",
            "frontend",
            "database"
        ]


if __name__ == "__main__":

    analyzer = WorkspaceAnalyzer()

    idea = input(
        "Project Idea: "
    )

    modules = analyzer.analyze(
        idea
    )

    print(
        "\nDetected Modules:"
    )

    for module in modules:

        print(
            f"- {module}"
        )