
select	b.*
from	(
			select	sum(case when a.point_yn = 'Y' and a.division_id = '3' then 0 else a.price end)	   as sum_price
				,	a.member_id
				,	(
						select	member_nm
						from	account_member	am
						where	1=1
						and		am.member_id = a.member_id
					)	as member_nm
			from	account			a
			where	1=1
			and		a.account_dt between %(strt_dt)s and %(end_dt)s
			and		a.division_id = '3'
			group by a.member_id
		) b
where	1=1
order by b.sum_price desc