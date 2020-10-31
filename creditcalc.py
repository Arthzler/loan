import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', help='specifies the type of loan : "diff" or "annuity"')
parser.add_argument('--payment', help='monthly payment amount, only available for "annuity" type', type=float)
parser.add_argument('--principal', help='loan principal', type=float)
parser.add_argument('--periods', help='number of months needed to repay the loan', type=int)
parser.add_argument('--interest', help='loan interest rate', type=float)
args = parser.parse_args()

if args.type == 'annuity':
    if args.principal and args.payment and args.interest:
        if args.principal < 0 or args.payment < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            month_interest = args.interest / 100 / 12
            months = math.ceil(
                math.log(args.payment / (args.payment - month_interest * args.principal), 1 + month_interest))
            years, months_left = months // 12, months % 12
            if years >= 1:
                if years == 1:
                    print(f'It will take 1 year and {months_left} months to repay this loan!')
                elif months_left == 0:
                    print(f'It will take {years} years to repay this loan!')
                else:
                    print(f'It will take {years} years and {months_left} months to repay this loan!')
            else:
                if months == 1:
                    print(f'It will take 1 month to repay this loan!')
                else:
                    print(f'It will take {months_left} months to repay this loan!')
            print(f'Overpayment = {int(months * args.payment - args.principal)}')
    elif args.principal and args.periods and args.interest:
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            month_interest = args.interest / 100 / 12
            annuity = math.ceil((args.principal * month_interest * (1 + month_interest) ** args.periods
                                 / ((1 + month_interest) ** args.periods - 1)))
            print(f'Your annuity payment = {annuity}!')
            print(f'Overpayment = {int(args.periods * annuity - args.principal)}')
    elif args.payment and args.periods and args.interest:
        if args.payment < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            month_interest = args.interest / 100 / 12
            pal = math.ceil((args.payment * ((1 + month_interest) ** args.periods - 1))
                            / month_interest / (1 + month_interest) ** args.periods)
            print(f'Your loan principal = {pal}!')
            print(f'Overpayment = {int(args.periods * args.payment - pal)}')
    else:
        print('Incorrect parameters')
elif args.type == 'diff':
    if args.payment:
        print('Incorrect parameters')
    elif args.principal and args.periods and args.interest:
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            current_amt = args.principal
            diff_payments = []
            current_month = 1
            month_interest = args.interest / 100 / 12
            while current_amt > 0:
                Dm = math.ceil((args.principal / args.periods
                                + month_interest * args.principal * (1 - (current_month - 1) / args.periods)))
                diff_payments.append(Dm)
                current_amt -= Dm
                current_month += 1
            for i in range(len(diff_payments)):
                print(f'Month {i+1}: payment is {diff_payments[i]}')
            print(f'\nOverpayment = {int(sum(diff_payments) - args.principal)}')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
