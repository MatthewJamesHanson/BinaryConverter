"""
This program converts binary numbers to decimal, decimal to binary.
"""


# Displays binary numbers as #### ####.######... (up to 268435456, then #########.#####...)
def binarySpacing(binaryResult, decimalFloat):
    binaryListed = []

    for i in binaryResult:
        binaryListed.append(i)

    if decimalFloat < 256:
        while len(binaryListed) < 8:
            binaryListed.insert(0, '0')

        binary4 = binaryListed[0:4]
        binary8 = binaryListed[4:8]
        output = ''.join(binary4) + ' ' + ''.join(binary8)

    elif decimalFloat >= 256 and decimalFloat < 4096:
        while len(binaryListed) < 12:
            binaryListed.insert(0, '0')

        binary4 = binaryListed[0:4]
        binary8 = binaryListed[4:8]
        binary12 = binaryListed[8:12]
        output = ''.join(binary4) + ' ' + ''.join(binary8) + ' ' + ''.join(binary12)

    elif decimalFloat >= 4096 and decimalFloat < 65536:
        while len(binaryListed) < 16:
            binaryListed.insert(0, '0')

        binary4 = binaryListed[0:4]
        binary8 = binaryListed[4:8]
        binary12 = binaryListed[8:12]
        binary16 = binaryListed[12:16]
        output = ''.join(binary4) + ' ' + ''.join(binary8) + ' ' + ''.join(binary12) + ' ' + ''.join(binary16)

    elif decimalFloat >= 65536 and decimalFloat < 16777216:
        while len(binaryListed) < 20:
            binaryListed.insert(0, '0')

        binary4 = binaryListed[0:4]
        binary8 = binaryListed[4:8]
        binary12 = binaryListed[8:12]
        binary16 = binaryListed[12:16]
        binary20 = binaryListed[16:20]
        output = ''.join(binary4) + ' ' + ''.join(binary8) + ' ' + ''.join(binary12) + ' ' + ''.join(binary16) \
                 + ' ' + ''.join(binary20)

    elif decimalFloat >= 16777216 and decimalFloat < 268435456:
        while len(binaryListed) < 24:
            binaryListed.insert(0, '0')

        binary4 = binaryListed[0:4]
        binary8 = binaryListed[4:8]
        binary12 = binaryListed[8:12]
        binary16 = binaryListed[12:16]
        binary20 = binaryListed[16:20]
        binary24 = binaryListed[20:24]
        output = ''.join(binary4) + ' ' + ''.join(binary8) + ' ' + ''.join(binary12) + ' ' + ''.join(binary16) \
                 + ' ' + ''.join(binary20) + ' ' + ''.join(binary24)

    else:
        output = binaryResult

    return output


# Ensures a valid decimal input
def inputValidDecimal(prompt):
    while True:
        decimal = input(prompt)

        try:
            decimalFloat = float(decimal)

        except:
            print('Invalid input. Try again.')
            continue

        return decimalFloat


# Ensures a valid binary input
def inputValidBinary(prompt, sign):
    while True:
        validBinary = input(prompt)

        if '2' in validBinary or '3' in validBinary or '4' in validBinary \
               or '5' in validBinary or '6' in validBinary or '7' in validBinary \
               or '8' in validBinary or '9' in validBinary:
            print('Invalid input. Binary must be 1s and 0s only.')
            continue

        if sign == 'Signed':
            if '.' in validBinary:
                print('Signed binary cannot have fractional parts; leave out the \'.\'')
                continue

            if len(validBinary) == 8 or len(validBinary) == 16:
                return validBinary

            else:
                print('Invalid length. Signed binary must have 8 or 16 digits.\n'
                      'e.g. enter \"11001100\" or \"1100110011001100\"\n*Do not enter spacing e.g. 1000 1000\n'
                      + '*Do not enter binary fractions e.g. 11011101.11001')
                continue

        return validBinary


