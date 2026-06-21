# פשוט מחשבון
# גרסה 2.0

from	operations	import	add,	subtract,	multiply,	divide
from	advanced	import	power,	square_root,	modulo
print("למחשבון	הבאים	ברוכים!")
print("====================")
print("\n---	בסיסיות	פעולות	---")
print(f"5	+	3	=	{add(5,	3)}")
print(f"10	-	4	=	{subtract(10,	4)}")
print(f"6	*	7	=	{multiply(6,	7)}")
print(f"20	/	4	=	{divide(20,	4)}")
print("\n---	מתקדמות	פעולות	---")
print(f"2	^	8	=	{power(2,	8)}")
print(f"√16	=	{square_root(16)}")
print(f"17	%	5	=	{modulo(17,	5)}")
