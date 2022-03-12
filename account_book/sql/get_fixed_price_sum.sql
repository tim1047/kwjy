select	sum(a.price) 	as sum_price
from	account			a
	,	category_dtl	cd
where	1=1
and		a.category_id = cd.category_id
and		a.category_seq = cd.category_seq
and		a.account_dt between %(strt_dt)s and %(end_dt)s
and		cd.fixed_price_yn = 'Y'
;