# Converts decimal to binary
def dec2BinUnsigned(decimalFloat, wholeDecimal, fractionDecimal, positiveNumberCheck):
    binaryWhole = ''

    if decimalFloat == 0:
        print(' 0.0')

    else:
        if positiveNumberCheck == 'Negative_Number':
            sign = '-'

            # Converts decimal whole to binary whole
            remainderList = []

            while wholeDecimal > 0:
                a = str(int(wholeDecimal % 2))
                remainderList.insert(0, a)

                if wholeDecimal % 2 == 1:
                    wholeDecimal = (wholeDecimal / 2) - 0.5

                else:
                    wholeDecimal = wholeDecimal / 2

            binaryWhole = ''.join(remainderList)

        else:
            sign = ' '

            # Converts decimal whole to binary whole
            remainderList = []

            while wholeDecimal > 0:
                a = str(int(wholeDecimal % 2))
                remainderList.insert(0, a)

                if wholeDecimal % 2 == 1:
                    wholeDecimal = (wholeDecimal / 2) - 0.5

                else:
                    wholeDecimal = wholeDecimal / 2

            binaryWhole = ''.join(remainderList)

        # Converts decimal fraction to binary fraction
        binaryFraction = ['0']

        if fractionDecimal > 0:
            binaryFraction = []

            while fractionDecimal < 1 and fractionDecimal > 0:
                if fractionDecimal * 2 > 1:
                    binaryFraction.append('1')
                    fractionDecimal = (fractionDecimal * 2) - 1

                elif fractionDecimal * 2 < 1:
                    binaryFraction.append('0')
                    fractionDecimal = fractionDecimal * 2

                elif fractionDecimal * 2 == 1:
                    binaryFraction.append('1')
                    fractionDecimal = 666  # ends 'while' loop

            while len(binaryFraction) < 16:
                binaryFraction.append('0')

        binaryFraction = ''.join(binaryFraction)

        unsignedBin = binarySpacing(binaryWhole, decimalFloat) + '.' + binaryFraction[0:16]
        dec2UnsignedBinDict = {'unsignedBin': unsignedBin, 'sign': sign}
        result = str(dec2UnsignedBinDict['sign'] + dec2UnsignedBinDict['unsignedBin'])

        return result


# Converts unsigned binary to signed binary
def binUnsigned2BinSigned(inputBinary):
    binaryListed = []
    wholeBinary = inputBinary['wholeBinary']
    fractionBinary = inputBinary['fractionBinary']
    binaryFloat = inputBinary['binaryFloat']

    # Converting positive 8bit decimals
    if binaryListed[0] == '0':
        binaryFloat = ''.join(binaryListed)
        return inputBinary

    # Converting negative 8 bit decimals
    elif binaryListed[0] == '1':
        binaryListedString = ''.join(binaryListed)

        for i in binaryListedString:
            a = binaryListedString.replace('0', 'x')
            b = a.replace('1', '0')
            c = b.replace('x', '1')

        if c[7] == '0':
            c = list(c)
            c[7] = '1'

        elif c[7] == '1':
            c = list(c)
            c[7] = '0'

            if c[6] == '0':
                c = list(c)
                c[6] = '1'

            elif c[6] == '1':
                c = list(c)
                c[6] = '0'

                if c[5] == '0':
                    c = list(c)
                    c[5] = '1'

                elif c[5] == '1':
                    c = list(c)
                    c[5] = '0'

                    if c[4] == '0':
                        c = list(c)
                        c[4] = '1'

                    elif c[4] == '1':
                        c = list(c)
                        c[4] = '0'

                        if c[3] == '0':
                            c = list(c)
                            c[3] = '1'

                        elif c[3] == '1':
                            c = list(c)
                            c[3] = '0'

                            if c[2] == '0':
                                c = list(c)
                                c[2] = '1'

                            elif c[2] == '1':
                                c = list(c)
                                c[2] = '0'

                                if c[1] == '0':
                                    c = list(c)
                                    c[1] = '1'

                                elif c[1] == '1':
                                    c = list(c)
                                    c[1] = '0'

                                    if c[0] == '0':
                                        c = list(c)
                                        c[0] = '1'
                                        digitListWhole = []
                                        cString = ''.join(c)
                                        answerWhole = 0

                                        for i in cString:
                                            digitListWhole.insert(0, int(i))

                                        for digit, value in enumerate(digitListWhole):
                                            answerWhole += 2 ** digit * value

                                        answerWhole = str(answerWhole)
                                        answerWhole = float(answerWhole)
                                        print('Decimal: -', answerWhole, 'Binary:  ', binary, '\n', sep='')

                                    elif c[0] == '1':
                                        c = list(c)
                                        c[0] = '0'
                                        print(c, 'b')
                                        digitListWhole = []
                                        cString = ''.join(c)
                                        answerWhole = 0

                                        for i in cString:
                                            digitListWhole.insert(0, int(i))

                                        for digit, value in enumerate(digitListWhole):
                                            answerWhole += 2 ** digit * value

                                        answerWhole += 128
                                        answerWhole = str(answerWhole)
                                        answerWhole = float(answerWhole)
                                        print('Decimal: -', answerWhole, 'Binary:  ', binaryFloat, '\n', sep='')


