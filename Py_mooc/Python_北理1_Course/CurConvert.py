# CurConvert.py 人民币与美元转换
CurStr = input()
if CurStr[:3] in ['RMB']:
    USD = (eval(CurStr[3:]))/6.78
    print("USD{:.2f}".format(USD))
elif CurStr[:3] in ['USD']:
    RMB = eval(CurStr[3:]) * 6.78
    print("RMB{:.2f}".format(RMB))
else:
    print()
