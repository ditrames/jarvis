import re


class HomeAssistant:
    @classmethod
    def from_command_relations(cls, prefix, commands_relations):
        new_commands_relations = [
            ([
                '(?i){} {}'.format(prefix, command_str)
                for command_str in command_strs
            ], command) for (command_strs, command) in commands_relations
        ]
        print(new_commands_relations)
        return cls(new_commands_relations)

    def __init__(self, regexs_command_pairs):
        self.regexs_command_pairs = regexs_command_pairs

    def parse_string(self, string):
        span_matches = list()
        for (command_strings, command) in self.regexs_command_pairs:
            for command_str in command_strings:
                print(command_str)
                span_matches += list(
                    [(i.span(), command) for i in re.finditer(command_str, string)]
                )
        sorted(span_matches, key=lambda x: x[0][0])
        splice_data = []
        for i in range(len(span_matches)):
            splice_start = span_matches[i][0][1]
            splice_stop = span_matches[i+1][0][0] if i != len(span_matches)-1 else len(string)
            splice_data.append((slice(splice_start, splice_stop), span_matches[i][1]))

        return [splice_data, string]

    def run_commands(self, parsed_string):
        parsing_data, original_string = parsed_string
        for splice, command in parsing_data:
            if command:
                command(original_string[splice])
