def Chkdpk():
    print('Checking dependencies...')
    a = 0
    errorL = []
    try:
        import source
    except Exception as errorS:
        print('The source file is missing or corrupted. please check your downloads')
        a += 1
        errorL.append(str(errorS))

    try:
        import sys
    except Exception as errorS:
        print(
            a, '\t', 'A python [sys] package is missing. install package to continue ')
        a += 1
        errorL.append(str(errorS))

    try:
        import time

    except Exception as errorS:
        print(
            a, '\t', 'A python [time] package is missing. install package to continue ')
        a += 1
        errorL.append(str(errorS))

    try:
        import mysql.connector

    except Exception as errorS:
        print(
            a, '\t', 'A python [mysql] package is missing. install package to continue ')
        a += 1
        errorL.append(str(errorS))
    try:
        import os

    except Exception as errorS:
        print(
            a, '\t', 'A python [os] package is missing. install package to continue ')
        a += 1
        errorL.append(str(errorS))
    try:
        import maskpass

    except Exception as errorS:
        print(
            a, '\t', 'A python [maskpass] package is missing. install package to continue ')
        a += 1
        errorL.append(str(errorS))
    try:
        import Config
    except Exception as errorS:
        print('Config file is missing or corrupted. check your files for missing or corrupted ones.')
        a += 1
        errorL.append(str(errorS))
        print(errorS)
    try:
        from Config1 import save1 as save1
    except Exception as errorS:
        print('Config1 file is missing or corrupted. check your files for missing or corrupted ones')
        a += 1
        errorL.append(str(errorS))
        print(errorS)

    try:
        from Config import keys_stored as keys
    except Exception as errorS:
        print('Config file is missing or corrupted. check your files for missing or corrupted ones.')
        a += 1
        errorL.append(str(errorS))

    if len(errorL) > 0:
        showErr = input('Show list of errors? [Y] [N]\n ')
        if showErr.lower() == 'y':
            c = 0
            for b in errorL:
                c += 1
                print(c, '\t', b, '\n')
        return 0


Chk = Chkdpk()
if Chk != 0:
    import source
    source.run()
