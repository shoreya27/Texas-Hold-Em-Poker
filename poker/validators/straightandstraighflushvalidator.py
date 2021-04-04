

class StraightAndStraighFlushValidator():

    @property
    def _get_collection_of_straight_cards(self):
        start_index = 0
        final_index = len(self.cards)-1
        collection_of_straight_cards = []

        while start_index + 4 <= final_index:
            cards = self.cards[start_index:start_index+5]
            if self._straight(cards):
                collection_of_straight_cards.append(cards)
            start_index += 1
        
        return collection_of_straight_cards

    def _straight(self, cards):

        rank_indexes = [card.rank_index for card in cards]
        starting_end = rank_indexes[0]
        ending       = rank_indexes[-1] + 1
        rank_indexes_range = list(
                            range(starting_end,ending)
                                )
        return rank_indexes == rank_indexes_range