class Item:

    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):

        condition_descriptions = {
            "0": "No condition provided",
            "0.5": "Not great",
            "1": "Meh",
            "1.5": "Existent",
            "2": "Passable",
            "2.5": "Okayish",
            "3": "Decent",
            "3.5": "Pretty good",
            "4": "Great",
            "4.5": "Like new",
            "5": "Perfection"
        }
        return condition_descriptions[str(self.condition)]
