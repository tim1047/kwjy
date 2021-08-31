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
	,	y.sum_price
	,	sum(y.sum_price) over() 							as total_sum_price
from	(
			select	a.category_id
				  , a.division_id
				  , sum(a.price) as sum_price	
			from	account			a
				,	category		c
			where	1=1
			and		a.category_id = c.category_id		
			group by a.category_id
				   , a.division_id
		) y
	,	division_category_mpng	dcm
where	1=1
and		y.division_id = dcm.division_id
and		y.category_id = dcm.category_id
and		y.division_id = %(division_id)s
order by cast(y.category_id as integer)
;