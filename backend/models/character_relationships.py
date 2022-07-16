INDEX_BOUND_GAP_CONST = 50


class CharacterRelationships:
    @staticmethod
    def create_relationship(viewpoint_char, target_char):
        viewpoint_char.relationship_scores_to_target_char[target_char.character_name] = []

        for book_num in list(range(7)):
            instances = 0
            view_char_to_target_char_score_list = []
            view_char_to_target_char_score_set = {}
            upper_bound = 1
            for app_index in viewpoint_char.appearances_by_book[book_num + 1]:
                indlow = app_index - INDEX_BOUND_GAP_CONST
                indhigh = app_index + INDEX_BOUND_GAP_CONST

                for index in target_char.appearances_by_book[book_num + 1]:
                    if indlow <= index <= indhigh:
                        instances += 1
                        view_char_to_target_char_score_list.append([app_index, index])

                upper_bound = float(len(viewpoint_char.appearances_by_book[book_num + 1]))
                view_char_to_target_char_score_set = {x[0] for x in view_char_to_target_char_score_list}

            relationship_score = "%.2f" % ((len(view_char_to_target_char_score_set) / upper_bound) * 100)
            if target_char.character_name in viewpoint_char.relationship_scores_to_target_char:
                viewpoint_char.relationship_scores_to_target_char[target_char.character_name].append(relationship_score)
            else:
                viewpoint_char.relationship_scores_to_target_char[target_char.character_name] = []

    @staticmethod
    def char_relationship_average(scores_arr):
        sum_score = sum(list(map(float, scores_arr)))
        average_score = "%.2f" % (float(sum_score) / 7.0)
        return average_score
