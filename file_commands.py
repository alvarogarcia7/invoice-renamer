class FileCommands:
    @staticmethod
    def compose_move_command(args, company_name, date):
        new_filename = " - ".join([date, company_name, args.file])
        new_filename = f'"{new_filename}"'
        command = f'mv "{args.file}" {new_filename}'
        return command

    @staticmethod
    def write_if(command, file):
        if file is not None:
            with open(file, 'w') as file:
                file.write(command + '\n')