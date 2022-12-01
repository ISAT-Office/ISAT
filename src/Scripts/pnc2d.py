#!I:\ISAT-2022\ISAT_code\ISATv2020final\src\python.exe
# Run this script with pnc options


def main():
    from PseudoNetCDF.pncparse import pncparse, getparser
    from PseudoNetCDF.plotutil.pnc2d import make2ds
    parser = getparser(has_ofile=True, plot_options=True, interactive=True)
    parser.add_argument('--swapaxes', action='store_true',
                        help='Swap x-y axes')
    ifiles, args = pncparse(
        has_ofile=True, plot_options=True, interactive=True, parser=parser)
    make2ds(args)


if __name__ == '__main__':
    main()
