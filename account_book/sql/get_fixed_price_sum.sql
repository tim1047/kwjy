select	x.week
	,	sum(x.price) 		as sum_price
from	(
			select	CASE 
						WHEN EXTRACT(DAY FROM  to_date(a.account_dt, 'YYYYMMDD')::TIMESTAMP)::INTEGER = 1
							THEN 1 
						ELSE extract(week from to_date(a.account_dt, 'YYYYMMDD'):: TIMESTAMP)::integer - extract(week from ( date_trunc('month', to_date(a.account_dt, 'YYYYMMDD')::TIMESTAMP) + interval  '1 day' ) )::integer + 1
					end as week
				  , a.price
			from	account			a
				,	category_dtl	cd
			where	1=1
			and		a.category_id = cd.category_id
			and		a.category_seq = cd.category_seq
			and		a.account_dt between %(strt_dt)s and %(end_dt)s
			and		a.division_id = '3'
			and		cd.fixed_price_yn = 'Y'
		) x
where	1=1
group by x.week
;