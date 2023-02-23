import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}
    Site = Site(**config)
    Site.build()
typer.run(main())