import json

from models.book import Book
from models.character import Character
from models.character_relationships import CharacterRelationships
from models.relationship import Relationship
from utils.parse_helpers import ParseHelpers

if __name__ == '__main__':

    # Parse the books and characters initialize a object for each one of them
    hp1 = Book('resources/HPBook1.txt')
    hp2 = Book('resources/HPBook2.txt')
    hp3 = Book('resources/HPBook3.txt')
    hp4 = Book('resources/HPBook4.txt')
    hp5 = Book('resources/HPBook5.txt')
    hp6 = Book('resources/HPBook6.txt')
    hp7 = Book('resources/HPBook7.txt')
    hp_books_list = [hp1.words, hp2.words, hp3.words, hp4.words, hp5.words, hp6.words, hp7.words]
    all_hp_characters = ParseHelpers.parse_characters(character_file='resources/harry_potter_characters.txt')

    chars_objects = []
    viewpoint_char_relationships_dict = {}

    # Create all the character objects and initialize their appearances dict based by books.
    for character in all_hp_characters:
        viewpoint_char_relationships_dict[character] = Relationship(character)
        first_name_alias = character.split(' ')[0]
        new_char = Character(character)
        new_char.add_aliases([first_name_alias])
        new_char.populate_appearances_dict(hp_books_list)
        chars_objects.append(new_char)

    # Go over every character and generate the relationship between every character in the books
    for viewpoint_char in chars_objects:
        target_chars = filter(lambda c: c.character_name != viewpoint_char.character_name, chars_objects)
        for target_char in target_chars:
            CharacterRelationships.create_relationship(viewpoint_char, target_char)
            scores_arr = viewpoint_char.relationship_scores_to_target_char[target_char.character_name]
            viewpoint_char_relationships_dict[viewpoint_char.character_name].insert_to_target_scores_array(
                target_char.character_name, scores_arr)

    # Serialize the data to json object
    relationships_object_res = []
    for viewpoint_char in viewpoint_char_relationships_dict:
        json_obj = viewpoint_char_relationships_dict[viewpoint_char].serialize()
        relationships_object_res.append(json_obj)

    # Dump the data to a results file
    with open('results.json', 'w') as fp:
        json.dump(relationships_object_res, fp)
