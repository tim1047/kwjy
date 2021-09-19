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
	,	z.first_week_sum_price
	,	z.second_week_sum_price
	,	z.third_week_sum_price
	,	z.fourth_week_sum_price
	,	z.fifth_week_sum_price
	,	z.sixth_week_sum_price
	,	cast(sum(z.first_week_sum_price) over() as integer) 	as total_first_week_sum_price
	,	cast(sum(z.second_week_sum_price) over() as integer) 	as total_second_week_sum_price
	,	cast(sum(z.third_week_sum_price) over() as integer) 	as total_third_week_sum_price
	,	cast(sum(z.fourth_week_sum_price) over() as integer) 	as total_fourth_week_sum_price
	,	cast(sum(z.fifth_week_sum_price) over() as integer) 	as total_fifth_week_sum_price
	,	cast(sum(z.sixth_week_sum_price) over() as integer) 	as total_sixth_week_sum_price
	,	cast(sum(z.sum_price) over() as integer)				as total_sum_price
from	(
			select	y.category_id
				,	y.division_id
				,	coalesce(sum(x.sum_price), 0) as sum_price
				,	coalesce(sum(case when x.week = '1' then x.sum_price end), 0) as first_week_sum_price
				,	coalesce(sum(case when x.week = '2' then x.sum_price end), 0) as second_week_sum_price
				,	coalesce(sum(case when x.week = '3' then x.sum_price end), 0) as third_week_sum_price
				,	coalesce(sum(case when x.week = '4' then x.sum_price end), 0) as fourth_week_sum_price
				,	coalesce(sum(case when x.week = '5' then x.sum_price end), 0) as fifth_week_sum_price
				,	coalesce(sum(case when x.week = '6' then x.sum_price end), 0) as sixth_week_sum_price
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
							, 	a.week
						from	(
									select	a.price
										,	a.division_id
										,	a.category_id
										,	a.category_seq
										,  	CASE 
												WHEN EXTRACT(DAY FROM  to_date(a.account_dt, 'YYYYMMDD')::TIMESTAMP)::INTEGER = 1
												THEN 1 
											ELSE extract(week from to_date(a.account_dt, 'YYYYMMDD'):: TIMESTAMP)::integer - extract(week from ( date_trunc('month', to_date(a.account_dt, 'YYYYMMDD')::TIMESTAMP) + interval  '1 day' ) )::integer + 1
											end as week
									from	account			a
									where	1=1
									and		a.account_dt between '20210901' and '20210930'
									and 	a.division_id = %(division_id)s
								) a
						where	1=1
						group by a.category_id
								, a.category_seq
								, a.week
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