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
	, 	y.fixed_price_yn
	,	y.sum_price
	,	y.first_week_sum_price
	,	y.second_week_sum_price
	,	y.third_week_sum_price
	,	y.fourth_week_sum_price
	,	y.fifth_week_sum_price
	,	y.sixth_week_sum_price
	,	cast(sum(y.first_week_sum_price) over() as integer) 	as total_first_week_sum_price
	,	cast(sum(y.second_week_sum_price) over() as integer) 	as total_second_week_sum_price
	,	cast(sum(y.third_week_sum_price) over() as integer) 	as total_third_week_sum_price
	,	cast(sum(y.fourth_week_sum_price) over() as integer) 	as total_fourth_week_sum_price
	,	cast(sum(y.fifth_week_sum_price) over() as integer) 	as total_fifth_week_sum_price
	,	cast(sum(y.sixth_week_sum_price) over() as integer) 	as total_sixth_week_sum_price
	,	cast(sum(y.sum_price) over() as integer)				as total_sum_price
from	(
			select	cd.category_id
				,	cd.category_seq
				,	cd.fixed_price_yn
				,	x.division_id
				,	coalesce(sum(x.sum_price), 0) as sum_price
				,	coalesce(sum(case when x.week = '1' then x.sum_price end), 0) as first_week_sum_price
				,	coalesce(sum(case when x.week = '2' then x.sum_price end), 0) as second_week_sum_price
				,	coalesce(sum(case when x.week = '3' then x.sum_price end), 0) as third_week_sum_price
				,	coalesce(sum(case when x.week = '4' then x.sum_price end), 0) as fourth_week_sum_price
				,	coalesce(sum(case when x.week = '5' then x.sum_price end), 0) as fifth_week_sum_price
				,	coalesce(sum(case when x.week = '6' then x.sum_price end), 0) as sixth_week_sum_price
			from	category_dtl	cd
			left outer join
					(
						select	a.week
							,	a.category_id
							,	a.category_seq
							,	a.division_id
							,	sum(a.price) as sum_price
						from	(
									select	a.price	   
										,	a.division_id 
										,	a.category_id
										,	a.account_dt
										,	a.category_seq
										,  	CASE 
												WHEN EXTRACT(DAY FROM  to_date(a.account_dt, 'YYYYMMDD')::TIMESTAMP)::INTEGER = 1
													THEN 1 
			    								ELSE extract(week from to_date(a.account_dt, 'YYYYMMDD'):: TIMESTAMP)::integer - extract(week from ( date_trunc('month', to_date(a.account_dt, 'YYYYMMDD')::TIMESTAMP) + interval  '1 day' ) )::integer + 1
											end as week
									from	account			a
									where	1=1
									and		a.account_dt between %(strt_dt)s and %(end_dt)s
									and 	a.division_id = %(division_id)s
								) a
						where	1=1
						group by a.week
							,	a.category_id
							,	a.category_seq
							,	a.division_id
					) x
			on		x.category_id = cd.category_id
			and		x.category_seq = cd.category_seq
			where	1=1
			group by cd.category_id
				   , cd.category_seq
				   , x.division_id
		) y
left outer join 
		division_category_mpng	dcm
on		y.division_id = dcm.division_id
and		y.category_id = dcm.category_id 		
where	1=1
order by y.sum_price desc
	   , cast(y.category_id as integer)
	   , y.category_seq
;

