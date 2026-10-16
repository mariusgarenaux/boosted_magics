from test_boosted_kernel import TestKernel
from boosted_magics import boosted_option, BoostedMagic


def my_completer(word, rank):
    return ["customa1", "customa2"]


class ExampleMagic(BoostedMagic):
    @boosted_option(
        "--very_long_option",
        "-o",
        default=None,
        help="This is a very long option name",
    )
    @boosted_option(
        "--an_other_option_but_which_is_a_flag",
        default=None,
        action="store_true",
        help="This is an other option",
    )
    @boosted_option(
        "-a",
        "--an_option_with_custom_completion_method",
        help="An option with custom completion method",
        completer=my_completer,
    )
    def line_example(
        self,
        very_long_option,
        an_other_option_but_which_is_a_flag,
        an_option_with_custom_completion_method,
    ):
        """
        %example : try the boosted magic completion
        """
        self.kernel: TestKernel
        self.kernel.Print(
            f"Example magic successfully called, with args :\n• very_long_option : {very_long_option}\n• an_other_option : {an_other_option_but_which_is_a_flag}\n• an_option_with_custom_completion_method : {an_option_with_custom_completion_method}"
        )


def register_magics(kernel) -> None:
    kernel.register_magics(ExampleMagic)
