# Boosted Magics

Python package that extends the magics of metakernel to provide TAB completion (complete_request messages) on arguments of the magic.

> Supports :
>
> - argument name completion
> - argument value completion, with custom `completer` function
> - parsing of magic command line with argparse

```bash
pip install boosted-magics
```

## Creating a Boosted Magic

Boosted Magic subclasses Metakernel Magic, so the magic declaration is the same. To have argument completion, you have to replace @option decorator of Magic with a @boosted_option, as below :

```python
from boosted_magics import boosted_option, BoostedMagic


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
        completer=lambda w, r: ["customa1", "customa2"],
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
```

The boosted_option uses [argparse](https://docs.python.org/3/library/argparse.html) under the hood for parsing (replacing optparse of metakernel), at command execution time. Hence, any parameter that you would give to an [argparse argument](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) will work for a boosted_option.

> This allows flags (`action='store_true'`), ...

For argument completion, boosted_magics uses statikomand, a custom package that mimics argparse mechanism for uncomplete commands. Completion is then proposed only for arguments that are not present on the command line.

You can create a custom completer function, that will be called just after you added the argument name (see example above). However, you will have to type at least the first letter of the argument value to get completion proposals.

## Troubleshooting

TAB completion for magic can be broken (some completion erase all line) with older metakernel versions (before 1.0.4). To fix it, install the 1.0.4 (or above) manually within the project that uses boosted-magics :

```bash
uv add "metakernel @ git+https://github.com/Calysto/metakernel.git@afd3ddd"
```

or without `uv`:

```bash
git clone https://github.com/Calysto/metakernel
cd metakernel
git checkout afd3ddd
pip install -e .
cd ..
```
