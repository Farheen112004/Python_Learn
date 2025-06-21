def test(*args,**kwargs):
	for i in args:
		print(i)
	for c,d in kwargs.items():
		print(f"c{c}",f"d{d}")



FN_ARGS = ("a","b",1)
FN_KWARGS = dict(c=2,d=3)

test(FN_ARGS,kwargs={"c":2, "d":3})