import io


class ParseHelpers:
    @staticmethod
    def parse_characters(character_file):
        characters = io.open(character_file, 'rt', encoding='utf-8', newline='\n').readlines()
        characters_no_backspaces = [character.replace('\n', '') for character in characters]
        return characters_no_backspaces