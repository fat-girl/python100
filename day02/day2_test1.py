"""
英寸与厘米的互换
英寸(in)==厘米(cm)*2.54
"""
value = float(input('请输入长度：'))
unit = input("请输入单位：")
if unit == 'in' or unit == '英寸':
    print('%.2f英寸==%.2f厘米' % (value,value/2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f厘米==%.2f英寸' % (value,value*2.54))
else:
    print('error')

