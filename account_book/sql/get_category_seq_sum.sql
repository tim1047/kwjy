select	y.category_id
	,	(
			select	cc.category_nm
			from	category	cc
			where	1=1
			and		cc.category_id = y.category_id
		) as category_nm
	,	y.division_id
	,	(
			select	dd.division_nm
			from	division	dd
			where	1=1
			and		dd.division_id = y.division_id
		) as division_nm
	,	y.category_seq
	,	(
			select	cd.category_seq_nm
			from	category_dtl	cd
			where	1=1
			and		cd.category_id = y.category_id
			and		cd.category_seq = y.category_seq
		) as category_seq_nm
	,	y.sum_price
	,	cast(sum(y.sum_price) over(partition by y.category_id) as integer) 	as category_sum_price
	,	cast(sum(y.sum_price) over()						   as integer)	as total_sum_price
from	(
			select	x.category_id
				  , x.division_id
				  , cd.category_seq
				  , sum(x.price) as sum_price
			from	(
						select	a.category_seq
							,	a.price
							,	a.division_id
							,	c.*
						from	account			a
							,	category		c
						where	1=1
						and		a.category_id = c.category_id
					) x
			left outer join category_dtl	cd
			on		x.category_id = cd.category_id
			and		x.category_seq = cd.category_seq
			where	1=1
			group by x.category_id
				   , cd.category_seq
				   , x.division_id
		) y
	,	division_category_mpng	dcm
where	1=1
and		y.division_id = dcm.division_id
and		y.category_id = dcm.category_id
and		y.division_id = %(division_id)s
order by cast(y.category_id as integer)
	   , y.category_seq
;