# Converts unsigned binary to decimal
def binUnsigned2Dec(wholeBinary, fractionBinary, numberValenceCheck):
    if numberValenceCheck == 'negativeNumber':
        signToDisplay = '-'

    else:
        signToDisplay = ' '

    # Converts whole binary to whole decimal
    if wholeBinary == 0:
        answerWhole = 0

    else:
        digitListWhole = []
        answerWhole = 0

        for i in str(wholeBinary):
            digitListWhole.insert(0, int(i))

        for digit, value in enumerate(digitListWhole):
            answerWhole += 2 ** digit * value

    # Converts fraction binary to fraction decimal
    if fractionBinary == 1:
        decimalFractionFinal = 0.5
    else:
        fractionBinary = int(fractionBinary * (10 ** (len(str(fractionBinary)) - 2)))

        if wholeBinary == 0 and len(str(fractionBinary)) > len(str(fractionBinary)) + 1:
            fractionBinary = int(fractionBinary * (10 ** (len(str(fractionBinary)))))

        else:
            fractionBinary = int(fractionBinary * (10 ** (len(str(fractionBinary)))))

        if fractionBinary > 0:
            fractionBinary = str(fractionBinary)
            digitListNumerator = []

            for i in str(fractionBinary):
                digitListNumerator.insert(0, int(i))

            answerNumerator = 0

            for digit, value in enumerate(digitListNumerator):
                answerNumerator += (2 ** digit) * value
            denominator = 2 ** (len(fractionBinary))

        else:
            answerNumerator = 0
            denominator = 1  # Easy way to avoid finding len(fractionBinary) when it's 0

        # computes and prints whole and fraction parts of binary conversion together as string
        decimalFractionFinal = str(answerNumerator / denominator)

    result = signToDisplay + str(answerWhole) + '.' + str(decimalFractionFinal)[2:]

    return result


import numbers
from decimal import Decimal
import string

print('WELCOME TO BINARY CONVERTER\n101010101010101010101010101\n')

