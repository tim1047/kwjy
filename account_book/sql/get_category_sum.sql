select	zz.*
	,	coalesce(cp.plan_price, 0)	as plan_price
from	(
			select	z.category_id
				,	(
						select	cc.category_nm
						from	category	cc
						where	1=1
						and		cc.category_id = z.category_id
					) as category_nm
				,	z.division_id
				,	(
						select	dd.division_nm
						from	division	dd
						where	1=1
						and		dd.division_id = z.division_id
					) as division_nm
				,  	z.category_seq
				, 	z.category_seq_nm
				,	max(z.account_yyyymm)	over()			as account_yyyymm
				,	z.sum_price 							as sum_price
				,	cast(sum(z.sum_price) over() as integer)				as total_sum_price
			from	(
						select	y.category_id
							,	y.category_seq
							, 	max(y.category_seq_nm)		as category_seq_nm
							,	y.division_id
							,	coalesce(sum(x.sum_price), 0) as sum_price
							,	to_char(now(), 'YYYYMM')	as account_yyyymm
						from	(	
									select	cc.category_id
										,	cc.division_id
										,	coalesce(cd.category_seq, '0') as category_seq
										,	cd.category_seq_nm
									from	(
												select	c.category_id
													  , dcm.division_id
												from	category	c
													,	division_category_mpng	dcm
												where	1=1
												and		c.category_id	= dcm.category_id 
												and		dcm.division_id = %(division_id)s
											) cc
									left outer join 
											category_dtl	cd
									on		cc.category_id = cd.category_id
								) y
						left outer join 
								(
									select	sum(a.price)	   		as sum_price
										,	a.division_id 			as division_id
										,	a.category_id
										,   case when a.category_seq = '' then '0' else a.category_seq end as category_seq
									from	(
												select	case when a.point_price > 0 and a.division_id = '3' then a.price - a.point_price else a.price end as price
													,	a.division_id
													,	a.category_id
													,	a.category_seq
													,	a.account_dt
												from	account			a
												where	1=1
												and		a.account_dt between %(strt_dt)s and %(end_dt)s
												and 	a.division_id = %(division_id)s
											) a
									where	1=1
									group by a.category_id
											, a.category_seq
											, a.division_id
								) x
						on		y.category_id = x.category_id
						and		y.division_id = x.division_id
						and		y.category_seq = x.category_seq
						where	1=1
						group by y.category_id
							,	 y.category_seq
							, 	 y.division_id
					) z
			where	1=1
		) zz
left outer join
		category_plan	cp
on		zz.category_id 	= cp.category_id
and		zz.account_yyyymm = cp.plan_dt
where	1=1
order by zz.sum_price desc, cast(zz.category_id as integer)
;