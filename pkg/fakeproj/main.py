from fakeproj.subprojone.dingus import dingus
import click


# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('printme')
#     args = parser.parse_args()
#     print(args.printme)

# @click.group()
# def main(**kwargs):
#     pass


# @main.command()
# @click.argument('printme')
# def printme(**kwargs):
#     print(kwargs['printme'])


@click.command()
@click.argument('printme')
def main(printme):
    print(dingus(printme))

if __name__ == "__main__":
    main()
