select	c.*
from	(
			select	b.account_dt
				,	b.sum_price
				,	substring(b.account_dt, 0, 7) as account_yyyymm
				,	substring(b.account_dt, 7, 9) as account_dd
			from	(
						select	a.account_dt
							,	sum(a.price) as sum_price
						from	account	a
						where	1=1
						and		a.account_dt between %(strt_dt)s and %(end_dt)s
						and		a.division_id = '3'
						group by a.account_dt
					) b
			where	1=1
		) c
order by c.account_dd, c.account_yyyymm
;