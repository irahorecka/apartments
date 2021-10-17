from apartments.url.base import Path, Param


class URL:
    domain_base = "https://apartments.com/"

    def __init__(self, *args, **kwargs):
        self.path = Path(*args, **kwargs)
        self.params = Param(*args, **kwargs)

    def url(self, new=False):
        """URL constructor. Takes one keyword argument to specify whether to query for
        new posts."""
        return "".join(
            (
                self.domain_base,
                self.path.get_path(is_new=new is not False),
                self.params.get_params(),
            )
        )
