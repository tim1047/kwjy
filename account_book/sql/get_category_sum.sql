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
	,	z.sum_price 			as sum_price
	,	sum(z.sum_price) over() as total_sum_price
from	(
			select	y.category_id
				,	y.division_id
				,	coalesce(sum(x.sum_price), 0)	as sum_price
			from	(
						select	c.category_id
							  , dcm.division_id
						from	category	c
							,	division_category_mpng	dcm
						where	1=1
						and		c.category_id	= dcm.category_id 
						and		dcm.division_id = %(division_id)s
					) y
			left outer join 
					(
						select	sum(a.price)	   as sum_price
							,	max(a.division_id) as division_id
							,	a.category_id
						from	account			a
						where	1=1
						and		a.account_dt between '20210901' and '20210930'
						and 	a.division_id = %(division_id)s
						group by a.category_id
							   , a.category_seq
					) x
			on		y.category_id = x.category_id
			and		y.division_id = x.division_id
			where	1=1
			group by y.category_id
				, 	 y.division_id
		) z
where	1=1		
order by cast(z.category_id as integer)
;