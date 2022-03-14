select	a.account_dt
	,	a.division_id
	,	d.division_nm
	,	sum(a.price) 	as sum_price
from	account		a
	,	division	d
where	1=1
and		a.division_id = d.division_id
and		a.account_dt between %(strt_dt)s and %(end_dt)s
group by a.account_dt
	   , a.division_id
	   , d.division_nm
;