#!I:\ISAT-2022\ISAT_code\ISATv2020final\src\python.exe


def main():
    from PseudoNetCDF.pncparse import getparser, pncparse
    from PseudoNetCDF.plotutil.pncts import plotts
    parser = getparser(plot_options=True, has_ofile=True)
    parser.epilog += """
    -----
box.py inobs inmod target [target ...]
inobs - path to obs
inmod - path to mod
target - variable name
"""
    ifiles, args = pncparse(plot_options=True, has_ofile=True, parser=parser)
    plotts(args)


if __name__ == '__main__':
    main()
