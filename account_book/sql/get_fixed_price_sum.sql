select	cd.category_id
	,	cd.category_seq
	,	cd.category_seq_nm
	,	a.sum_price
from	category_dtl	cd
left outer join
		(
			select	a.category_id
				  , a.category_seq
				  ,	sum(a.price)	as sum_price
			from	account			a
				,	category_dtl 	cd
			where	1=1
			and		a.category_id = cd.category_id
			and		a.category_seq = cd.category_seq
			and		a.account_dt between %(strt_dt)s and %(end_dt)s
			and		cd.fixed_price_yn = 'Y'
			group by a.category_id
				   , a.category_seq
		) a
on		cd.category_id = a.category_id
and		cd.category_seq = a.category_seq
where	1=1
and		cd.fixed_price_yn = 'Y'
order by cd.category_id
	,	cd.category_seq
;