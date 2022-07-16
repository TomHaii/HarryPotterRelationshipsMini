from models.character_relationships import CharacterRelationships


class Relationship:
    def __init__(self, viewpoint_char):
        self._viewpoint_char = viewpoint_char
        self.target_char_to_scores_dict = {}

    def insert_to_target_scores_array(self, target_char, scores_arr):
        self.target_char_to_scores_dict[target_char] = CharacterRelationships.char_relationship_average(scores_arr)

    def serialize(self):
        return {
            self._viewpoint_char: self.target_char_to_scores_dict
        }