while True:
    choice = input('[0] - Convert from decimal\n[1] - '
                   + 'Convert from unsigned binary\n[11] - '
                   + 'Convert from signed binary\n\n[h]elp - '
                   + 'Explanation of signed/unsigned binary\n[i]nfo - '
                   + 'Information about this program\n\nCHOICE: ').lower()

    if choice == '0':
        inputDecimal = inputValidDecimal('\nEnter a decimal number: ')

        if str(inputDecimal)[0] == '-':
            positiveNumberCheck = 'Negative_Number'

        else:
            positiveNumberCheck = 'Positive_Number'

        decimal = str(inputDecimal).lstrip('-')

        if decimal[0] == '.':
            decimal = '0' + decimal

        if '.' not in str(inputDecimal):
            decimal = decimal + '.0'

        decimalFloat = float(decimal)
        wholeDecimal = int(decimalFloat)
        fractionDecimal = round(decimalFloat - wholeDecimal, len(str(decimal)) - len(str(wholeDecimal)) + 1)
        unsignedResult = dec2BinUnsigned(decimalFloat, wholeDecimal, fractionDecimal, positiveNumberCheck)
        #signedResult = binSigned2binUnsigned(dec2BinUnsigned(decimalFloat, wholeDecimal,
                  #                           fractionDecimal, positiveNumberCheck))

        print('\tDecimal:', inputDecimal,
              '\n\tSigned Binary:', # signedResult
              '\n\tUnsigned Binary:', unsignedResult, '\n')

    elif choice == '1':
        inputBinary = inputValidBinary('\nEnter a binary number: ', 'Unsigned')

        # Checks for positive or negative input
        numberValenceCheck = 'positiveNumber'

        if '-' == inputBinary[0]:
            numberValenceCheck = 'negativeNumber'
            signToDisplay = '-'

        else:
            signToDisplay = ' '

        binary = inputBinary.lstrip('-')
        binaryFloat = float(binary)
        wholeBinary = int(binaryFloat)
        fractionBinary = int(str(round(binaryFloat - wholeBinary, len(binary) - len(str(wholeBinary)) + 1))[2:])
        decimalResult = binUnsigned2Dec(wholeBinary, fractionBinary, numberValenceCheck)
        signedResult = ''

        print('\tUnsigned binary: ', inputBinary,
              '\n\tSigned binary:', signedResult,
              '\n\tDecimal:', decimalResult, '\n', sep='')

    elif choice == '11':
        inputSignedBinary = inputValidBinary('\nEnter a binary number: ', 'Signed')

        if inputSignedBinary[0] == '0':
            numberValenceCheck = 'Positive_Number'

            binaryFloat = float(inputSignedBinary)
            wholeBinary = int(binaryFloat)
            decimalResult = binUnsigned2Dec(wholeBinary, 0, numberValenceCheck)

            print('\tDecimal:', decimalResult,
                  '\n\tSigned Binary:', inputSignedBinary[0:4], inputSignedBinary[4:8], inputSignedBinary[8:12],  inputSignedBinary[12:16],
                  '\n\tUnsigned Binary:', inputSignedBinary[0:4], inputSignedBinary[4:8], inputSignedBinary[8:12],  inputSignedBinary[12:16], '\n')

        elif inputSignedBinary[0] == '1':
            numberValenceCheck = 'Negative_Number'

            temp1 = inputSignedBinary.replace('1', 'x')
            temp2 = temp1.replace('0', '1')
            temp3 = temp2.replace('x', '0')

            decimalResult = float(binUnsigned2Dec(temp3, 0, numberValenceCheck)) + 1
            positiveNumberCheck = 'Positive_Number'

            decimalFloat = float(binUnsigned2Dec(temp3, 0, numberValenceCheck))
            wholeDecimal = int(decimalFloat) + 1
            fractionDecimal = round(decimalFloat - wholeDecimal, len(str(inputSignedBinary.strip())) - len(str(wholeDecimal)) + 1)
            unsignedBinaryResult = dec2BinUnsigned(decimalFloat, wholeDecimal, fractionDecimal, positiveNumberCheck)

            print('\tDecimal: -', decimalResult,
                  '\n\tSigned Binary: ', inputSignedBinary[0:4], ' ' , inputSignedBinary[4:8], ' ' , inputSignedBinary[8:12], ' ' , inputSignedBinary[12:16],
                  '\n\tUnsigned Binary: -', int(float(unsignedBinaryResult.replace(' ', ''))), '\n', sep='')

    elif choice == 'h':
        print('\nSigned binary is a method for representing negative binary numbers in a computer.\nIf you are '
              + 'unsure, then you are probably interested in choosing menu [1].\n\nSigned binary numbers use '
              + 'the left-most bit to represent its positive or negative status. \nFor example: 1000 0111 is '
              + 'negative 7; 0000 0111 is positive 7.\n')

    elif choice == 'i':
        print('This program will accept input of decimal or binary numbers and convert them.\nYou may input integers'
              + ' like \'5\' or \'9324\', or floats like \'34.645\' or \'.234\', or \'0.663\'. You may also enter'
              + ' negative numbers by including \'-\', e.g. \'-23.5\' or \'-.635\', etc.\n\nYou may enter negative'
              + ' binary numbers such as \'-10101.1101\', but you should not confuse this functionality with'
              + ' signed binary numbers, (see [h]elp for more).\n')

    else:
        print('\nInvalid choice. Choose again.\n')
