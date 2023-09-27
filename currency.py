"""
Starting a class that will be a complete example of Python OOPs
We will implement operator overloading as well.

The Currency class takes rupees and paise as input. Converts
paise >=100 into rupees and proceeds

"""
'''
Operators that can be overloaded

Operator. Required Method
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
Comparison Operators :
Operator	Methods
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)
Assignment Operators :
Operator	Method to be overloaded
-=	__isub__(self, other)
+=	__iadd__(self, other)
*=	__imul__(self, other)
/=	__idiv__(self, other)
//=	__ifloordiv__(self, other)
%=	__imod__(self, other)
**=	__ipow__(self, other)
>>=	__irshift__(self, other)
<<=	__ilshift__(self, other)
&=	__iand__(self, other)
|=	__ior__(self, other)
^=	__ixor__(self, other)
Unary Operators :
Operator	Method to be overloaded
–	__neg__(self)
+	__pos__(self)
~	__invert__(self)
Note: It is not possible to change the number of operands of an operator. For ex. you cannot overload a unary operator as a binary operator. The following code will throw a syntax error.

'''
# class currency:
    