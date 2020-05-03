import os


class FileCommands:
    @staticmethod
    def compose_move_command(company_name, date, filename):
        new_filename = FileCommands.new_filename2(company_name, date, filename)
        command = f'mv "{filename}" {new_filename}'
        return command

    @staticmethod
    def new_filename2(company_name, date, filename):
        # Parse relative or absolute path
        path_parts = filename.split("/")
        base_name = path_parts[-1]
        rest = "/".join(path_parts[0:-1])

        # My custom format
        new_filename = " - ".join([date, company_name, base_name])

        new_filename = f'"{"/".join([rest, new_filename])}"'
        return new_filename

    @staticmethod
    def write_if(command, file):
        if file is not None:
            with open(file, 'w') as file:
                file.write(command + '\n')

    def preview(self, original_filename):
        # Open
        os.system(f'open "{original_filename}"')
