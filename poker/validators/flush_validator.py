class FlushValidator():
    
    def __init__(self, cards):
        self.cards = cards
        self.name = "Flush"
    
    def is_valid(self):
        return len(self._suite_count_dict) == 1
    
    def valid_cards(self):
        return [card 
                for card in self.cards
                if card.suite in self._suite_count_dict
                 ]

    @property
    def _suite_count_dict(self):
        suite_count_dict = self.create_suite_count_dict
        return {
            suite:count
            for suite, count in suite_count_dict.items()
            if count >= 5
        }

    @property
    def create_suite_count_dict(self):
        card_suite_count = dict()
        for card in self.cards:
            '''
            setdefault(key, default value) sets the key
            to default value if that key is not
            present in dict
            '''
            card_suite_count.setdefault(card.suite, 0)
            card_suite_count[card.suite] += 1
        
        return card_suite_count     