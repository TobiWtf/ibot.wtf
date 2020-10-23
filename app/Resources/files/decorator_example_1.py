## This example is based off of
## iFunny user Affects decorator for
## CleverBot, i have improved it to a
## Degree and rewritten many of its features

# This will not include the other modules
# involved

from commands import strings
import libs.typing as typing

class commands_container(type):
    commands: dict = {} ## Dict of commands Functions
    commands_help: dict = {} ## Dict of commands aliases with help
    mode: dict = {} ## Dict of aliases with Mode.Type

    @classmethod
    def add(self, aliases: (list, str), function) -> typing.decorator:
        if isinstance(aliases, str):
            aliases: list = [aliases] ## Checks the type of alias arg
        assert isinstance(aliases, list),
            strings.function_string_or_list(function.__name__)
        for alias in aliases: ## Iterates over alias args
            assert not self.commands.get(alias),
                strings.function_already_exists(function.__name__, alias)
            self.commands[alias]: typing.function = function

    @classmethod
    def help(self, aliases: (list, str), message: str) -> typing.decorator:
        if isinstance(aliases, str):
            aliases: list = [aliases] ## Checks alias type
        for alias in aliases: ## Iterates over alias args
            self.commands_help[alias]: str = message

    @classmethod
    def add_mode(self, aliases: (list, str), mode: str) -> typing.decorator:
        if isinstance(aliases, str):
             aliases: list = [aliases,]
        for alias in aliases: ## Iterates over aliases
            data: str = self.mode.get(mode)
            if data: ## ^^ Checks if mode and < if mode,
                data.append(alias) ## Appends an alias
                self.mode[mode]: str = data
            else: ## Passes alias arg
                self.mode[mode]: list = [alias,]

    def __getitem__(self, index) -> typing.decorator:
        return self.commands.get(index) ## Item __get__ method


class pool(metaclass=commands_container):
    pass ## Container for Commands Decorator


def command(*args, **kwargs) -> typing.decorator:
    def decorator(function) -> typing.decorator:
        aliases: list = [] ## Alias list
        if kwargs.get(strings.names_argument): ## Checks for "Name" arg
            aliases.extend(kwargs[strings.names_argument]) ## Extends name arg
        else: raise f"Please provide a command name for {function.__name__}"
        if kwargs.get(strings.help_argument): ## Checks for help arg
            pool.help(aliases, kwargs[strings.help_argument]) ## Help arg
        if kwargs.get(strings.mode_argument): ## Checks for mode arg
            pool.add_mode(aliases, kwargs[strings.mode_argument])
        pool.add(aliases, function) ## Pools command and function
        return function

    return decorator ## Returns decorator Function without () initialization




command(names:list =["help", "e"], mode: str ="Everyone",
        help: str ="Provides help message")
def _help(ctx):
    ## --------------------------------------------------------------------
    ## You can now use this command with <PREFIX>help, <PREFIX>e           |
    ## Mode everyone allows you to disctate what type of command           |
    ## it is, this is useful for help menus, keeping people out of certain |
    ## commands, and many other tasks                                      |
    ## Help, provides a help message tagges with <help> and <e> in a dict  |
    ## This is amazing for help messages, ect                              |
    ## --------------------------------------------------------------------
    pass
